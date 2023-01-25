from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
sched = BlockingScheduler(timezone='Asia/Taipei')


def my_job(text):
    print(text)


# 在2022年12月3日執行
sched.add_job(my_job, 'date', run_date=datetime(
    2022, 12, 3, 12, 0, 1))

sched.start()
