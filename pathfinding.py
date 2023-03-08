import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, obstacles):
    open_set = []
    closed_set = set()
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    heapq.heappush(open_set, (f_score[start], start))

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        closed_set.add(current)

        for neighbor in get_neighbors(current, obstacles):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in [i[1] for i in open_set] or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def get_neighbors(pos, obstacles):
    neighbors = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
    valid_neighbors = []
    for n in neighbors:
        if n[0] < 0 or n[0] >= len(obstacles) or n[1] < 0 or n[1] >= len(obstacles[0]):
            continue
        if obstacles[n[0]][n[1]]:
            continue
        valid_neighbors.append(n)
    return valid_neighbors

# Define the start, goal, and obstacles
start = (0, 0)
goal = (2, 2)
obstacles = [
    [False, False, False, False, False, False],
    [False, True, True, False, True, False],
    [False, False, False, False, True, False],
    [False, True, False, True, True, False],
    [False, True, False, False, False, False],
    [False, False, False, False, False, False],
]

# Call the astar function to find the path
path = astar(start, goal, obstacles)

# Print the path
if path:
    print("Path found:", path)
else:
    print("No path found")
