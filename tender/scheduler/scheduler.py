import contextlib
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.core.management import call_command

def db_backup():
    with contextlib.suppress(Exception):
        call_command('dbbackup')
        print('db created! - ')

def start():
    scheduler=BackgroundScheduler()
    # scheduler.add_jobstore(DjangoJobStore(),'default')

    # scheduler.add_job(db_backup, 'interval', minutes=2, jobstore='default', id='weekly_backup', replace_existing=True)
    scheduler.add_job(db_backup, 'interval', minutes=1440, timezone= 'Asia/Yekaterinburg')
    # register_events(scheduler)
    scheduler.start()



