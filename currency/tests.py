from django.test import SimpleTestCase

# Create your tests here.
class TestCase(SimpleTestCase):
    def test_first(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
