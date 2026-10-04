from collections import deque
import heapq


# ============================================================
# TASK 1: IMPLEMENT THE GIVEN GRAPH
# ============================================================

print("========== TASK 1 ==========")

# Graph from the diagram
graph1 = {
    0: [1, 4],
    1: [0, 4, 3, 2],
    2: [1, 3],
    3: [1, 4, 2],
    4: [0, 1, 3]
}

print("Graph:")
for vertex in graph1:
    print(vertex, "->", graph1[vertex])


# ============================================================
# TASK 2: BREADTH FIRST SEARCH USING QUEUE
# Starting node = A
# Goal node = G
# ============================================================

print("\n========== TASK 2 ==========")

# Tree from the lab diagram
graph2 = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}


def BFS(graph, start, goal):

    # Create a queue
    queue = deque()

    # Insert starting node into queue
    queue.append(start)

    # Set for visited nodes
    visited = set()

    while queue:

        # Remove the first node from queue
        current = queue.popleft()

        # If already visited, skip it
        if current in visited:
            continue

        # Mark node as visited
        visited.add(current)

        print(current, end=" ")

        # Stop when goal is found
        if current == goal:
            print("\nGoal G achieved!")
            return

        # Add neighbours to queue
        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append(neighbour)


print("BFS Traversal:")
print("Starting from A:")

BFS(graph2, 'A', 'G')


# ============================================================
# TASK 3: IMPLEMENT PRIORITY QUEUE
# ============================================================

print("\n========== TASK 3 ==========")

# Create an empty priority queue
priority_queue = []

# Insert elements
heapq.heappush(priority_queue, (3, "C"))
heapq.heappush(priority_queue, (1, "A"))
heapq.heappush(priority_queue, (4, "D"))
heapq.heappush(priority_queue, (2, "B"))

print("Priority Queue:")

# Remove elements according to priority
while priority_queue:

    priority, value = heapq.heappop(priority_queue)

    print("Priority:", priority, "Value:", value)
