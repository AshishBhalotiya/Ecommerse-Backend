from django.shortcuts import render
import logging
import requests

logger = logging.getLogger(__name__) #playground.views


def say_hello(request):
    try:
        logger.info('Calling httpbin')
        response = request.get('https://httpbin.org/delay/2')
        logger.info('Received the response')
        data = response.json()
    except requests.ConnectionError:
        logger.critical('httpbin is offline')
    return render(request, 'hello.html', {'name': 'Mosh'})
