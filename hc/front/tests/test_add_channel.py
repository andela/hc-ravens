from django.test.utils import override_settings

from hc.api.models import Channel
from hc.test import BaseTestCase


@override_settings(PUSHOVER_API_TOKEN="token", PUSHOVER_SUBSCRIPTION_URL="url")
class AddChannelTestCase(BaseTestCase):

    def test_it_adds_email(self):
        url = "/integrations/add/"
        form = {"kind": "email", "value": "alice@example.org"}

        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url, form)

        self.assertRedirects(r, "/integrations/")
        assert Channel.objects.count() == 1

    def test_it_trims_whitespace(self):
        """ Leading and trailing whitespace should get trimmed. """

        url = "/integrations/add/"
        form = {"kind": "email", "value": "   alice@example.org   "}

        self.client.login(username="alice@example.org", password="password")
        self.client.post(url, form)

        q = Channel.objects.filter(value="alice@example.org")
        self.assertEqual(q.count(), 1)

    def test_instructions_work(self):
        self.client.login(username="alice@example.org", password="password")
        kinds = ("email", "webhook", "pd", "pushover", "hipchat", "victorops")
        for frag in kinds:
            url = "/integrations/add_%s/" % frag
            r = self.client.get(url)
            self.assertContains(r, "Integration Settings", status_code=200)

    ### Test that the team access works
    def test_that_team_access_works(self):
        url = "/integrations/add_email/"
        form = {"kind": "email", "value": "alice@example.org"}

        self.client.login(username="alices@example.org", password="password")
        self.client.post(url, form)
        self.client.logout()

        url2 = '/integrations/'
        self.client.login(username="bob@example.org", password="password")
        r = self.client.get(url2)
        html_text = r.content.decode('utf-8')
        self.assertIn('alice@example.org', html_text)

    ### Test that bad kinds don't work
    def test_bad_kinds_dont_work (self):
        url = "/integrations/add/"
        form = {"kind": "tumbr", "value": "alicetumbr"}

        self.client.login(username="alice@example.org", password="password")
        self.client.post(url, form)
        q = Channel.objects.filter(value='tumbr')
        self.assertEqual(q.count(), 0)
