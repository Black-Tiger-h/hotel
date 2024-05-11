#올바른 값이 나옴


class TreeNode:
    def __init__(self, room_number):
        self.room_number = room_number
        self.reservations = []
        self.left = None
        self.right = None

    def add_reservation(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        # 예약 시간이 겹치는지 확인
        for start, end in self.reservations:
            if start_timestamp < end and end_timestamp > start:
                return False
        self.reservations.append((start_timestamp, end_timestamp))
        self.reservations.sort()  # 예약을 시간순으로 정렬
        return True

    def is_available(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        for start, end in self.reservations:
            if start_timestamp < end and end_timestamp > start:
                return False
        return True

class HotelReservation:
    def __init__(self):
        self.root = None

    def register_room(self, room_number):
        if not self.root:
            self.root = TreeNode(room_number)
            return True
        else:
            return self._insert(self.root, room_number)

    def _insert(self, node, room_number):
        if room_number < node.room_number:
            if not node.left:
                node.left = TreeNode(room_number)
                return True
            else:
                return self._insert(node.left, room_number)
        elif room_number > node.room_number:
            if not node.right:
                node.right = TreeNode(room_number)
                return True
            else:
                return self._insert(node.right, room_number)
        else:
            return False  # 중복 방 번호 추가 방지

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
        if node:
            if node.is_available(start_timestamp, duration):
                available_rooms.append(node.room_number)
            self._check_availability(node.left, start_timestamp, duration, available_rooms)
            self._check_availability(node.right, start_timestamp, duration, available_rooms)

def main():
    hotel = HotelReservation()
    while True:
        command = input(" ")
        if command.lower() == "exit":
            break
        parts = command.split()
        action = parts[0]

        if action == "register_room":
            room_number = int(parts[1])
            hotel.register_room(room_number)
        elif action == "add_reservation":
            room_number = int(parts[1])
            start_timestamp = int(parts[2])
            duration = int(parts[3])
            result = hotel.add_reservation(room_number, start_timestamp, duration)
            print("True" if result else "False")
        elif action == "check_availability":
            start_timestamp = int(parts[1])
            duration = int(parts[2])
            available = hotel.check_availability(start_timestamp, duration)
            print(str(available).replace(" ", ""))

if __name__ == "__main__":
    main()
