#!/usr/bin/env python3
# coding: utf-8


import datetime
import time

from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import configparser
import requests
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .consts import *
from .google_calender import *
from .schedule import *
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

    schedules = []
    for schedule_detail in schedule_details:
        game_date = schedule_detail.find(class_='day').get_text().strip()
        month, day = [int(item) for item in game_date.split('.')]

        game_time = schedule_detail.find(class_='start-time').get_text().strip()
        hour, minute = [int(item) for item in game_time.split(':')]

        game_start_datetime = datetime.datetime(next_month_datetime.year, month, day, hour, minute)
        game_end_datetime = game_start_datetime + datetime.timedelta(hours=2)

        schedules.append(Schedule(game_start_datetime, game_end_datetime))

    google_calendar = GoogleCalendar()
    google_calendar.create_creds()

    try:
        service = build('calendar', 'v3', credentials=google_calendar.creds)
        for schedule in schedules:
            google_calendar.register(service, schedule)
    except HttpError as error:
        print(f"An error occurred: {error}")
        sys.exit(1)

    config_ini = configparser.ConfigParser()
    config_ini.read(Consts.PATH_CONFIG, encoding='utf-8')

    slack = Slack(config_ini['Slack']['channel_id'], config_ini['Slack']['token'])
    slack.notify(len(schedules))


if __name__ == '__main__':
    main()
