import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    
    def test_err_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1),"err")
    
    def test_nobirth_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0),50)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    def test_teenage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13),100)
    
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21),150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70),100)
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()
