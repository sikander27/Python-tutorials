#!/usr/bin/env python3
import logging
import time
import threading
from concurrent.futures import ThreadPoolExecutor


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        with self._lock.obtain():
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy 


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info(f"Tesing start: initial value : {database.value}")
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info(f"Tesing Ends: final value : {database.value}")

