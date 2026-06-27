import time
import storage


class Timer:

    def __init__(self):
        self.data = storage.load()

    def start(self):

        if self.data["start_time"] is None:

            self.data["start_time"] = int(time.time())
            self.data["paused"] = False
            self.data["paused_total"] = 0

            storage.save(self.data)

    def pause(self):

        if self.data["paused"]:
            return

        self.data["paused"] = True
        self.data["pause_time"] = int(time.time())

        storage.save(self.data)

    def resume(self):

        if not self.data["paused"]:
            return

        paused_for = int(time.time()) - self.data["pause_time"]

        self.data["paused_total"] += paused_for
        self.data["paused"] = False
        self.data["pause_time"] = None

        storage.save(self.data)

    def stop(self):

        storage.reset()
        self.data = storage.load()

    def elapsed(self):

        if self.data["start_time"] is None:
            return 0

        now = int(time.time())

        elapsed = now - self.data["start_time"] - self.data["paused_total"]

        if self.data["paused"]:
            elapsed -= now - self.data["pause_time"]

        return elapsed

    def timestamp(self):

        if self.data["start_time"] is None:
            return int(time.time())

        return self.data["start_time"] + self.data["paused_total"]
