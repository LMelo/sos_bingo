#!/usr/bin/python
# -*- encoding: utf-8 -*-
from random import sample

from django.shortcuts import render
from bingo.utils import Bingo


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def bingo(request, *args, **kwargs):
    bingo_numbers = Bingo()
    bingo_instance = bingo_numbers.get_instance()
    if request.method == 'POST':
        value = bingo_numbers.sort_numbers()
        values_sorted = bingo_instance.numbers_sorted
    else:
        if bingo_instance.numbers_sorted:
            value = bingo_instance.numbers_sorted[bingo_instance.numbers_sorted.__len__() - 1]
            values_sorted = bingo_instance.numbers_sorted
        else:
            value = 0
            values_sorted = []

    return render(request, 'bingo.html', {'value': value, 'numbers_sorted': values_sorted})


def cards(request, *args, **kwargs):
    numbers = range(1, 61)
    sorted_numbers = sample(numbers, 25)

    return render(request,'cards.html', {'numbers': sorted_numbers})