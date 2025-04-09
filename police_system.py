class PoliceOfficer:
    def __init__(self,name,budge_number):
        self.name=name
        self.budge_number=budge_number
        self.cases=[]
    
    def assign_case(self,case):
        self.cases.append(case)
    
    def get_case_by_id(self,case_id):
        for case in self.cases:
            if case.case_id ==case_id:
                print(case.description)
            
            
        
        
        
    
    def get_summary(self):
        total_cases=len(self.cases)
        print("Officer have ",total_cases, "cases")
        
        
    
    def get_info(self):
        print("name:",self.name,",budge number:",self.budge_number)
    
    
class Case:
    def __init__(self,case_id,description):
        self.case_id=case_id
        self.description=description
        self.status=True
        self.events=[]
        
    def add_event(self,event):
        self.events.append(event)
        
        
        
    
    def close_case(self):
        self.status=False
    
    def get_timeline(self):
        for event in self.events:
            print(event)
        else:
            print("vale id")
    
    def get_status(self):
        if self.status==True:
            print("case is open")
        else:
            print("case is close")
    
    def get_description(self):
        print("description:",self.description)
    
    def get_case_id(self):
        print("case id:",self.case_id)
        
    def riority(self):
        pass
    
    
class Event:
    def __init__(self,timestamp,note,officer_name):
        self.timestamp=timestamp
        self.note=note
        self.officer_name=officer_name
        
    def __str__(self):
        print(event1.timestamp,event1.note,event1.officer_name)
    
 
officer1=PoliceOfficer("Mustafa",4)
officer2=PoliceOfficer("Natalja",9)

case1=Case(666,"bla bla bla blu blu blu")
case2=Case(744,"dasa was killed")

event1=Event("12.22.25","note number 1","Natalja")
event2=Event("12.22.25","note number 2","Natalja")

case1.add_event((event1.timestamp,event1.note,event1.officer_name))
case1.add_event((event2.timestamp,event2.note,event2.officer_name))
case1.get_timeline()

officer1.assign_case(case1)
officer1.assign_case(case2)
officer1.get_case_by_id(66)

event2.__str__()

officer1.get_summary()



    