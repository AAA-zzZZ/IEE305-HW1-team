

class Machine:
    def __init__(self, id, type, operations, power_rating):
        self.id = id
        self.type = type
        self.operations = operations
        self.power_rating = power_rating

    def display_info(self): #For printing/ printing each attruibute for machines
        return f"id: {self.id}, type: {self.type}, Operations: {self.operations}, power rating: {self.power_rating}"

class ManufacturingPlant:
    def __init__(self):
        self.machines=[] #store machine objs
    
    def add_machine(self, machine):
        self.machines.append(machine)

    def display_machines(self): #print from machine class
       for machine in self.machines:
            print(machine.display_info())

#defining each machine and their attributes
machine_1= Machine("M1","Lathe","Cutting, Threading", "10kw")
machine_2= Machine("M2","Milling","Drilling, Slotting", "12 kW")
machine_3= Machine("M3", "Welding", "Joining, Fabrication", "8 kW")
machine_4= Machine("M4", "Drilling", "Hole Drilling, Countersink", "6 kW")
machine_5= Machine("M5", "Grinding", "Polishing, Finishing", "5 kW")

#Create a manufacturing plant instance
Plant = ManufacturingPlant()

#Add machines to our list/plant
Plant.add_machine(machine_1)
Plant.add_machine(machine_2)
Plant.add_machine(machine_3)
Plant.add_machine(machine_4)
Plant.add_machine(machine_5)

#Print each Machines attribute
Plant.display_machines()