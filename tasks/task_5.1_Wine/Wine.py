#!/usr/bin/env python3
import datetime


class Wine(object):
    """
    Class describing Wine for storing in database

    :ivar str name: Wine title
    :ivar str brand: trademark
    :ivar str country: produced in country
    :ivar date: bottling date
    :type date: datetime.datetime
    :ivar str comment: note
    """
    def __init__(self, name: str, brand: str, country: str, date: datetime.datetime, comment: str):
        if not type(date) == datetime.datetime:
            raise TypeError(f'date must be datetime.datetime, not {type(date)}')
        self.name = name
        self.brand = brand
        self.country = country
        self.date = date
        self.comment = comment
    
    def oldness(self, day=None):
        """
        returns Wine age

        :param day: current date
        :type day: datetime.datetime
        :rtype: datetime.timedelta
        """
        if not day:
            day = datetime.datetime.now()
        return day - self.date

