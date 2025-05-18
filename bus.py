from abc import ABC, abstractmethod

class Bus(ABC):
    
    def __init__(self,coach_no,bus_name,arrival,departure,starting_location,ending_location,rows,cols):
        self.coach_no=coach_no
        self.bus_name=bus_name
        self.arrival=arrival 
        self.departure=departure
        self.starting_location=starting_location
        self.ending_location=ending_location
        self.seats=[["0" for _ in range(cols)for _ in range(rows)]]
        
class bus(Bus):
    pass

class bus_company():
    
    def  __init__(self):
        self.buses={}
        
    def install_bus(self,bus):
        print("Name:{bus.bus_name} and coach No: {bus.coach_no} is installed sucessfully")
        self.buses[bus.coach_no]=bus
    
    def display_available_buses(self):
        
        
        
        