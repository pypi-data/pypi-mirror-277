from cli_chess.core.game import GameModelBase
from cli_chess.menus.tv_channel_menu import TVChannelMenuOptions
from cli_chess.utils.event import Event
from cli_chess.utils.logging import log
from chess import COLOR_NAMES, COLORS, Color, WHITE, BLACK
from berserk.exceptions import ResponseError
from time import sleep
import threading


class WatchTVModel(GameModelBase):
    def __init__(self, channel: TVChannelMenuOptions):
        super().__init__(variant=channel.variant, fen=None)
        self.channel = channel
        self._tv_stream = StreamTVChannel(self.channel)
        self._tv_stream.e_tv_stream_event.add_listener(self.stream_event_received)

    def start_watching(self):
        """Notify the TV stream thread to start"""
        self._tv_stream.start()

    def stop_watching(self):
        """Stop the TV stream thread"""
        if self._tv_stream.is_alive():
            self._tv_stream.stop_watching()

    def _update_game_metadata(self, **kwargs) -> None:
        """Parses and saves the data of the game being played"""
        try:
            if 'tv_descriptionEvent' in kwargs:
                data = kwargs['tv_descriptionEvent']
                if 'tv_startGameEvent' in kwargs:
                    self.game_metadata.reset()

                self.game_metadata.game_id = data.get('id')
                self.game_metadata.rated = data.get('rated')
                self.game_metadata.variant = data.get('variant')
                self.game_metadata.speed = data.get('speed')
                self.game_metadata.game_status.status = data.get('status')
                self.game_metadata.game_status.winner = data.get('winner')  # Not included on draws or abort

                for color in COLOR_NAMES:
                    color_as_bool = Color(COLOR_NAMES.index(color))
                    side_data = data.get('players', {}).get(color, {})
                    player_data = side_data.get('user')
                    ai_level = side_data.get('aiLevel')
                    if side_data and player_data:
                        self.game_metadata.players[color_as_bool].title = player_data.get('title')
                        self.game_metadata.players[color_as_bool].name = player_data.get('name', "?")
                        self.game_metadata.players[color_as_bool].rating = side_data.get('rating', "?")
                        self.game_metadata.players[color_as_bool].is_provisional_rating = side_data.get('provisional', False)
                        self.game_metadata.players[color_as_bool].rating_diff = side_data.get('ratingDiff', "")
                    elif ai_level:
                        self.game_metadata.players[color_as_bool].name = f"Stockfish level {ai_level}"

            if 'tv_coreGameEvent' in kwargs:
                data = kwargs['tv_coreGameEvent']
                for color in COLORS:
                    self.game_metadata.clocks[color].units = "sec"
                    self.game_metadata.clocks[color].time = data.get('wc' if color == WHITE else 'bc')

            self.e_game_model_updated.notify()
        except Exception as e:
            log.error(f"Error saving game metadata: {e}")
            raise

    def stream_event_received(self, **kwargs):
        """An event was received from the TV thread. Raises exception on invalid data"""
        try:
            if 'searchingForGame' in kwargs:
                self.e_game_model_updated.notify(searchingForGame=True)

            if 'tvGameFound' in kwargs:
                self.e_game_model_updated.notify(tvGameFound=True)

            if 'startGameEvent' in kwargs:
                event = kwargs['startGameEvent']
                variant = event.get('variant', {}).get('key')
                white_rating = int(event.get('players', {}).get('white', {}).get('rating') or 0)
                black_rating = int(event.get('players', {}).get('black', {}).get('rating') or 0)
                orientation = WHITE if ((white_rating >= black_rating) or self.channel.key == "racingKings") else BLACK

                self._update_game_metadata(tv_descriptionEvent=event, tv_startGameEvent=True)
                last_move = event.get('lastMove', "")
                if variant == "crazyhouse" and len(last_move) == 4 and last_move[:2] == last_move[2:]:
                    # NOTE: This is a dirty fix. When streaming a crazyhouse game from lichess, if the
                    #   last move field in the initial stream output is a drop, lichess sends this as
                    #   e.g. e2e2 instead of N@e2. This causes issues parsing the UCI as e2e2 is invalid.
                    #   Considering we only use `lm` and `lastMove` for highlighting squares, this fix
                    #   changes this to a valid UCI string to still allow the square to be highlighted.
                    #   Without this, an exception will occur and we will call the API again, which is unnecessary.
                    last_move = "k@" + last_move[2:]

                self.board_model.reinitialize_board(variant, orientation, event.get('fen'), last_move)
                self.e_game_model_updated.notify(tvPositionUpdated=True)

            if 'coreGameEvent' in kwargs:
                # NOTE: the `lm` field that lichess sends is not valid UCI. It should only be used
                #       for highlighting move squares (invalid castle notation, missing promotion piece, etc).
                event = kwargs['coreGameEvent']
                self._update_game_metadata(tv_coreGameEvent=event)
                self.board_model.set_board_position(event.get('fen'), uci_last_move=event.get('lm'))
                self.e_game_model_updated.notify(tvPositionUpdated=True)

            if 'endGameEvent' in kwargs:
                event = kwargs['endGameEvent']
                self._update_game_metadata(tv_descriptionEvent=event)
                self.e_game_model_updated.notify(onlineGameOver=True)

            if 'tvError' in kwargs:
                self.e_game_model_updated.notify(tvError=True, msg=kwargs.get('msg'))
        except Exception as e:
            log.error(f"Error parsing stream data: {e}")
            raise


