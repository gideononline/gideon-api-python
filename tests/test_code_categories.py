import unittest
from gideon_api_python.codes.categories import check_category

class TestCategoryCheck(unittest.TestCase):
    def test_diseases(self):
        self.assertEqual(check_category('diseases'), '/diseases')

    def test_drugs(self):
        self.assertEqual(check_category('drugs'), '/drugs')

    def test_vaccines(self):
        self.assertEqual(check_category('vaccines'), '/vaccines')

    def test_bacteria(self):
        self.assertEqual(check_category('bacteria'), '/microbiology/bacteria')

    def test_mycobacteria(self):
        self.assertEqual(check_category('mycobacteria'), '/microbiology/mycobacteria')

    def test_yeasts(self):
        self.assertEqual(check_category('yeasts'), '/microbiology/yeasts')

    def test_regions(self):
        self.assertEqual(check_category('regions'), '/travel/regions')

    def test_countries(self):
        self.assertEqual(check_category('countries'), '/countries')

    def test_capitalization(self):
        self.assertEqual(check_category('BACTERIA'), '/microbiology/bacteria')
        self.assertEqual(check_category('Regions'), '/travel/regions')
        self.assertEqual(check_category('yeasTs'), '/microbiology/yeasts')
        self.assertEqual(check_category('vACCINES'), '/vaccines')

    def test_whitespace(self):
        self.assertEqual(check_category('countries '), '/countries')
        self.assertEqual(check_category(' vaccines'), '/vaccines')
        self.assertEqual(check_category(' drugs '), '/drugs')
        self.assertEqual(check_category('\tdiseases\n'), '/diseases')