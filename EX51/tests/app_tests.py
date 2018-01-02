from nose.tools import *
from app6 import app
from tests.tools import assert_response

client = app.test_client()
client.testing = True

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=404)

    resp = client('/hello')
    assert_response(resp)

    resp = client.post('/hello')
    assert_response(resp, contains="Nobody")

    testdata = {'name': 'Hanna', 'greet': 'Hola'}
    resp = client.post('/hello', data=testdata)
    assert_reponse(resp, contains="Hanna")
