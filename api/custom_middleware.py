from django.db import connection
from django.template import Template, Context
from celery_demo.settings import LOG


class SQLLogMiddleware:

    def process_response(self, request, response):
        time = 0.0
        for q in connection.queries:
            time += float(q['time'])
            LOG.info(q)
        LOG.info({'count':len(connection.queries),'time': time})
        return response