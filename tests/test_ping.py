import requests
import base
from hashlib import sha256
from klefki.bitcoin import gen_key_pair

class BasicTest(base.BaseTest):
    def test_ping(self):
        assert requests.get(self.host).status_code == 200


    def test_bluewallet_create_user(self):
        resp = requests.post(
            "%s/%s" % (self.host, "create"),
            data=dict(
                partnerid="bluewallet",
                accounttype="bluewallet"
            )
        )
        assert resp.status_code == 200
        assert resp.json()['password']
        assert resp.json()['login']
        token = requests.post(
            "%s/%s" % (self.host, "auth"),
            resp.json()
        )
        assert token
        resp = requests.post(
            "%s/%s" % (self.host, "verify_auth"),
            headers=dict(authorization=token)
        )
        assert resp.text == "ok"





    def test_firefly_create_user(self):
        pub, priv = gen_key_pair()
        resp = requests.post(
            "%s/%s" % (self.host, "create"),
            data=dict(
                partnerid="bluewallet",
                accounttype="bluewallet",
                pubkey=pub
            )
        )
        assert resp.status_code == 200
        assert resp.json()['result'] == "ok"
