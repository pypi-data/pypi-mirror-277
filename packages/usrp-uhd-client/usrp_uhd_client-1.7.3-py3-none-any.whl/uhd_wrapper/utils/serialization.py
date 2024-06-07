"""This module contains functions required for serialization.

Since we use zerorpc for RPC, we need to serialize non-pythonic datatypes.
"""

import numpy as np


SerializedComplexArray = bytes
"""Bytes containing the data as serialized complex64 format"""


def serializeComplexArray(data: np.ndarray) -> SerializedComplexArray:
    """Serialize a complex array.

    Args:
        data (np.ndarray): Onedimensional array of complex samples.

    Raises:
        ValueError: Array must be one dimensional.

    Returns:
        SerializedComplexArray: Serialized data.

    """
    data = np.squeeze(data)
    if len(data.shape) == 2:
        raise ValueError("Array must be one dimensional!")
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Only numeric arrays can be serialized!")
    res = data.astype(np.complex64).tobytes()
    return res


def deserializeComplexArray(data: SerializedComplexArray) -> np.ndarray:
    """Deserialize into a complex array.

    Args:
        data (SerializedComplexArray): Samples.
    Raises:
        ValueError: Number of samples must match

    Returns:
        np.ndarray: One dimensional numpy array.
    """
    X = np.frombuffer(data, dtype=np.complex64)
    return X
    if len(data[0]) != len(data[1]):
        raise ValueError(
            """Number of imaginary samples
                            mismatches number of real samples."""
        )
    arr = np.array(data[0]) + 1j * np.array(data[1])
    return arr
