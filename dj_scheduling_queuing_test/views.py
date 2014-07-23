from django.http import HttpResponse
from rq import Queue
from worker import conn
from utils import count_words_at_url


def root(request):
    """
    """

    q = Queue(connection=conn)
    result = q.enqueue(count_words_at_url, 'http://heroku.com')

    return HttpResponse()
