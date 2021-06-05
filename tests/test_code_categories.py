import unittest
from gideon_api_python.codes.categories import get_category

class TestCategoryCheck(unittest.TestCase):
    def test_diseases(self):
        self.assertEqual(get_category('diseases'), '/diseases')

    def test_drugs(self):
        self.assertEqual(get_category('drugs'), '/drugs')

    def test_vaccines(self):
        self.assertEqual(get_category('vaccines'), '/vaccines')

    def test_bacteria(self):
        self.assertEqual(get_category('bacteria'), '/microbiology/bacteria')

    def test_mycobacteria(self):
        self.assertEqual(get_category('mycobacteria'), '/microbiology/mycobacteria')

    def test_yeasts(self):
        self.assertEqual(get_category('yeasts'), '/microbiology/yeasts')

    def test_regions(self):
        self.assertEqual(get_category('regions'), '/travel/regions')

    def test_countries(self):
        self.assertEqual(get_category('countries'), '/countries')

    def test_capitalization(self):
        self.assertEqual(get_category('BACTERIA'), '/microbiology/bacteria')
        self.assertEqual(get_category('Regions'), '/travel/regions')
        self.assertEqual(get_category('yeasTs'), '/microbiology/yeasts')
        self.assertEqual(get_category('vACCINES'), '/vaccines')

    def test_whitespace(self):
        self.assertEqual(get_category('countries '), '/countries')
        self.assertEqual(get_category(' vaccines'), '/vaccines')
        self.assertEqual(get_category(' drugs '), '/drugs')
        self.assertEqual(get_category('\tdiseases\n'), '/diseases')

    def test_variations(self):
        self.assertEqual(get_category('disease'), '/diseases')
        self.assertEqual(get_category('region'), '/travel/regions')
        self.assertEqual(get_category('country'), '/countries')
        self.assertEqual(get_category('bacterium'), '/microbiology/bacteria')
        self.assertEqual(get_category('yeast'), '/microbiology/yeasts')

