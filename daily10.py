"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import threading
from time import sleep, time


# Stupid simple solution
# def scheduler(f, n):
#     time.sleep(n / 1000)
#     return f()


# print(scheduler(lambda: 1 + 2, 1))


# More elegant solution


class Scheduler:
    def __init__(self):
        self.fns = []  # (fn, time) tuple
        sched = threading.Thread(target=self.scheduler_loop)
        sched.start()

    def scheduler_loop(self):
        while True:
            now = time() * 1000
            for fn, run_time in self.fns:
                if now > run_time:
                    fn()
            self.fns = [(fn, run_time)
                        for (fn, run_time) in self.fns if run_time > now]
            sleep(1 / 1000)  # run every millisecond

    def schedule(self, f, n):
        self.fns.append((f, time() * 1000 + n))


scheduler = Scheduler()
scheduler.schedule(lambda: print("5 seconds passed!"), 5)
