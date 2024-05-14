# 올바른 값이 나옴
# 호텔 에약 시스템의 백엔드를 개발하라
# 이진 탐색 트리
# 왼쪽 노드가 오른쪽 노드 보다 무조건 작은 구조이다.
# 삽입 삭제 탐색의 경우
# 검색이나 삽입 삭제의 경우에 사용
# 그렇다면 딕셔너리를 사용하나?
# class에 들어가는 인자 = room_number` `start_timestamp` `end_timestamp
# orderd map을 기반으로 만들어라
# 이진 탐색은 정렬된어 있는 리스트에서 중간을 가르고 대소 비교를 통해 찾는 것을 의미한다 = 아니 그럼 이것도 이진 트리로 찾을 수 있는 거 아닌가?
# in-order traversal을 이용하자
# 내가 해야 하는 것 일단 새로 들어오는 호텔 번호와 일정을 insert 해야 한다 -
# 이진 탐색 트리의 insert 하는 방법 = 위에서 부터 대소 비교를 통해 내려오고 적절한 위치에 저장한다. 
# 탐색하고 불가능 하면 불가능 하다는 것을 알려주는 알고리즘을 제작해야 한다.


class TreeNode:
    #import를 사용핵 트리를 만들지 않을 것이라면 tree node를 직접 작성해주어여 한다.
    def __init__(self, room_number):
        #room_number만을 매개변수로 받음 나머지는 받을 필요가 없기 때문이다
        self.room_number = room_number
        self.reservations = []
        #예약 된 정보를 [] 리스트에 저장한다. 
        self.left = None
        self.right = None
        #각 왼쪽 오른쪽 노드는 비운다

    def add_reservation(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        # 예약 시간이 겹치는지 확인
        for start, end in self.reservations:
            #reservation에 있는 정보를 start와 end로 나누어 정리해준다.
            if start_timestamp < end and end_timestamp > start:
                #중복되는 시간들을 모두 제외시켜 준다
                return False
        self.reservations.append((start_timestamp, end_timestamp))
        #중복되는 것이 없다면 참이기 때문에 리스트에 저장해준다.
        self.reservations.sort()  # 예약을 시간순으로 정렬
        return True # 가능한다는 것을 리턴해준다.

    def is_available(self, start_timestamp, duration):
        end_timestamp = start_timestamp + duration
        for start, end in self.reservations:
            if start_timestamp < end and end_timestamp > start:
                return False
        return True
    # 가능한지에 대한 여부만을 알려주기 때문에 true만 리턴 해준다.

class HotelReservation:
    def __init__(self):
        self.root = None
        # 처음의 뿌리 노드는 비워준다.

    def register_room(self, room_number):
        # 방 등록 하기
        if not self.root:
            #root node가 비어있다면 
            self.root = TreeNode(room_number)
            #리스트에 저장해준다. numnumber를 
            return True
        else:
            return self._insert(self.root, room_number)
        #root가 있다면 _insert 함수를 재귀적으로 호출해 왼쪽 오른쪽으로 정한 뒤 추가해준다.

    def _insert(self, node, room_number):
        # 초기에는 node 매개변수를 작성할 필요가 없다 어차피 비어있기 떄문이다.
        if room_number < node.room_number:
            # 각 room_number마다 크기를 비교한다. 이진 탐색 트리 성격 상 크기 순서대로 정렬되어 있기 때문이다.
            if not node.left:
                #왼쪽 노드가 비어있다면 
                #새로 추가되는 노드가 기존의 있는 노드보다 작으면 왼쪽 노드에 저장된다
                node.left = TreeNode(room_number)
                return True
            else:
                return self._insert(node.left, room_number)
            #비어있지 않다면 서브 트리로 내려가는데 거기서도 크기비교를 통해 위치를 정한다.

        elif room_number > node.room_number:
            # 새로들어오는 룸넘버가 기존 보다 크다면
            if not node.right:
                #오른쪽이 비어있는 경우
                node.right = TreeNode(room_number)
                #추가해준다
                return True
            else:
                return self._insert(node.right, room_number)
            # 비어있지 않다면 또 크기 비교를 통해 추가해준다.
        else:
            return False  # 중복 방 번호 추가 방지

    def add_reservation(self, room_number, start_timestamp, duration):
        node = self._find(self.root, room_number)
        #room_number가 들어갈 수 있는 위치를 찾는다.
        if node:
            return node.add_reservation(start_timestamp, duration)
        #위치를 찾았다면 그 자리에 추가해준다.
        return False

    def _find(self, node, room_number):
        if node is None:
            #루트가 없다면 찾지 못했다는 것을 리턴해준다
            return None
        elif node.room_number == room_number:
            #노드의 크기가ㅣ 같다면 해당 노드를 리턴해준다.
            return node
        elif room_number < node.room_number:
            return self._find(node.left, room_number)
        #새로 들어온 노드가 더 작다면 왼쪽 과 비교를 통해 찾는다.
        else:
            return self._find(node.right, room_number)
        #둘다 아니라면 오른쪽 노드와 같은지를 검사해 찾느다

    def check_availability(self, start_timestamp, duration):
        #예약이 가능한지에 대해 조사한다.
        available_rooms = []
        self._check_availability(self.root, start_timestamp, duration, available_rooms)
        return sorted(available_rooms)
    #_check_availability 여기서 가능한지 여부를 확인했음으로 정렬해준다.

    def _check_availability(self, node, start_timestamp, duration, available_rooms):
        if node:
            if node.is_available(start_timestamp, duration):
                available_rooms.append(node.room_number)
                 #중복되는 값이 있는지 확인하고 이를 넣어줌
            self._check_availability(node.left, start_timestamp, duration, available_rooms)
            self._check_availability(node.right, start_timestamp, duration, available_rooms)
            #왼쪽 노드 오른쪽 노드 모두 진행한다.

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
#출력문
