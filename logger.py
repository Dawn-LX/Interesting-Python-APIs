import time
import logging


_LOG_FMT = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s'
_DATE_FMT = '%Y-%m-%d %H:%M:%S'

LOGGER = logging.getLogger('__main__')  # this is the global logger
LOGGER.setLevel(logging.DEBUG)

def add_log_to_file(log_path):
    formatter = logging.Formatter(_LOG_FMT, datefmt=_DATE_FMT)

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    LOGGER.addHandler(file_handler)

    terminal_handler = logging.StreamHandler()
    terminal_handler.setLevel(logging.INFO)
    terminal_handler.setFormatter(formatter)
    LOGGER.addHandler(terminal_handler)
    
    # so that LOGGER.debug("...") will only be logging to file, not the terminal

    LOGGER.info("-="*20)


def get_timestamp():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())

def display_args(args):
    txt = "\n"
    max_name_len = max(len(arg_name) for arg_name in vars(args))
    for arg_name in vars(args):
        arg_value = getattr(args,arg_name)
        arg_type = type(arg_value)
        txt += "{:{L}}:\t{} {}\n".format(arg_name,arg_value,arg_type,L=max_name_len+1)
    
    return txt

def logger_demo():
    add_log_to_file("test_APIs/my_log_file2.log")
    LOGGER.debug("this is debug level, which will only be logged to the file")
    LOGGER.info("this is info level, which will be logged to both the terminal and the file")
    
