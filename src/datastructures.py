
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = ([{
        'id': self._generateId(),
        'age': 33, 
        'first_name': 'John', 
        #'last_name': last_name,
        'lucky_numbers': [7, 13, 22]
    }, 
    {
        'id': self._generateId(),
        'age': 35, 
        'first_name': 'Jane', 
        'lucky_numbers': [10, 14, 3]
    }, 
    {
        'id': self._generateId(),
        'age': 5, 
        'first_name': 'Jimmy', 
        'lucky_numbers': [1]}
    ])
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        #Si member no tiene un id, creale un id
        if not member.get("id"):
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        #Si no existe el miembro
        return False

    def get_member(self, id):
         for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    print(get_all_members)