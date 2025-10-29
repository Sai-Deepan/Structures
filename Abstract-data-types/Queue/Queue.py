#Sai

"""
"""

#Queue implemented in List


class Queue:
    def __init__(self, queue):
        self.queue = queue if queue is not None else []

    def push(self,item):
        self.queue.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if len(self.queue) != 0:
            item = self.queue.pop(0)
            print(f"Popped: {item}")
        else:
            return "UnderFlow"

    def top(self):
        if len(self.queue) != 0:
            print(f"Top: {self.queue[0]}")
        else:
            return "EmptyQueue"

    def size(self):
        if len(self.queue) != 0:
            print(f"Size: {len(self.queue)}")
        else:
            return "EmptyQueue"

