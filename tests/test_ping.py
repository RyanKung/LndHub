import requests
import base

class TestPing(base.BaseTest):
    def test_ping(self):
        assert requests.get(self.host).status_code == 200
