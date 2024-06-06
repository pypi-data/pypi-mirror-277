import pandas as pd
from loguru import logger

from dataframe_decorators.utils import get_prefix


def _report_on_dataframe(df: pd.DataFrame):
    if len(df) == 0:
        raise ValueError("The DataFrame passed is empty.")
    return set(list(df.columns)), df.shape, df.dtypes


def _report_dataframe_delta(
    df: pd.DataFrame, og_columns, og_shape, og_dtypes, prefix: str
):
    new_columns, new_shape, new_dtypes = _report_on_dataframe(df)

    columns_added = list(new_columns - og_columns)
    columns_removed = list(og_columns - new_columns)
    shared_index_rows = og_dtypes.index.intersection(new_dtypes.index)
    dtype_changed_og = og_dtypes[shared_index_rows][
        og_dtypes[shared_index_rows] != new_dtypes[shared_index_rows]
    ]
    dtype_changed_new = new_dtypes[shared_index_rows][
        og_dtypes[shared_index_rows] != new_dtypes[shared_index_rows]
    ]
    rows_delta = new_shape[0] - og_shape[0]

    if len(columns_added) > 0:
        logger.info(f"{prefix} | Columns added: {', '.join(columns_removed)}")
    if len(columns_removed) > 0:
        logger.info(f"{prefix} | Columns removed: {', '.join(columns_removed)}")
    if rows_delta != 0:
        logger.info(f"{prefix} | Number rows delta: {rows_delta}")
    if len(dtype_changed_og) > 0:
        logger.info(
            f"{prefix} | Data type changes:\n{dtype_changed_og}\nTO:\n{dtype_changed_new}"
        )


def pipe(func):
    """
    Decorator for functions that accept a dataframe and return a dataframe
    """

    prefix = get_prefix(func, "pipe")

    def wrapper(*args, **kwargs):
        og_columns, og_shape, og_dtypes = None, None, None
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, pd.DataFrame):
                og_columns, og_shape, og_dtypes = _report_on_dataframe(arg)
                break
        if og_columns is None:
            raise ValueError(
                "No DataFrame found in args or kwargs, should not be tagged a pipe"
            )

        logger.info(f"{prefix} | start")
        output = func(*args, **kwargs)
        if isinstance(output, pd.DataFrame):
            _report_dataframe_delta(output, og_columns, og_shape, og_dtypes, prefix)
        else:
            logger.warning(
                f"{prefix} | Output is not a DataFrame, should not be decorated a pipe"
            )
        return output

    return wrapper
