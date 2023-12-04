#!/usr/bin/env python3
# coding: utf-8


import datetime
import time

from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import configparser
import requests

from google.oauth2 import service_account
from googleapiclient.discovery import build

from .consts import *
from .google_schedule import *
from .slack import *


def main():
    next_month_datetime = datetime.datetime.today() + relativedelta(months=1)

    url = f'{Consts.BCOR_URL}/schedule/?scheduleYear={next_month_datetime.year}&scheduleMonth={next_month_datetime.month}'

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            break
        except:
            time.sleep(1)

    soup = BeautifulSoup(response.content, 'html.parser')
    schedule_details = soup.find_all(class_='schedule-detail')

    config_ini = configparser.ConfigParser()
    config_ini.read(Consts.PATH_CONFIG, encoding='utf-8')

    calendar_id = config_ini['Google']['calendar_id']

    schedules = []
    for schedule_detail in schedule_details:
        game_date = schedule_detail.find(class_='day').get_text().strip()
        month, day = [int(item) for item in game_date.split('.')]

        game_time = schedule_detail.find(class_='start-time').get_text().strip()
        hour, minute = [int(item) for item in game_time.split(':')]

        game_start_datetime = datetime.datetime(next_month_datetime.year, month, day, hour, minute)
        game_end_datetime = game_start_datetime + datetime.timedelta(hours=2)

        schedule_start_datetime = game_start_datetime.isoformat(timespec='seconds')
        schedule_end_datetime = game_end_datetime.isoformat(timespec='seconds')

        schedules.append(GoogleSchedule(calendar_id, Consts.TITLE, Consts.COLOR_ID, schedule_start_datetime, schedule_end_datetime))

    creds = service_account.Credentials.from_service_account_file(Consts.PATH_CREDENTIALS, scopes=Consts.SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    for schedule in schedules:
        schedule.register(service)

    slack = Slack(config_ini['Slack']['channel_id'], config_ini['Slack']['token'])
    slack.notify(len(schedules))


if __name__ == '__main__':
    main()
