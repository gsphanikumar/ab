API usage:

ab = AddressBook();
ab.add_person(first_name,last_name,[emails],[addresses],[phone_numbers],[groups])
ab.add_group(group_name)
ab.find_groups_by_person(person)
ab.find_people_group_name(group_name)
ab.find_person_by_name(first_name=None,last_name=None)
ab.find_person_by_email(email)



Examples:

ab.add_person("fname","lname",["phani@gmail.com"],["Bangalore"],[9611411881],["Friends"])
ab.add_group("Friends")
ab.find_people_group_name('Friends')
ab.find_groups_by_person(person)
ab.find_person_by_name('first')
ab.find_person_by_name(None,'second')
ab.find_person_by_name('first','second')
ab.find_person_by_email('second@gmail.com')


Implementing find person by any substring of email:

If we are limited to a library we can implement this search using multiple ways:

1) using regular expressions, we can do something like below
   import re
   re.search(any_string, email, re.IGNORECASE)
   
2) We can create an index for all the characters in an email and use that index.
   eg: for emails extra@example.com, sample@example.com we would create the below indexes
       email1 = extra@example.com
	   email2 = zebra@yahoo.com
    
	  {'e': [email1,email2],a:[email1,email2],y:[email1,email2]}

   If we search for yah,From the above index we can form a set of emails which have yah and then search for emails which have yah contiguously

3) Use a third party module called woosh which does the indexing and searching. 

If a backend server can be used, then We can use solr to search.
 


