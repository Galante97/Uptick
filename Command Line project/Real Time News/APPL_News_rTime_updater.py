#updates APPL_news_rTime sheet

#GENERAL IMPORTS #
import time
import datetime as dt

import pandas as pd

import numpy as np
import datetime as dt
from copy import copy

import google_sheets_api as sheet

#import news module
import yahoo as news

def update_APPL_news_rTime():
    newsArticles = news.get_company_news("AAPL")
    
    for i in range(len(newsArticles)):
        time.sleep(0.21)
        print("adding row to APPL_news_rTime...")
        try:
            sheet.AAPL_news_rTime.append_row([str(dt.datetime.now()), str(dt.datetime.now().time()), str(dt.datetime.now().date()), newsArticles[i]['title'], newsArticles[i]['summary'],newsArticles[i]['content'], newsArticles[i]['link']])
        except:
            print("error adding news article")
