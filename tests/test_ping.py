import requests
import base
from hashlib import sha256
from klefki.bitcoin import gen_key_pair, sign
from klefki.bitcoin.sign import sign

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


    def test_firefly_create_user(self):
        priv, pub = gen_key_pair()
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

        data = "Hello World"
        resp = requests.post(
            "%s/%s" % (self.host, "verify_auth"),
            headers=dict(
                authorization="Pubkey%s" % pub,
                sig=sign(priv, sha256(data.encode()).hexdigest())
            ),
            data=data
        )
        assert resp.json()['error'] != True
