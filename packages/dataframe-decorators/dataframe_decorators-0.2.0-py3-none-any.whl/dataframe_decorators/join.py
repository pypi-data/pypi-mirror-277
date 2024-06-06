import pandas as pd
from loguru import logger

from dataframe_decorators.utils import get_prefix


def join(func):
    """
    Decorator for functions that accept two dataframes and return a dataframe. The two dataframes are joined.
    """

    def wrapper(*args, **kwargs):
        prefix = get_prefix(func, "feature")
        df_list = []
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, pd.DataFrame):
                df_list.append(arg)
        logger.info(f"{prefix} | {len(df_list)} DataFrames passed")
        output = func(*args, **kwargs)
        return output

    return wrapper
