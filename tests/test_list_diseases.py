import unittest
import gideon_api_python.diseases.list_diseases as list_diseases

class TestGetDiseaseCode(unittest.TestCase):
    def test_covid19(self):
        self.assertEqual(
            list_diseases.get_disease_code_from_name('COVID-19'),
            12683
        )
    
    def test_ebola(self):
        self.assertEqual(
            list_diseases.get_disease_code_from_name('Ebola'),
            10700
        )