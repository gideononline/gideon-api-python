import unittest
from gideon_api import lookup_item


class TestLookupItemExact(unittest.TestCase):

    def test_lookup_diseases(self):
        disease_and_id = (
            ('Anthrax', 10100),
            ('Cholera', 10390),
            ('Meningitis - aseptic (viral)', 10130),
            ('St. Louis encephalitis', 12250),
            ('Pyodermas (impetigo, abscess, etc)', 11915),
            ('Zika', 12680),
        )
        for disease, id_ in disease_and_id:
            self.assertEqual(lookup_item('diseases', disease), id_)

    def test_lookup_drugs(self):
        drug_and_id = (
            ('Ampicillin / Sulbactam', 20520),
            ('Cefsulodin', 20742),
            ('Interferon alfacon-1', 21259),
            ('Ombitasvir-Paritaprevir-Ritonavir', 20895),
            ('Ritonavir (alone or with lopinavir)', 21245),
            ('Sofosbuvir / Velpatasvir', 21219),
        )
        for drug, id_ in drug_and_id:
            self.assertEqual(lookup_item('drugs', drug), id_)

    def test_lookup_vaccines(self):
        vaccine_and_id = (
            ('COVID-19 vaccine - recombinant nanoparticle', 30400),
            ('H. influenzae (HbOC-DTP or -DTaP) vaccine', 30124),
            ('Varicella-Zoster immune globulin', 30380),
        )
        for vaccine, id_ in vaccine_and_id:
            self.assertEqual(lookup_item('vaccines', vaccine), id_)

    def test_lookup_bacteria(self):
        bacterium_and_id = (
            ('Acidipropionibacterium timonense', 74),
            ('Capnocytophaga genomospecies AHN8471', 1015),
            ('Lactococcus lactis ssp lactis', 2960),
            ('OFBA-1', 3555),
            ('Rodentibacter pneumotropicus', 3640),
            ('Staphylococcus aureus', 4700),
        )
        for bacteria, id_ in bacterium_and_id:
            self.assertEqual(lookup_item('bacteria', bacteria), id_)

    def test_lookup_mycobacteria(self):
        mycobacterium_and_id = (
            ('Mycobacterium aubagnense', 8035),
            ('Mycobacterium heckeshornense', 8181),
            ('Mycolicibacter kumamotonensis', 8203),
        )
        for mycobacteria, id_ in mycobacterium_and_id:
            self.assertEqual(lookup_item('mycobacteria', mycobacteria), id_)

    def test_lookup_yeasts(self):
        yeast_and_id = (
            ('Candida duoubshaemulonii', 7077),
            ('Cutaneotrichosporon mucoides', 7412),
            ('Trichosporon mycotoxinivorans', 7447),
        )
        for yeast, id_ in yeast_and_id:
            self.assertEqual(lookup_item('yeasts', yeast), id_)

    def test_lookup_regions(self):
        region_and_id = (
            ('Australia and the South Pacific', 9),
            ('Eastern Europe and Northern Asia', 11),
            ('North America', 15),
        )
        for region, id_ in region_and_id:
            self.assertEqual(lookup_item('regions', region), id_)

    def test_lookup_countries(self):
        country_and_id = (
            ('China', 'G140'),
            ('Netherlands', 'G226'),
            ('United Kingdom', 'G291'),
        )
        for country, id_ in country_and_id:
            self.assertEqual(lookup_item('countries', country), id_)
