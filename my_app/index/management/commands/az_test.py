from django.core.management.base import BaseCommand
import unittest

class Command(BaseCommand):
    help = """
    If you need Arguments, please check other modules in
    django/core/management/commands.
    """

    def handle(self, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestChronology)
        unittest.TextTestRunner().run(suite)

class TestChronology(unittest.TestCase):
    def setUp(self):
        print("Write your pre-test prerequisites here")

    def test_equality(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 3)