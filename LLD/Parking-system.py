"""
Self coded LLD, few bugs
"""

from datetime import datetime


class Parking:
    slots = {}

    @classmethod
    def set_slots(cls, slots):
        for vehicle_type, parking in slots.items():
            cls.slots[vehicle_type] = [0] * parking
    
    @classmethod
    def get_slots(cls, vehicle_type):
        return cls.slots.get(vehicle_type, [])
    
    @classmethod
    def assign_slot(cls, vehicle_type):
        slot = cls.slots.get(vehicle_type)
        parking_no = slot.index(0)
        slot[parking_no] = 1
        return parking_no

    @classmethod
    def free_slot(cls, vehicle_type, parking_no):
        cls.slots[vehicle_type][parking_no] = 0
        return parking_no


class ParkingLot:
    tickets = {}
    def __init__(self, slots, per_minute_charge) -> None:
        Parking.set_slots(slots)
        self.per_minute_charge = per_minute_charge

    def generateTicket(self, vehicle_number, vehicle_type, parking_no):
        ticket = f"{vehicle_type}|{vehicle_number}|{parking_no}|{datetime.now()}"
        self.tickets[vehicle_number] = ticket
        return ticket

    def entry(self, vehicle_type):
        slots = Parking.get_slots(vehicle_type)
        if 0 not in slots:
            return False
        return True

    def getTicket(self, vehicle_number):
        return self.tickets[vehicle_number]

    def processPayment(self, ticket):
        entry_time_str = ticket.split('|')[-1]
        entry_time = datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S.%f')
        charge = (datetime.now() - entry_time).seconds * self.per_minute_charge / 60
        print(f"Total charge: ${charge:.2f}")

    def exit(self, vehicle_number):
        ticket = self.getTicket(vehicle_number)
        self.processPayment(ticket)
        del ticket[vehicle_number]
        Parking.free_slot(ticket.split('|')[0], ticket.split('|')[2])

    def park(self, vehicle_type, vehicle_number):
        parking_avl = self.entry(vehicle_type)
        # import pdb; pdb.set_trace()
        if parking_avl:
            parking_no = Parking.assign_slot(vehicle_type)
            return self.generateTicket(vehicle_number, vehicle_type, parking_no)
        return "Parking full"

slots = {"car": 2, "bike":1, "truck": 0}
vehicle_no = "MH04SK7866"
vehicle_type = "car"
skParking = ParkingLot(slots, 1)
skParking.park(vehicle_type, vehicle_no)
skParking.park(vehicle_type, 'MH04SK7868')
skParking.park(vehicle_type, 'MH04SK7867')
skParking.exit(vehicle_no)
