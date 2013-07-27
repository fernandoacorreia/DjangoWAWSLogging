from time import gmtime, strftime
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    logger.info('home ' + current_time)
    return HttpResponse("Hello from Django! It is now " + current_time + ".\n")
