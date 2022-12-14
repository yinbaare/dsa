class MinHeap:
    def __init__(self) -> None:
        self.heap = [0]
        self.size = 0


    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //=2

    def insert(self, item):
        self.heap.append(item)
        self.size +=1
        self.arrange(self.size)

    def minChild(self, k):
        if k * 2 +1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k*2
        else:
            return k*2+1
    def sink(self,k):
        while k*2 <=self.size:
            mc = self.minChild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def delete_at_root(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -=1
        self.heap.pop()
        self.sink(1)
        return item
    def  delete_at_location(self, loc):
        item = self.heap[loc]
        self.heap[loc] = self.heap[self.size]
        self.size -=1
        self.heap.pop()
        self.sink(loc)
        return item

    def heap_sort(self):
        sorted_list = []
        for _ in range(self.size):
            n = self.delete_at_root()
            sorted_list.append(n)
        return sorted_list

h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)
n = h.delete_at_location(2)
print(n)
print(h.heap)

h  = MinHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsorted_list:
    h.insert(i)
print("Unsorted list: {}".format(unsorted_list))
print("Heap: {}".format(h.heap))
print("Sorted list: {}".format(h.heap_sort()))