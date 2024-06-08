__version__ = 1
import time

class Timer:
    def __init__(self) -> None:
        self.reset()
    def reset(self) -> int:
        self.ctime = time.time()
        return self.ctime
    def get_time(self) -> int:
        return (time.time()-self.ctime)