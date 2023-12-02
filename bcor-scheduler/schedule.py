# coding: utf-8


from .consts import *


class Schedule:
    def __init__(self, start_datetime, end_datetime):
        self.__title = Consts.TITLE
        self.__start_datetime = start_datetime
        self.__end_datetime = end_datetime
        self.__color_id = Consts.COLOR_ID

    @property
    def title(self):
        return self.__title

    @property
    def start_datetime(self):
        return self.__start_datetime

    @property
    def end_datetime(self):
        return self.__end_datetime

    @property
    def color_id(self):
        return self.__color_id
