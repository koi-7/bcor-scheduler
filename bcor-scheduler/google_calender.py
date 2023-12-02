# coding: utf-8


import os
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from .consts import *


class GoogleCalendar:
    def __init__(self):
        self.__creds = None

    @property
    def creds(self):
        return self.__creds

    @creds.setter
    def creds(self, value):
        self.__creds = value

    def create_creds(self):
        if os.path.exists(Consts.PATH_TOKEN):
            self.creds = Credentials.from_authorized_user_file(Consts.PATH_TOKEN, Consts.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    Consts.PATH_CREDENTIALS, Consts.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(Consts.PATH_TOKEN, 'w') as token:
                token.write(self.creds.to_json())

    def register(self, service, schedule):
        start_datetime = schedule.start_datetime.isoformat(timespec='seconds')
        end_datetime = schedule.end_datetime.isoformat(timespec='seconds')

        body = {
            'summary': schedule.title,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'Japan',
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'Japan',
            },
            'colorId': Consts.COLOR_ID,
        }

        service.events().insert(calendarId='primary', body=body).execute()

        time.sleep(1)
