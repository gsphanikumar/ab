import unittest
from AddressBook import AddressBook,Group

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.ab = AddressBook();

    def test_add_group(self):
        self.ab.add_group("test2")
        self.assertEqual(1,len(self.ab.get_groups()),"Unable to add group")

    
    def test_unique_groups(self):
        self.ab.add_group("test")
        self.ab.add_group("test")
        self.ab.add_group("test")
        self.assertEqual(1,len(self.ab.get_groups()),"duplicate groups")
        
    
    def test_add_person_validations(self):
        with self.assertRaises(ValueError) as context:
            self.ab.add_person("","lname","",[],[],None)
        self.assertTrue('First Name should be present' in context.exception)
        
        with self.assertRaises(ValueError) as context:
            self.ab.add_person("fname","","",[],[],None)
        self.assertTrue('Last Name should be present' in context.exception)

        with self.assertRaises(ValueError) as context:
            self.ab.add_person("fname","lname","",[],[],None)
        self.assertTrue('Atleast one email should be present' in context.exception)
        
        with self.assertRaises(ValueError) as context:
            self.ab.add_person("fname","lname",[],[],[],None)
        self.assertTrue('Atleast one email should be present' in context.exception)
        
        with self.assertRaises(ValueError) as context:
            self.ab.add_person("fname","lname",["phani@gmail.com"],[],[],None)
        self.assertTrue('Atleast one address should be present' in context.exception)
        
        with self.assertRaises(ValueError) as context:
            self.ab.add_person("fname","lname",["phani@gmail.com"],["Bangalore"],[],None)
        self.assertTrue('Atleast one phone number should be present' in context.exception)
        
        
    def test_add_person(self):
        self.ab.add_person("fname","lname",["phani@gmail.com"],["Bangalore"],[9611411881],["Friends"])
        self.assertEqual(1,len(self.ab.get_groups()),"Incorrect groups")
        self.assertEqual(1,len(self.ab.get_people()),"Incorrect contacts")
        
    def test_add_person_with_multiple_emails(self):
        self.ab.add_person("fname","lname",["phani@gmail.com","sri@yahoo.com"],["Bangalore"],[9611411881],["Friends"])
        self.assertEqual(1,len(self.ab.get_people()),"Incorrect contacts")
        self.assertEqual(2,len(self.ab.get_people()[0].emails),"Incorrect emails")

    def test_prevent_duplicate_person(self):
        self.ab.add_person("fname","lname",["phani@gmail.com"],["Bangalore"],[9611411881],None)
        self.ab.add_person("fname","lname",["phani@gmail.com"],["Bangalore"],[9611411881],None)
        
        self.assertEqual(0,len(self.ab.get_groups()),"Incorrect groups")
        self.assertEqual(1,len(self.ab.get_people()),"Incorrect contacts")
        
    
    def test_find_groups_by_person(self):
        self.ab.add_person("test","kumar",["phani@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.ab.add_person("test2","phani",["second@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.assertEqual(1,len(self.ab.find_person_by_name('test')),"Incorrect result count for  search by name")
        person = self.ab.find_person_by_name('test')[0]
        self.assertEqual(Group('Friends'), self.ab.find_groups_by_person(person).pop(),"Incorrect groups")
    
        
    def test_group_members(self):
        self.ab.add_person("test","lname",["phani@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.ab.add_person("test2","lname",["second@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.assertEqual(2,len(self.ab.find_people_group_name('Friends')),"Incorrect count in a group")
        
    def test_find_person_by_name(self):
        self.ab.add_person("test","kumar",["phani@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.ab.add_person("test2","phani",["second@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.assertEqual(1,len(self.ab.find_person_by_name('test')),"Incorrect result count for  search by name")
        self.assertEqual("kumar",self.ab.find_person_by_name('test')[0].last_name,"Incorrect result count for  search by name")
        self.assertEqual(1,len(self.ab.find_person_by_name('test','kumar')),"Incorrect result count for  search by name")
        self.assertEqual("kumar",self.ab.find_person_by_name('test','kumar')[0].last_name,"Incorrect search result")
        self.assertEqual("kumar",self.ab.find_person_by_name(None,'kumar')[0].last_name,"Incorrect search result")
        
    def test_find_person_by_email(self):
        self.ab.add_person("test","kumar",["phani@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.ab.add_person("test2","phani",["second@gmail.com"],["Bangalore"],[9611411881],['Friends'])
        self.assertEqual("second@gmail.com",self.ab.find_person_by_email('second@gmail.com').emails[0],"Incorrect result for search by email")
        self.assertEqual("second@gmail.com",self.ab.find_person_by_email('second').emails[0],"Incorrect result for search by email")
        self.assertEqual("phani",self.ab.find_person_by_email('second@gmail.com').last_name,"Incorrect result for search by email")
        
if __name__ == '__main__':
    unittest.main()