import unittest
from data_classes import Person
from parameterized import parameterized #type: ignore



class MainTest(unittest.TestCase):
    
    @parameterized.expand([
        ("Peter Edward", "Software Engineer", 33, "Peter Edward"),
        ("Melody Otuka", "Software Engineer", 33, "Melody Otuka")
    ])
    def test_constructor_asigns_value(self, name: str, job: str, age: int, result: str) -> None:
        person = Person(name, job, age)
        self.assertEqual(person.name, result)
        
    def test_person1_gt_person2(self) -> None:
        person1 = Person("Peter Edward", "Software Engineer", 35)
        person2 = Person("Peter Edward", "Software Engineer", 34)
        condition = person1 < person2
        self.assertEqual(condition, False)
        
        

if __name__ == "__main__":
    pass