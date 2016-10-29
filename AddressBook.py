class Person(object):
    def __init__(self,first_name,last_name,emails,address,phone_numbers,groups):
        self.__validate(first_name,last_name,emails,address,phone_numbers)
        self.first_name = first_name
        self.last_name = last_name
        self.emails = emails
        self.address = address
        self.phone_numbers = phone_numbers
        self.groups = groups
        
    def __validate(self,first_name,last_name,emails,address,phone_numbers):
        if not first_name or first_name.isspace():
            raise ValueError("First Name should be present")
            
        if not last_name or last_name.isspace():
            raise ValueError("Last Name should be present")
        
        if not emails:
            raise ValueError("Atleast one email should be present")
        
        if not address:
            raise ValueError("Atleast one address should be present")
            
        if not phone_numbers:
            raise ValueError("Atleast one phone number should be present")
     
    def __eq__(self, other):
        return getattr(other, 'first_name', None) == self.first_name # and getattr(other, 'last_name', None) == self.last_name #and getattr(other, 'emails', None) == self.emails
            
    def __hash__(self):
        return hash(self.first_name + self.last_name)
    

class Group(object):
    def __init__(self,group_name):
        self.name = group_name
        self.people = set()
        
    def add_person(self,person):
        self.people.add(person)
        
    def get_people(self):
        return self.people

    def get_group_name(self):
        return self.name

    def __eq__(self, other):
        return getattr(other, 'name', None) == self.name
    
    def __hash__(self):
        return hash(self.name)

class AddressBook(object):

    def __init__(self):
        self.groups = set()
        self.people = set()
        
    def add_group(self,group_name):
        group = Group(group_name)
        self.groups.add(group)
        
    def get_groups(self):
        return list(self.groups)
        
    def find_group(self,group_name):
        for g in self.groups:
            if group_name == g.get_group_name():
                return g
        return None
        
    def get_people(self):
        return list(self.people)    
                    
    def __add_groups(self,group_names):
        if group_names is None:
            group_names = []
        for g in group_names:
            self.add_group(g)
    
    
    def __get_groups(self,group_names):
        contact_groups = set()
        if group_names is not None:
            for g in group_names:
                for e in self.groups:
                    if e.name == g:
                        contact_groups.add(e)                
        return contact_groups
        

    def add_person(self,first_name,last_name,emails,address,phone_numbers,group_names=None):
        self.__add_groups(group_names)
        groups = self.__get_groups(group_names)
        person = Person(first_name,last_name,emails,address,phone_numbers,groups)
        for g in groups:
            g.add_person(person)
        self.people.add(person)
        
    def find_people_group_name(self,group_name):
        group = self.find_group(group_name)
        if group is not None:
            return group.get_people()
        return []
        
        
    def find_person_by_name(self,first_name=None,last_name=None):
        if first_name is None and last_name is None:
            return []
        results = []
        for p in self.people:
            if first_name is not None and last_name is not None:
                if first_name == p.first_name and last_name ==p.last_name:
                    results.append(p)
                    
            elif first_name is not None:
                if first_name == p.first_name:
                    results.append(p)
            else:
                if last_name == p.last_name:
                    results.append(p)
        return results
        
    def find_person_by_email(self,email):
        if email is None:
            return None
        for p in self.people:
            for e in p.emails:
                if e.startswith(email) or e == email:
                    return p
        return None
        
    def find_groups_by_person(self,person):
        if person is None:
            return None
        return person.groups
        
                
