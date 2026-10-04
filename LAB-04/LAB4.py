# Question 1: Implement Stack using Python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0


# Question 2: Implement Queue using Python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0


# Question 3: Binary Search Implementation matching the Lab example
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 1

    print(f"Search ( {target} )\n")

    while low <= high:
        mid = (low + high) // 2
        print(f"#{step}")
        print(f"Low: {low} | High: {high} | Mid: {mid}")
        print(f"Value at Mid: {arr[mid]}")

        if arr[mid] == target:
            print(f"{arr[mid]} == {target}")
            print("\nSuccessful Search !!")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target} ---> Low = Mid + 1 = {mid + 1}\n")
            low = mid + 1
        else:
            print(f"{arr[mid]} > {target} ---> High = Mid - 1 = {mid - 1}\n")
            high = mid - 1

        step += 1

    return -1


# Execution matching the Lab 4 trace example exactly
if __name__ == "__main__":
    # Question 1 Demo
    print("=== QUESTION 1: STACK ===")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Popped element:", s.pop())

    # Question 2 Demo
    print("\n=== QUESTION 2: QUEUE ===")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print("Dequeued element:", q.dequeue())

    # Question 3 Demo (Exact dataset and target from Lab 4 diagram)
    print("\n=== QUESTION 3: BINARY SEARCH ===")
    number = [6, 12, 17, 23, 38, 45, 77, 84, 90]
    target = 45
    binary_search(number, target)

