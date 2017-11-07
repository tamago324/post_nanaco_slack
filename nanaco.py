#!/usr/bin/env python

class Nanaco():

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
