# coding: utf-8


import os


class Consts:
    PATH_MAIN_DIR = os.path.dirname(__file__)
    PATH_CONFIG = os.path.join(PATH_MAIN_DIR, '../config/config.ini')
    PATH_TOKEN = os.path.join(PATH_MAIN_DIR, '../data/token.json')
    PATH_CREDENTIALS = os.path.join(PATH_MAIN_DIR, '../data/credentials.json')
    PATH_LOG = os.path.join(PATH_MAIN_DIR, '../logs/bcor-scheduler.log')

    BCOR_URL = 'https://b-corsairs.com'

    # If modifying these scopes, delete the file token.json.
    # SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    TITLE = 'Bリーグ'
    COLOR_ID = '4'

    TEXT_NOTIFY = '来月の試合を {} 件登録しました。'
