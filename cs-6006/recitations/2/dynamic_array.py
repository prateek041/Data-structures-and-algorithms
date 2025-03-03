from typing import List
import math


class Dynamic_Array:
    def __init__(self):
        self.size = 0
        self.array = []
        self.array_value_bound = 0
        pass

    def __len__(self):
        return self.size

    def __iter__(self):
        yield self.array

    def build(self, x: List[int]):
        for index, item in enumerate(x):
            while index >= self.size:
                self._resize()
            self.array[index] = item
        self.array_value_bound = len(x)
        return self

    def _resize(self):
        current_size = self.size if self.size > 0 else 1
        new_size = current_size * 2
        new_array = [None]*new_size
        new_array = self._old_to_new(True, new_array)
        self.array = new_array
        self.size = len(new_array)

    def _old_to_new(self, isBuildProcess, new_array: List[int])->List[int]:
        if self.size == 0:
            return new_array
        if isBuildProcess:
            for index, _ in enumerate(self.array):
                new_array[index] = self.array[index]
        else:
            for index in range(self.array_value_bound):
                new_array[index] = self.array[index]
        return new_array


    def insert_last(self, item: int)-> None:
        if self.size == self.array_value_bound:
            self._resize()
            return self.insert_last(item)
        self.array[self.array_value_bound] = item

    def _resize_decrese(self):
        current_size = self.size if self.size > 0 else 1
        new_size = math.floor(current_size / 2)
        new_array = [None]*new_size
        new_array = self._old_to_new(False, new_array)
        self.array = new_array
        self.size = len(new_array)


    def delete_last(self):
        self.array[self.array_value_bound - 1] = None
        print("comparing to",math.floor((self.size)/4))
        
        if self.array_value_bound <= math.floor((self.size)/4):
            print("decresing size")
            self._resize_decrese()
            self.size = len(self.array) - 1
        self.array_value_bound -= 1
        print("final array", self.array)

    def insert_at(self, index):
        pass

    def delete_at(self):
        pass

    def insert_first(self):
        pass

    def delete_first(self):
        pass

test = [1, 2, 3, 4, 5]
d_array = Dynamic_Array().build(test)
print("STARTING WITH", d_array.array)
# [1, 2, 3, 4, 5, None, None, None]
print("DELETE OPERATION")
d_array.delete_last()
# [1, 2, 3, 4, None, None, None, None]

print("DELETE OPERATION")
d_array.delete_last()
# [1, 2, 3, None, None, None, None, None]

print("DELETE OPERATION")
d_array.delete_last()
# [1, 2, None, None, None, None, None, None]
# [1, 2, None, None]

print("DELETE OPERATION")
d_array.delete_last()
# [1, None, None, None]
# [1, None]

print("FINALLY")
for item in d_array:
    print(item)
