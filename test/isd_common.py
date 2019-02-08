import logging
import os
import unittest


class ISDTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        if (os.getenv('LOG_LEVEL')):
            stream_handler = logging.StreamHandler()
            stream_handler_formatter = logging.Formatter(
                '%(asctime)s %(levelname)-8s %(name)-12s %(funcName)-12s %(message)s'
            )
            stream_handler.setFormatter(stream_handler_formatter)
            logging_level = logging._nameToLevel.get(
                os.getenv('LOG_LEVEL'), logging.info)
            cls.logger.setLevel(logging_level)
            cls.logger.addHandler(stream_handler)
            # Try to use the same log level also for prange_isd module
            prange_isd_logger = logging.getLogger('isd.prange_isd')
            prange_isd_logger.setLevel(logging_level)
            prange_isd_logger.addHandler(stream_handler)