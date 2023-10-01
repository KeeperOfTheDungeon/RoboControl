import functools
import threading
import time


def blocking_ratelimit(times=1, seconds=1):
    """ slowed down to run x times per y seconds """

    def limiter(fn):
        semaphore = threading.Semaphore(times)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            semaphore.acquire()
            try:
                return fn(*args, **kwargs)
            finally:
                timer = threading.Timer(seconds, semaphore.release)
                timer.setDaemon(True)
                timer.start()
        return wrapper

    return limiter


def dropping_ratelimit(times=1, seconds=1):
    """ allowed to run x times per y seconds """

    def limiter(fn):
        calls, last_reset = 0, time.time()

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset
            elapsed = time.time() - last_reset
            if int(elapsed) > seconds:
                calls, last_reset = 0, time.time()
            if calls < times:
                return fn(*args, **kwargs)
            calls += 1
        return wrapper

    return limiter
