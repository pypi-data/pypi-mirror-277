import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, log_file='app.log', level=logging.INFO, max_bytes=10485760, backup_count=5):
        """
        Initializes the Logger instance.

        :param name: The name of the logger.
        :param log_file: The file to log to.
        :param level: The logging level.
        :param max_bytes: Maximum size of log file before rotation.
        :param backup_count: Number of backup log files to keep.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_file = log_file

        # Create file handler which logs even debug messages
        if not self.logger.handlers:
            # Prevent adding multiple handlers if logger is already configured
            file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
            file_handler.setLevel(level)

            # Create console handler with a higher log level
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.ERROR)

            # Create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        """
        Returns the configured logger instance.

        :return: Configured logger.
        """
        return self.logger

# Example usage within the module
logger = Logger(name=__name__).get_logger()
logger.info("Logger initialized successfully.")
