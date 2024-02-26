"""
Improvised coded LLD, used encapsulation
"""

from datetime import datetime

class Parking:
    @classmethod
    def set_slots(cls, slots):
        slots_info = {}
        for vehicle_type, parking_slots in slots.items():
            slots_info[vehicle_type] = [0] * parking_slots
        return slots_info

    @classmethod
    def get_slots(cls, slots_info, vehicle_type):
        return slots_info.get(vehicle_type, [])

    @classmethod
    def assign_slot(cls, slots_info, vehicle_type):
        slots = slots_info.get(vehicle_type)
        if slots:
            parking_no = slots.index(0)
            slots[parking_no] = 1
            return parking_no
        return None

    @classmethod
    def free_slot(cls, slots_info, vehicle_type, parking_no):
        slots_info[vehicle_type][parking_no] = 0

class ParkingLot:
    def __init__(self, slots, per_minute_charge) -> None:
        self.slots_info = Parking.set_slots(slots)
        self.tickets = {}
        self.per_minute_charge = per_minute_charge

    def generate_ticket(self, vehicle_number, vehicle_type, parking_no):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ticket = f"{vehicle_type}|{vehicle_number}|{parking_no}|{timestamp}"
        self.tickets[vehicle_number] = ticket
        return ticket

    def entry(self, vehicle_type):
        slots = Parking.get_slots(self.slots_info, vehicle_type)
        return 0 in slots

    def get_ticket(self, vehicle_number):
        return self.tickets.get(vehicle_number)

    def process_payment(self, ticket):
        entry_time_str = ticket.split('|')[-1]
        entry_time = datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
        charge = (datetime.now() - entry_time).seconds * self.per_minute_charge / 60
        print(f"Total charge: ${charge:.2f}")

    def exit(self, vehicle_number):
        ticket = self.get_ticket(vehicle_number)
        if ticket:
            self.process_payment(ticket)
            del self.tickets[vehicle_number]
            vehicle_type, parking_no = ticket.split('|')[0], int(ticket.split('|')[2])
            Parking.free_slot(self.slots_info, vehicle_type, parking_no)

    def park(self, vehicle_type, vehicle_number):
        if self.entry(vehicle_type):
            parking_no = Parking.assign_slot(self.slots_info, vehicle_type)
            if parking_no is not None:
                return self.generate_ticket(vehicle_number, vehicle_type, parking_no)
        return "Parking full"

# slots = {"car": 2, "bike":1, "truck": 0}
# vehicle_no = "MH04SK7866"
# vehicle_type = "car"
# skParking = ParkingLot(slots, 1)
# skParking.park(vehicle_type, vehicle_no)
# skParking.park(vehicle_type, 'MH04SK7868')
# skParking.park(vehicle_type, 'MH04SK7867')
# skParking.exit(vehicle_no)