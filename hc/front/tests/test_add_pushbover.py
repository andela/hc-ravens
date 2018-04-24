from django.test.utils import override_settings
from hc.api.models import Channel
from hc.test import BaseTestCase
from django.utils.http import urlencode


@override_settings(PUSHOVER_API_TOKEN="token", PUSHOVER_SUBSCRIPTION_URL="url")
class AddPushoverTestCase(BaseTestCase):
    def test_it_adds_channel(self):
        self.client.login(username="alice@example.org", password="password")

        session = self.client.session
        session["po_nonce"] = "n"
        session.save()

        params = "pushover_user_key=a&nonce=n&prio=0"
        r = self.client.get("/integrations/add_pushover/?%s" % params)
        assert r.status_code == 302

        channels = list(Channel.objects.all())
        assert len(channels) == 1
        assert channels[0].value == "a|0"

    @override_settings(PUSHOVER_API_TOKEN=None)
    def test_it_requires_api_token(self):
        self.client.login(username="alice@example.org", password="password")
        r = self.client.get("/integrations/add_pushover/")
        self.assertEqual(r.status_code, 404)

    def test_it_validates_nonce(self):
        self.client.login(username="alice@example.org", password="password")

        session = self.client.session
        session["po_nonce"] = "n"
        session.save()

        params = "pushover_user_key=a&nonce=INVALID&prio=0"
        r = self.client.get("/integrations/add_pushover/?%s" % params)
        assert r.status_code == 403

    def test_pushover_validates_priority(self):
        self.client.login(username="alice@example.org", password="password")

        po_nonce = "randomString"
        # store test po_nonce in session for access in views
        session = self.client.session
        session["po_nonce"] = po_nonce
        session.save()
        # simulate request
        query_params = {
            "pushover_user_key": "key",
            "nonce": po_nonce,
            "prio": "INVALID" # valid values for prio ('-2', '-1', '0', '1', '2')
        }
        url = "/integrations/add_pushover/?%s" %urlencode(query_params)
        resp = self.client.get(url)
        # client gets a 400 Bad Request Response, prio invalid
        self.assertEqual(resp.status_code, 400)
