from datetime import datetime
import logging
import os
import sqlite3 as sq

def onStart() -> None:
    now: datetime = datetime.now()
    logging.basicConfig(level=logging.INFO, filename=os.path.join('logs', f"{now:%y.%m.%d.%H.%m}.log"), filemode="w", encoding='utf-8')
    logging.info('Start Logging..')
    logging.info('Starting Bot...')

def sqlStart() -> None:
    try:
        logging_base = sq.connect('logs/db/logging.db')
        logging.info('LOGGING DATABASE CONNECTION STATE: -SUCCESS-')
        script = open(os.path.join('db', 'loggingScript.sql')).read()
        logging_base.executescript(script)
        logging_base.commit()
    except sq.Error as e:
        logging.info('LOGGING DATABASE CONNECTION STATE: -ERROR-')
        logging.error(e)
    try:
        base = sq.connect('reqsFolder/reqs.db')
        logging.info('REQUEST DATABASE CONNECTION STATE: -SUCCESS-')
        script = open(os.path.join('db', 'reqScript.sql')).read()
        base.executescript(script)
        base.commit()
    except sq.Error as e:
        logging.info('REQUEST DATABASE CONNECTION STATE: -ERROR-')
        logging.error(e)
    try:
        quest = sq.connect('extra/questions.db')
        logging.info('QUESTIONS DATABASE CONNECTION STATE: -SUCCESS-')
        script = open(os.path.join('db', 'questions.sql')).read()
        quest.executescript(script)
        quest.commit()
    except sq.Error as e:
        logging.info("QUESTIONS DATABASE CONNECTION STATE: -ERROR-")
        logging.error(e)