from django.http import HttpResponse
from rq import Queue
from dj_scheduling_queuing_test.worker import conn
from dj_scheduling_queuing_test.utils import count_words_at_url


def root(request):
    """
    """

    q = Queue(connection=conn)
    result = q.enqueue(count_words_at_url, 'http://heroku.com')

    return HttpResponse()
