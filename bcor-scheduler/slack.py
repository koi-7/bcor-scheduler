# coding: utf-8


import requests

from .consts import *


class Slack:
    def __init__(self, channel_id, token):
        self.__channel_id = channel_id
        self.__token = token

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def token(self):
        return self.__token

    def notify(self, number_of_schedules):
        text = Consts.TEXT_NOTIFY.format(number_of_schedules)

        api_url = 'https://slack.com/api/chat.postMessage'
        headers = {'Authorization': f'Bearer {self.token}'}
        data = {'channel': self.channel_id, 'text': text}
        requests.post(api_url, headers=headers, data=data)
