class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        visited_rooms = set()
        # pick up first keys
        keys.update(rooms[0])
        visited_rooms.add(0)
        while len(keys) != 0:
            new_keys = set()  # Create a new set to collect keys found during this iteration
            for k in keys:
                if k not in visited_rooms:
                    # update new_keys and add the found keys
                    new_keys.update(rooms[k])
                    visited_rooms.add(k)
            keys = new_keys  # Replace keys with new_keys for the next iteration

        # all rooms reached
        if len(visited_rooms) == len(rooms):
            return True
        return False