# Description
Getting a logger in PySB, optionally with model-specific logging.

# Code
```
import logging
import warnings
import pysb

BASE_LOGGER_NAME = 'pysb'

class PySBModelLoggerAdapter(logging.LoggerAdapter):
    """ A logging adapter to prepend a model's name to log entries """
    def process(self, msg, kwargs):

def get_logger(logger_name=BASE_LOGGER_NAME, model=None, log_level=None,
               **kwargs):
    """
    Returns (if extant) or creates a PySB logger

    If the PySB base logger has already been set up, this method will return it
    or any of its descendant loggers without overriding the settings - i.e.
    any values supplied as kwargs will be ignored.

    Parameters
    ----------
    logger_name : string
        Get a logger for a specific namespace, typically __name__ for code
        outside of classes or self.__module__ inside a class
    model : pysb.Model
        If this logger is related to a specific model instance, pass the
        model object as an argument to have the model's name prepended to
        log entries
    log_level : bool or int
        Override the default or preset log level for the requested logger.
        None or False uses the default or preset value. True evaluates to
        logging.DEBUG. Any integer is used directly.
    **kwargs : kwargs
        Keyword arguments to supply to :func:`setup_logger`. Only used when
        the PySB logger hasn't been set up yet (i.e. there have been no
        calls to this function or :func:`get_logger` directly).

    Returns
    -------
    A logging.Logger object with the requested name

    Examples
    --------

    >>> from pysb.logging import get_logger
    >>> logger = get_logger(__name__)
    >>> logger.debug('Test message')
    """
    if BASE_LOGGER_NAME not in logging.Logger.manager.loggerDict.keys():
        setup_logger(**kwargs)
    elif kwargs:
        warnings.warn('PySB logger already exists, ignoring keyword '
                      'arguments to setup_logger')

    logger = logging.getLogger(logger_name)

    if log_level is not None and log_level is not False:
        if isinstance(log_level, bool):
            log_level = logging.DEBUG
        elif not isinstance(log_level, int):
            raise ValueError('log_level must be a boolean, integer or None')

        if logger.getEffectiveLevel() != log_level:
            logger.debug('Changing log_level from %d to %d' % (
                logger.getEffectiveLevel(), log_level))
            logger.setLevel(log_level)

    if model is None:
        return logger
    else:

```
