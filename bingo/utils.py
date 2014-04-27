#!/usr/bin/python
# -*- encoding: utf-8 -*-
from random import sample


class Bingo(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Bingo, cls).__new__(cls, *args, **kwargs)
            setattr(cls._instance, 'numbers', map(lambda each_number: str(each_number).zfill(2), range(1, 61)))
            setattr(cls._instance, 'numbers_sorted', [])
        return cls._instance

    def get_instance(self):
        return self._instance

    def sort_numbers(self):
        if self._instance.numbers:
            value = sample(self._instance.numbers, 1)[0]

            self._instance.numbers_sorted.append(value)
            self._instance.numbers.remove(value)
        else:
            value = 0
        return value
