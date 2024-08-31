#!/usr/bin/env python3
"""
implements Cache class with decorators.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator that counts how many times a method is called. """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_list_key = f"{method.__qualname__}:inputs"
        output_list_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(output))
        return output
    return wrapper


class Cache:
    """ Cache class. """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random uuid4 str and use it as a key
        to store the input data in Redis.
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
        Retrieves a string value from the Redis cache.

        This method uses the Cache.get method with a UTF-8 decode function.
        It's designed to work with keys that were stored as strings.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Optional[str]: The retrieved data as a string,
            or None if the key doesn't exist.
        """
        def decodeutf8(value: bytes) -> str:
            return value.decode("utf-8")
        return self.get(key, fn=decodeutf8)

    def get_int(self, key=int) -> int:
        """
        Retrieves an integer value from the Redis cache.
        This method uses the Cache.get method with int
        as the conversion function.
        It's designed to work with keys that were stored as integers.

        Args:
            key (str): The key to retrieve the value for.
        Returns:
            Optional[int]: The retrieved data as an integer,
            or None if the key doesn't exist.
        """
        return self.get(key, fn=int)
