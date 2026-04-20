class DynamicArray:
    
    def __init__(self, capacity: int):
        self.c = capacity
        self.ln = 0
        self.arr = [0] * self.c


    def get(self, i: int) -> int:
        if i < self.c:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.c:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.ln == self.c:
            self.resize()
        self.arr[self.ln] = n
        self.ln += 1


    def popback(self) -> int:
        if self.ln > 0:
            self.ln -= 1
        return self.arr[self.ln]
 

    def resize(self) -> None:
        self.c *= 2
        arr = [0] * self.c
        for i in range(self.ln):
            arr[i] = self.arr[i]
        self.arr = arr


    def getSize(self) -> int:
        return self.ln
        
    
    def getCapacity(self) -> int:
        return self.c
