#!/usr/bin/env python3
"""
implements Cache class
"""
import redis
import random
import uuid
import typing


class Cache:
    """
    Cache class.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
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
