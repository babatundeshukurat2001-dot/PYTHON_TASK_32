#import unittest
#class TestContactApp(unittest.TestCase):
#(self) is not a keyword it is convention in python

from unittest import TestCase

#import contact_app_function

from contact_app_function import create_contact, clear_contacts

class TestContactApp(TestCase):

#    def test_sample(self):
#
#        self.assertEqual(90, 90)
#        self.assertTrue(True)
#        self.assertFalse(False)
#    
    def test_that_newContact_canBeCreated_andSave(self):

        clear_contacts()

        first_name = "Rasaq"
        last_name = "Abiodun"

        phone_number = "07023425964"

        contact = create_contact(first_name, last_name, phone_number)

        self.assertEqual(type(contact), list)
        self.assertEqual(len(contact) , 3)

        self.assertEqual("07023425964", contact[-1])
 

    def test_that_Dulicate_contacts_cannot_be_create(self):

        clear_contacts()

        first_name = "ope"
        last_name = "ola"

        phone_number = "07023425964"

        contact = create_contact(first_name, last_name, phone_number)

        first_name = "tosin"
        last_name = "bimbo"

        phone_number = "07023425964"

        contact = create_contact(first_name, last_name, phone_number)

#        self.assertEqual(contact, None)

        self.assertIsNone(contact)


    

        
