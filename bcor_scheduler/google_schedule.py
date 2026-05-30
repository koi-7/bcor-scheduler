# coding: utf-8


import os
import time

from .consts import *


class GoogleSchedule:
    def __init__(self, calendar_id, title, color_id, start_datetime, end_datetime):
        self.__calendar_id = calendar_id
        self.__title = title
        self.__color_id = color_id
        self.__start_datetime = start_datetime
        self.__end_datetime = end_datetime

    def register(self, service):
        body = {
            'summary': self.__title,
            'start': {
                'dateTime': self.__start_datetime,
                'timeZone': 'Japan',
            },
            'end': {
                'dateTime': self.__end_datetime,
                'timeZone': 'Japan',
            },
            'colorId': self.__color_id,
        }

        service.events().insert(calendarId=self.__calendar_id, body=body).execute()

        time.sleep(1)
