
## 자료구조 과제 

## Problem

You are tasked with developing a system to manage the reservations for a hotel. The system should allow customers to book rooms for a specified duration and check the availability of rooms for a given time period.

Each room in the hotel has the following properties:

- `room_number`: An integer representing the unique identifier for the room.

- `start_timestamp`: An integer representing the Unix timestamp when the room is booked.

- `end_timestamp`: An integer representing the Unix timestamp when the room is vacated.

Implement the `HotelReservation` class:

- `register_room(room_number)`: Adds a room with the specified `room_number` to the system. This method is called once for each room at the system's initiation. This method does not generate any output.

- `add_reservation(room_number, start_timestamp, duration)`: Adds a reservation with the specified `room_number`, `start_timestamp`, and `duration` to the list of reservations. If the room is already reserved for the specified time period, return False; otherwise, return True. If the reservation is successfully added, the room is considered occupied from:
    - `start_timestamp` <= `room_occupied_timestamp` < `start_timestamp` + `duration`
    - Note: The room is considered available at the `start_timestamp` + `duration`.

- `check_availability(start_timestamp, duration)`: Returns a list of all room `room_number`s that are available for booking during the time period starting at the timestamp `start_timestamp`(inclusive) and ending at `start_timestamp` + `duration` (non-inclusive). A room is considered available if it is not reserved for any time period that overlaps with the specified time period.
    - Note1: If no rooms are available, return an empty list, `[]`.
    - Note2: The list should be ordered by `room_number`.

Constraints:

- 1 <= number of rooms <= 10^2

- 1 <= `room_number`, `start_timestamp`, `duration` <= 10^5

- The total number of operations will not exceed 10^7.

## Input specification

The names of the functions and their respective parameters will be provided in the order they are called.

Functions will be separated by a newline, and the parameters of the functions will be separated by whitespace.

## Output specification

For each call to `add_reservation()`, output `True` if the reservation is successfully added, or `False` if the room is already reserved for the specified time period, followed by a single newline.

For each call to `check_availability(start_timestamp, duration)`, output a list of room `room_number`s that are available for booking during the specified time period, separated by a comma and a whitespace, surrounded by brackets `[]`, followed by a single newline. e.g., `[1, 2, 3]`.

## Example

### Sample Input 0

```plaintext
register_room 1
register_room 2
add_reservation 1 100000 1000
add_reservation 2 100000 2000
check_availability 100500 500
check_availability 100500 1000
check_availability 101000 500
check_availability 101000 2000
check_availability 102000 1000
add_reservation 1 100500 500
add_reservation 1 101000 500
add_reservation 1 101000 500
```

True
 True
 []
 []
 [1]
 [1]
 [1,2]
 False
 True
 False


### Sample Output 0

```plaintext
True
True
[]
[]
[1]
[1]
[1, 2]
False
True
False
```

register_room 2
add_reservation 1 100000 1000
add_reservation 2 100000 2000
check_availability 100500 500
check_availability 100500 1000
check_availability 101000 500
check_availability 101000 2000
check_availability 102000 1000
add_reservation 1 100500 500
add_reservation 1 101000 500
add_reservation 1 101000 500

