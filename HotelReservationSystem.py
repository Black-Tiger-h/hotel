class TreeNode:
    def __init__(self, room_number):
        self.room_number = room_number
        self.reservations = []
        self.left = None
        self.right = None
    
    def add_reservation(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        for start, end in self.reservations:
            if start_timestamp < end and end_timestamp > start:
                return False
        self.reservations.append((start_timestamp, end_timestamp))
        self.reservations.sort()  # Keep reservations sorted for easier management
        return True

    def is_available(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        for start, end in self.reservations:
            if start_timestamp < end and end_timestamp > start:
                return False
        return True

class HotelReservationBST:
    def __init__(self):
        self.root = None

    def register_room(self, room_number):
        if not self.root:
            self.root = TreeNode(room_number)
        else:
            self._insert(self.root, room_number)
    
    def _insert(self, node, room_number):
        if room_number < node.room_number:
            if not node.left:
                node.left = TreeNode(room_number)
            else:
                self._insert(node.left, room_number)
        elif room_number > node.room_number:
            if not node.right:
                node.right = TreeNode(room_number)
            else:
                self._insert(node.right, room_number)
    
    def add_reservation(self, room_number, start_timestamp, duration):
        node = self._find(self.root, room_number)
        if node:
            return node.add_reservation(start_timestamp, duration)
        return False

    def _find(self, node, room_number):
        if node is None:
            return None
        elif node.room_number == room_number:
            return node
        elif room_number < node.room_number:
            return self._find(node.left, room_number)
        else:
            return self._find(node.right, room_number)
    
    def check_availability(self, start_timestamp, duration):
        available_rooms = []
        self._check_availability(self.root, start_timestamp, duration, available_rooms)
        return sorted(available_rooms)

    def _check_availability(self, node, start_timestamp, duration, available_rooms):
        if node is not None:
            if node.is_available(start_timestamp, duration):
                available_rooms.append(node.room_number)
            self._check_availability(node.left, start_timestamp, duration, available_rooms)
            self._check_availability(node.right, start_timestamp, duration, available_rooms)

def main():
    hotel = HotelReservationBST()
    while True:
        command = input("Enter command (register, reserve, check, exit): ")
        if command.startswith("register"):
            _, room_number = command.split()
            hotel.register_room(int(room_number))
            print(f"Room {room_number} registered.")

        elif command.startswith("reserve"):
            _, room_number, start_timestamp, duration = command.split()
            if hotel.add_reservation(int(room_number), int(start_timestamp), int(duration)):
                print("Reservation successful.")
            else:
                print("Reservation failed: time slot already booked.")

        elif command.startswith("check"):
            _, start_timestamp, duration = command.split()
            available_rooms = hotel.check_availability(int(start_timestamp), int(duration))
            print("Available rooms:", available_rooms)

        elif command == "exit":
            print("Exiting the reservation system.")
            break

if __name__ == "__main__":
    main()
