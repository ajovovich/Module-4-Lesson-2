#Task 1:Vehicle Registration System
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self):
            print(f'The owner of the {self.type} is {self.owner}, the registration number is:{self.registration_number}')

owner1 = Vehicle(1837528392, 'Jetta Gli', 'Mark')
owner2 = Vehicle(1837528392, 'Jetta Gli', 'Andreas')
owner3 = Vehicle(1837528392, 'Jetta Gli', 'Ray')

owner1.update_owner()
owner2.update_owner()
owner3.update_owner()


#Task 2:Event Management System Enhancement 

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0

        def add_participant(self):
            self.participant_count += 1
        
        def get_participant_count(self):
            return self.participant_count
        
event1 = Event('Fair', '07/15/2024')

event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()


count = event1.get_participant_count()

print(f'The count of participants that attended the Fair is: {count}')