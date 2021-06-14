import unittest
from gideon_api import get_endpoint


class TestCategoryCheck(unittest.TestCase):

    def test_diseases(self):
        self.assertEqual(get_endpoint('diseases'), '/diseases')

    def test_drugs(self):
        self.assertEqual(get_endpoint('drugs'), '/drugs')

    def test_vaccines(self):
        self.assertEqual(get_endpoint('vaccines'), '/vaccines')

    def test_bacteria(self):
        self.assertEqual(get_endpoint('bacteria'), '/microbiology/bacteria')

    def test_mycobacteria(self):
        self.assertEqual(get_endpoint('mycobacteria'),
                         '/microbiology/mycobacteria')

    def test_yeasts(self):
        self.assertEqual(get_endpoint('yeasts'), '/microbiology/yeasts')

    def test_regions(self):
        self.assertEqual(get_endpoint('regions'), '/travel/regions')

    def test_countries(self):
        self.assertEqual(get_endpoint('countries'), '/countries')

    def test_capitalization(self):
        self.assertEqual(get_endpoint('BACTERIA'), '/microbiology/bacteria')
        self.assertEqual(get_endpoint('Regions'), '/travel/regions')
        self.assertEqual(get_endpoint('yeasTs'), '/microbiology/yeasts')
        self.assertEqual(get_endpoint('vACCINES'), '/vaccines')

    def test_whitespace(self):
        self.assertEqual(get_endpoint('countries '), '/countries')
        self.assertEqual(get_endpoint(' vaccines'), '/vaccines')
        self.assertEqual(get_endpoint(' drugs '), '/drugs')
        self.assertEqual(get_endpoint('\tdiseases\n'), '/diseases')

    def test_variations(self):
        self.assertEqual(get_endpoint('disease'), '/diseases')
        self.assertEqual(get_endpoint('region'), '/travel/regions')
        self.assertEqual(get_endpoint('country'), '/countries')
        self.assertEqual(get_endpoint('bacterium'), '/microbiology/bacteria')
        self.assertEqual(get_endpoint('yeast'), '/microbiology/yeasts')
