import logging
from datetime import datetime

_KNOW_USERS = "log/know_users.txt"
_ACCESS_LOG = "log/access_log.txt"
_ERROR_LOG = "log/error_log.txt"

formatter = logging.Formatter('%(asctime)s %(message)s',
                              datefmt="%Y/%m/%d-%H:%M:%S")


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


_ACCESS_LOGGER = setup_logger("ACCESS_LOG", _ACCESS_LOG)
ERROR_LOGGER = setup_logger("ERROR_LOG", _ERROR_LOG, level=logging.ERROR)


def add_known_user(user):
    try:
        if not is_user_known(user):
            with open(_KNOW_USERS, 'a') as f:
                f.write(f"{_now()}-{user}")
                f.write('\n')
    except Exception as error:
        ERROR_LOGGER.error("LOG:add_known_user: " + str(error))


def is_user_known(user):
    try:
        with open(_KNOW_USERS, 'r') as f:
            for line in f:
                if str(user) in line:
                    return True

        return False
    except Exception as error:
        ERROR_LOGGER.error("LOG:is_user_known: " + str(error))
        return False


def log_access(user, command):
    _ACCESS_LOGGER.info(f"{user}:{command}")


def _now():
    strformat = "%Y/%m/%d-%H:%M:%S"
    return datetime.strftime(datetime.now(), strformat)
