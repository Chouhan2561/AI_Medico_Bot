# ==========================================================
# Puzzle Generator Studio
# Game Timer
# ==========================================================

import time


class GameTimer:
    """
    Simple Game Timer.

    Responsibilities

    • Start Timer

    • Stop Timer

    • Reset Timer

    • Get Elapsed Time

    • Format Time
    """

    def __init__(self):

        self.start_time = None

        self.end_time = None

        self.running = False

    # ======================================================
    # Start Timer
    # ======================================================

    def start(self):

        self.start_time = time.time()

        self.running = True

    # ======================================================
    # Stop Timer
    # ======================================================

    def stop(self):

        self.end_time = time.time()

        self.running = False

    # ======================================================
    # Reset Timer
    # ======================================================

    def reset(self):

        self.start_time = None

        self.end_time = None

        self.running = False

    # ======================================================
    # Get Elapsed Seconds
    # ======================================================

    def elapsed_seconds(self):

        if self.start_time is None:

            return 0

        if self.running:

            return int(

                time.time()

                -

                self.start_time

            )

        return int(

            self.end_time

            -

            self.start_time

        )

    # ======================================================
    # Format Time
    # ======================================================

    def formatted_time(self):

        seconds = self.elapsed_seconds()

        minutes = seconds // 60

        remaining_seconds = seconds % 60

        return f"{minutes:02}:{remaining_seconds:02}"

    # ======================================================
    # Check Running
    # ======================================================

    def is_running(self):

        return self.running