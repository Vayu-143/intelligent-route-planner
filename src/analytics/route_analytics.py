import time


class RouteAnalytics:

    def __init__(self):

        self.start_time = None
        self.end_time = None

    def start(self):

        self.start_time = time.perf_counter()

    def stop(self):

        self.end_time = time.perf_counter()

    def execution_time(self):

        return round(
            (
                self.end_time
                - self.start_time
            )
            * 1000000,
            4
        )