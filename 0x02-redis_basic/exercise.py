#!/usr/bin/env python3
"""
implements Cache class
"""
import redis
import random
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a rondom uuid4 str and store the input data on Redis.
        Args:
            data - data to be stored in the database.
        Return:
            str - random uuid4
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[bytes, str, None]:
        """
        Retrieves data from Redis and optionally apply a conversion function.
        Args:
            key (str): The key to retrieve from Redis.
            fn (Callable, Optional): A function to convert the data
                 to the desired format.
        Return:
            The data stored in Redis, potentially converted by `fn`,
            or None if the key doesn't exists.
        """
        val = self._redis.get(key)
        if val is not None and fn is not None:
            return fn(val)
        return val

    def get_str(self, key=str) -> str:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            str: The retrieved data as a UTF-8 string,
            or None if the key doesn't exist.
        """
        def decodeutf8(data: bytes) -> str:
            return data.decode("utf-8")
        return self.get(key, fn=decodeutf8)

    def get_int(self, key=int) -> int:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            int: The retrieved data as an integer,
            or None if the key doesn't exist.
        """
        return self.get(key, fn=int)
