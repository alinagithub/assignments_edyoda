#Implement a queue using the stack data structure?
class QueueUsingStack:
    def __init__(self):
        """
        Initialize an empty queue using two stacks.
        """
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        """
        Get the current size of the queue.

        Returns:
            int: The size of the queue.
        """
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Args:
            item: The item to be enqueued.
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.

        Returns:
            item: The item that was dequeued.
        """
        if len(self.stack2) == 0:
            # If stack2 is empty, transfer all items from stack1 to stack2 in reverse order
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            # If both stacks are empty, the queue is empty
            return None

        return self.stack2.pop()

# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())  # Output: 3
print("Dequeued item:", queue.dequeue())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 2
print("Queue size:", queue.size())  # Output: 1