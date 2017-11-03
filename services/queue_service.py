"""
Created by anthony on 26.10.17
queue_service
"""
from telegram.ext import JobQueue, Job
from

class BotJobQueue:
    def __init__(self, bot):
        # TODO make queue singleton
        self.job_queue = JobQueue(bot)
        print('Job queue has been set up')

    def add_job(self, callback, when):
        if not self.job_queue:
            raise ValueError('Job queue does not exist')

        job = Job(callback=callback, repeat=False)
        self.job_queue.run_once(job, when)

        print('Current jobs: ' + str(self.job_queue.jobs()))

    def add_to_q(self, msg):
        queue.add(msg)


class CallbackJob:
    def __init__(self, message, name):
        self.message = message
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        print('calling' + self.message)
