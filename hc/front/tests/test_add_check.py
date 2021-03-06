from hc.api.models import Check
from hc.test import BaseTestCase


class AddCheckTestCase(BaseTestCase):

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")
        assert Check.objects.count() == 1

    ### Test that team access works
    def test_that_team_access_works(self):
        url = "/checks/add/"

        self.client.login(username="alices@example.org", password="password")
        self.client.post(url)
        self.client.logout()

        url = '/checks/'
        self.client.login(username="bob@example.org", password="password")
        r = self.client.get(url)
        self.assertContains(r, 'alice@example.org', status_code=200)
