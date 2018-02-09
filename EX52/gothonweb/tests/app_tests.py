from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client()
client.testing = True

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=302)

    resp = client.get('/game')
    assert_response(resp)

    resp= client.post('/game')
    assrt_reponse(resp, contains="You Died!")

    # Go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to another scene
    testdata = {'userinput': '123'}
    resp = client.post(/'game', data=testdata)
    assrt_response(resp, contains="The Bridge")
