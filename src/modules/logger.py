#src/logger.py


import logging
import logging.config
import os



from config.config import LOGGER_CONFIG

class LoggerManager:
    @staticmethod
    def configure_logger(name:str =' default', logger_config:dict = LOGGER_CONFIG, verbose: bool = False) -> logging.Logger:

        if name not in logger_config["logging"]["loggers"]:
            raise ValueError(f"Logger {name} not found in logging config file")
        else:
            log_directory = os.path.dirname(logger_config["logging"]["handlers"]["file"]["filename"])
            os.makedirs(log_directory, exist_ok=True)
            logging.config.dictConfig(logger_config["logging"])

            logger = logging.getLogger(name)

            if verbose:
                level = logging.DEBUG
            else:
                level = logging.INFO
            
            logger.setLevel(level)

            return logger