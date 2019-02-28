from django.urls import reverse
from django.test import TestCase

class GedcomTestTests(TestCase):
    def test_gedcom_test_status_code(self):
        url = reverse('gedcom_test_page')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)