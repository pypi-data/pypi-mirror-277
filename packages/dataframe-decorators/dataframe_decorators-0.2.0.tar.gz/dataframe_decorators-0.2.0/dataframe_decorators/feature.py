import pandas as pd
from loguru import logger

from dataframe_decorators.utils import get_prefix


def feature(func):
    """
    Decorator for functions that accept a dataframe and return a series. The series is added as a new column to the dataframe.
    """
    prefix = get_prefix(func, "feature")

    def wrapper(*args, **kwargs):
        column_name = func.__name__
        logger.info(f"{prefix} | adding {column_name}")
        output = func(*args, **kwargs)
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, pd.DataFrame):
                first_df = arg
                break
        first_df[column_name] = output
        return first_df

    return wrapper
