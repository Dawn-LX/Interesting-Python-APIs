import time
import logging

_LOG_FMT = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s'
_DATE_FMT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=_LOG_FMT, datefmt=_DATE_FMT, level=logging.INFO)
LOGGER = logging.getLogger('__main__')  # this is the global logger


def add_log_to_file(log_path):
    fh = logging.FileHandler(log_path)
    formatter = logging.Formatter(_LOG_FMT, datefmt=_DATE_FMT)
    fh.setFormatter(formatter)
    LOGGER.addHandler(fh)


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
