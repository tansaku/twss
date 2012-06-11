from django.http import HttpResponse
import twss
import pickle
import json
from svmutil import *

# import the logging library
import logging
logging.basicConfig()

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
  input = open('data/vocab.pk')
  vocabList = pickle.load(input)
  input.close()
  model = svm_load_model("data/svm_model.pk")
  #logger.error(request.GET['say'])
  #logger.error(model)
  callback = request.GET.get('callback', '')
  req = {}
  req ['reply'] = twss.twss(request.GET['say'],vocabList,model)
  response = json.dumps(req)
  response = callback + '(' + response + ');'
  return HttpResponse(response, mimetype="application/json")