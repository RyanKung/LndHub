import requests
import base

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
