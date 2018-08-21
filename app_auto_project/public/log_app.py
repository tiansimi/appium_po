__author__ = 'lenovo'
import logging


class Logger():
    # 控制台输出的是clevel 文件中输出的是flevel
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        fh = logging.FileHandler(path)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        sh.setFormatter(fmt)
        fh.setFormatter(fmt)
        sh.setLevel(clevel)
        fh.setLevel(flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
















