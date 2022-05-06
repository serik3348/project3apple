from django.test import TestCase

# Create your tests here.
from .models import *


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods")
        pass

    def setUp(self):
        print("setUp:Run once for every test method to set up clean data")
        pass



    def test_letter(self):
        print("Method : test_letter")

        self.assertTrue('SERIK'.isupper())


    def test_compare_num(self):
        post=POST()
        self.assertEqual(post.get_number(),8)


    def test_values(self):
        post=POST()
        self.assertIn(post.get_let1(),post.get_let2())
