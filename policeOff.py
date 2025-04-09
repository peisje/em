class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
        self.cases = []
        
    def assign_case(self, case):
        self.cases.append(case)
    
    def get_case_by_id(self, case_id):
        for case in self.cases:
            print(case.get_case_id())
        return self.cases
    
    def get_summary(self):
         total_cases = len(self.cases)
         return f"total cases: {total_cases}"
    
    def get_info(self):
        print("name", self.name, "badge number", self.badge_number)
    
        
        
class Case:
    def __init__(self, case_id, description, status):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []
        
    def add_event(self, event):
        self.events.append(event)
    
    def close_case(self):
         self.status = "closed"
        
    def get_timeline(self):
        for event in self.events:
            return event
        
    def get_status(self):
        return self.status
            
        
    def get_description(self):
        print("description", self.description)
        
    def get_case_id(self):
        return self.case_id
        
        
        
class Event:
    def __init__(self, timestamp, note, officer_name):
        self.timestamp = timestamp
        self.note = note
        self.officer_name = officer_name
        
    
    
off1 = PoliceOfficer("dasa", 2781377)
off2 = PoliceOfficer("lena", 9832177)

event1 = Case(282,"ubili", "dasa")
event2 = Case(442,"ski", "lena")
event3 = Case(332,"dsxi", "elina")

case1 = Case(71, "ubili em","du")
case2 = Case(21, "skinuli","aa")


case1.add_event(event1)
case2.add_event(event2)
case2.add_event(event3)

off1.get_info()
off2.get_info()


event1.get_description()
event1.get_status()


off1.assign_case(case1)
off2.assign_case(case2)
off2.assign_case(case2)
off1.get_case_by_id(71)
off2.get_case_by_id(21)
print(case1.get_status())
print(case2.get_status())


print(off1.get_summary())
print(off2.get_summary())
case1.close_case()
print(case1.get_status())
print(case1.get_case_id())









        
    