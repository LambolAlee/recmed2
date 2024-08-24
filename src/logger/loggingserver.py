import logging
import logging.handlers
import multiprocessing

from pathlib import Path
from time import sleep, ctime



def configLogEnviron(queue):
    """
    Everytime in a new process, we should call this fucntion to initialize the logger system
    """
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    handler = logging.handlers.QueueHandler(queue)
    handler.setLevel(logging.DEBUG)
    # handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s !> <%(name)s> %(message)s'))
    rootLogger.addHandler(handler)



class LoggingServer(multiprocessing.Process):
    def __init__(self, logDir: Path) -> None:
        super().__init__(name="LoggingServer")
        self.logDir = logDir
        self.message_queue: multiprocessing.Queue[logging.LogRecord] = multiprocessing.Queue()
        self.initialized = multiprocessing.Value('b', False)

    # operation in new process (not main process)
    def waitForInitializing(self):
        while True:
            if self.initialized.value:
                break
            else:
                sleep(1)

    # operation in new process (not main process)
    def initRootLogger(self):
        log_path = self.logDir / (ctime().replace(' ', '-').replace(":", ".") + ".log"); print(log_path)

        serverRootLogger = logging.getLogger()
        serverRootLogger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s => <%(name)s> %(message)s'))
        serverRootLogger.addHandler(handler)

        std_out = logging.StreamHandler()
        std_out.setLevel(logging.INFO)
        std_out.setFormatter(logging.Formatter('%(levelname)s => <%(name)s> %(message)s'))
        serverRootLogger.addHandler(std_out)

    # operation in new process (not main process)
    def run(self) -> None:
        self.initRootLogger()
        server_self = logging.getLogger("LoggingServer")
        server_self.info("LoggingServer started...")
        self.initialized.value = True   # type: ignore
        while True:
            record = self.message_queue.get()
            if record is None:
                server_self.info("LoggingServer closed")
                self.message_queue.close()
                break
            else:
                logger_client = logging.getLogger(record.name)
                logger_client.handle(record)

    def stop(self):
        server_self = logging.getLogger("LoggingServer")
        server_self.info("Closing LoggingServer...")
        self.message_queue.put_nowait(None)

    def __enter__(self):
        self.start()
        self.waitForInitializing()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not isinstance(exc_value, SystemExit):
            print("\n ***LoggingServer error condition:")
            print(exc_type, exc_value, traceback, sep='\n')
        self.stop()
        self.join()