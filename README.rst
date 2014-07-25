Django Scheduling Queuing Review
================================

This is a review of various scheduling & queuing technologies for use with Django.

Background Tasks in Python with RQ
----------------------------------

This is a nice writeup & simple, straightforward approach to queuing with RQ (Redis Queue): https://devcenter.heroku.com/articles/python-rq. An implementation can be found in this repository (deployed here: http://dj-scheduling-queuing-test.herokuapp.com/), in which a page load queues a task.

Heroku logs sample
~~~~~~~~~~~~~~~~~~

::

    2014-07-25T03:10:17.818102+00:00 heroku[router]: at=info method=GET path="/" host=dj-scheduling-queuing-test.herokuapp.com request_id=1870e214-fc28-443c-b2c7-592f8ab92d87 fwd="108.48.33.128" dyno=web.1 connect=0 service=12 status=200 bytes=580
    2014-07-25T03:10:17.817720+00:00 app[worker.1]: 03:10:17 default: dj_scheduling_queuing_test.utils.count_words_at_url('http://heroku.com') (3fdf4d3c-6079-4fb6-a0a2-c19140a96574)
    2014-07-25T03:10:17.950457+00:00 app[worker.1]: 03:10:17 Starting new HTTPS connection (1): heroku.com
    2014-07-25T03:10:18.033652+00:00 app[worker.1]: 03:10:18 Job OK, result = 721
    2014-07-25T03:10:18.042495+00:00 app[worker.1]: 03:10:18 
    2014-07-25T03:10:17.817804+00:00 app[web.1]: [24/Jul/2014 22:10:17] "GET / HTTP/1.1" 200 0
    2014-07-25T03:10:17.940225+00:00 app[worker.1]: 03:10:17 Starting new HTTP connection (1): heroku.com
    2014-07-25T03:10:17.974730+00:00 app[worker.1]: 03:10:17 Starting new HTTPS connection (1): www.heroku.com
    2014-07-25T03:10:18.033821+00:00 app[worker.1]: 03:10:18 Result is kept for 500 seconds.
    2014-07-25T03:10:18.042639+00:00 app[worker.1]: 03:10:18 *** Listening on high, default, low...
