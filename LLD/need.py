from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def enqueue(self, value):
        # Add the value to the regular queue
        self.queue.append(value)

        # Maintain the max_queue
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Dequeue from an empty queue")

        value = self.queue.popleft()

        # Remove the front of the max_queue if it matches the dequeued value
        if self.max_queue and self.max_queue[0] == value:
            self.max_queue.popleft()

        return value

    def getMax(self):
        if not self.max_queue:
            raise IndexError("Queue is empty")

        return self.max_queue[0]


# Example usage
mq = MaxQueue()
mq.enqueue(1)
mq.enqueue(3)
mq.enqueue(2)
print(mq.getMax())  # Output: 3
print(mq.dequeue())  # Output: 1
print(mq.getMax())  # Output: 3
mq.enqueue(5)
print(mq.getMax())  # Output: 5
