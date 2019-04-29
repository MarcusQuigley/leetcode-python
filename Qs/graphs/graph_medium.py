def keys_and_room(rooms):
    num_rooms = len(rooms) 
    visited = [False] * num_rooms
    queue = [0]
    while len(queue) > 0:
        room = queue.pop()
        if visited[room] == False:
            visited[room] = True
            keys = rooms[room]
            for key in keys:
                if visited[key] == False: 
                    queue.append(key)
    
    return (False not in visited)

def keys_and_room_better_storage(rooms):
    queue = [0]
    visited = set(queue)

    while queue:
        room = queue.pop()
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                queue.append(key)
                if len(visited) == len(rooms): return True
    return len(visited) == len(rooms)
     
