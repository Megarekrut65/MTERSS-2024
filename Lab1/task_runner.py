import threading
import time

from app.maclaurin import MaclaurinSeries


class RunUntil:
    def __init__(self, target, args):
        self.__result = None
        self.__is_done = False

        self.__task = threading.Thread(target=self.__run, args=(target, args))

    def __run(self, target, args):
        self.__result = None
        self.__is_done = False

        self.__result = target(*args)
        self.__is_done = True

    def get(self):
        return self.__result

    def is_done(self):
        return self.__is_done

    def start(self, timeout):
        self.__task.start()

        while not self.__is_done and timeout > 0:
            time.sleep(1)
            timeout-=1

        if self.__is_done:
            self.__task.join()


def run_task(algo, x, eps):
    try:
        y, n = algo.evaluate(x, eps)
        return y, n
    except ValueError as e:
        print(e)
        return None, None

def run_until_completed(x, eps, timeout=15*60):
    algo = MaclaurinSeries()

    runner = RunUntil(run_task, (algo, x, eps))
    runner.start(timeout)

    if runner.is_done():
        return runner.get()

    print("Timeout reached. Canceling computation task")
    algo.cancel = True
    return None, None