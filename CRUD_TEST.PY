import unittest

from CRUD.py import read

class TestCR(unittest.TestCase):
    #READ
    def test_read(self):
        data = {"animal_id" : "Lucy"}
        match = {"age_upon_outcome" : "5 years",
                "animal_id" : "A696004",
                "animal_type" : "Dog",
                "breed" : "Cardigan Welsh Corgi Mix",
                "color" : "Sable/White",
                "date_of_birth" : "Jan 27,2010",
                "datetime" : Date(),
                "name" : "",
                "outcome_subtype" : "",
                "outcome_type" : "",
                "sex_upon_outcome" : "Spayed Female",
                 "age_upon_outcome_in_weeks" : "261 weeks"
                 }
        result = read(data)
        self.assertEqual(result, match)

if __name__ == '__main__':
    unittest.main()