class StreamTVChannel(threading.Thread):
    def __init__(self, channel: TVChannelMenuOptions):
        super().__init__(daemon=True)
        self.channel = channel
        self.current_game = ""
        self.running = False
        self.max_retries = 10
        self.retries = 0
        self.e_tv_stream_event = Event()

        try:
            from cli_chess.core.api.api_manager import api_client
            self.api_client = api_client
        except ImportError:
            # TODO: Clean this up so the error is displayed on the main screen
            log.error("Failed to import api_client")
            raise ImportError("API client not setup. Do you have an API token linked?")

        # Current flow that has to be followed to watch the "variant" tv channels
        # as /api/tv/feed is only for the top-rated game, and doesn't allow channel specification
        # 1. Get current tv game (/api/tv/channels) -> Get the game ID for the game we're interested in
        # 2. Start streaming game, on initial input set board orientation, show player names, etc. On follow up set pos.
        # 3. When the game completes, start this loop over.

    def get_channel_game_id(self, channel: TVChannelMenuOptions) -> str:
        """Returns the game ID of the ongoing TV game of the passed in channel"""
        channel_game_id = self.api_client.tv.get_current_games().get(channel.key, {}).get('gameId')
        if not channel_game_id:
            raise ValueError(f"TV Stream: Didn't receive game ID for current {channel.value} TV game")

        return channel_game_id

    def run(self):
        """Main entrypoint for the thread"""
        log.info(f"Started watching {self.channel.value} TV")
        self.running = True
        while self.running:
            try:
                self.e_tv_stream_event.notify(searchingForGame=True)
                game_id = self.get_channel_game_id(self.channel)

                if game_id != self.current_game:
                    self.current_game = game_id
                    turns_behind = 0
                    stream = self.api_client.games.stream_game_moves(game_id)

                    for event in stream:
                        # TODO: This does close the stream, but not until the next event comes in (which can be a while
                        #  sometimes (especially in longer time format games like Classical). Ideally there's
                        #  a way to immediately kill the stream, without waiting for another event. This is certainly
                        #  something to watch for since if a user backs out of multiple TV streams and immediately
                        #  enters another streams/threads will start to compound streams/threads and quickly
                        #  bring us close to the 8 streams open per IP limit.
                        if not self.running:
                            stream.close()
                            break

                        fen = event.get('fen')
                        winner = event.get('winner')
                        status = event.get('status', {}).get('name')

                        if winner or status != "started" and status:
                            log.info(f"Game finished: {game_id}")
                            self.e_tv_stream_event.notify(endGameEvent=event)
                            break

                        if status == "started":
                            log.info(f"Started streaming TV game: {game_id}")
                            self.e_tv_stream_event.notify(startGameEvent=event, tvGameFound=True)
                            turns_behind = event.get('turns', 0)

                        if fen:
                            if turns_behind <= 2:
                                if event.get('wc') and event.get('bc'):
                                    self.e_tv_stream_event.notify(coreGameEvent=event)
                            else:
                                # Keeping track of turns behind allows skipping this event until
                                # we are caught up. This stops a quick game replay from happening.
                                # We do however want to grab the last move event to pick up the clock data.
                                turns_behind -= 1

            except Exception as e:
                self.handle_exceptions(e)

            else:
                if self.running:
                    self.retries = 0
                    log.debug("Sleeping 2 seconds before finding next TV game")
                    sleep(2)

    def handle_exceptions(self, e: Exception):
        """Handles the passed in exception and responds appropriately"""
        if self.retries <= self.max_retries:
            log.error(e)
            self.current_game = ""
            delay = 2 * (self.retries + 1)

            if isinstance(e, ResponseError):
                if e.status_code == 429:
                    delay = 60

            # TODO: Send event to model with retry notification so we can display it to the user
            log.info(f"Sleeping {delay} seconds before retrying ({self.max_retries - self.retries} retries left).")
            self.e_tv_stream_event.notify(tvError=True, msg=f"Error streaming. Retrying in {delay} seconds.")
            sleep(delay)
            self.retries += 1
        else:
            self.stop_watching()

    def stop_watching(self):
        log.info("Stopping TV stream")
        self.e_tv_stream_event.notify(tvError=True, msg="Retries exhausted. Stopping TV.")
        self.e_tv_stream_event.remove_all_listeners()
        self.running = False
