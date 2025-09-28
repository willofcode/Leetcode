class DynamicArray:
    
    def __init__(self, capacity: int):
        # initialize capacity and dynamic array size
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity
        # O(n) for n elements of capacity

    def get(self, i: int) -> int:
        # get the i-th element from dynamic array at index i
        return self.arr[i]
        # O(1) for constant time look up

    def set(self, i: int, n: int) -> None:
        # insert index i with the element, ensure that index i exist
        self.arr[i] = n
        # O(1) for insertion

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1
        # O(n) for worstcase and O(1) ammoritized/ avg case

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]
        # O(1)

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newarr = [0] * self.capacity

        for i in range(self.size):
            newarr[i] = self.arr[i]

        self.arr = newarr
        # O(n) where n is dependent on size of array

    def getSize(self) -> int:
        return self.size
        # O(1) look up

    def getCapacity(self) -> int:
        return self.capacity
        # O(1) look up

