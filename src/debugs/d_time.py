import time

moove_count = 0

class Debug:
    def __init__(self):
        self.t_start = time.perf_counter()
        self.t_ms = 0.0000
    def stop(self):
        t_final = time.perf_counter() - self.t_start
        self.t_ms = t_final * 1000
        print(f"\n => Time elapsed: {self.t_ms:.2f} ms")
        print(f" => Moove: {moove_count}")
