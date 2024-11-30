
import random

class InstantAccessDSError(Exception):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def value_already_present(value):
        return InstantAccessDSError(f"{value} already present in collection")

    @staticmethod
    def value_not_in_collection(value):
        return InstantAccessDSError(f"{value} not in collection")

    @staticmethod
    def no_items_present():
        return InstantAccessDSError("No items present in the collection")


class InstantAccessDS :
    def __init__(self):
        self.ary_items:list[int] = []
        self.index_map = {}

    def insert(self,value:int)-> bool:
        if(value in self.index_map): # element already exist
            raise InstantAccessDSError.value_already_present(value)
            return False
        ary_len = len(self.ary_items)
        self.index_map[value] = ary_len
        self.ary_items.append(value)
        return True

    def delete(self, value:int)-> bool:
        if(value not in self.index_map):
            raise InstantAccessDSError.value_not_in_collection(value)
            return False
        # toDO! check for last element pop1

        last_elm = self.ary_items.pop()
        value_index = self.index_map[value]
        del self.index_map[value]

        if(self.ary_items):
            self.ary_items[value_index] = last_elm
            self.index_map[last_elm] = value_index

        return True

    def getRandom(self)-> int:
        if(not self.ary_items):
            raise InstantAccessDSError.no_items_present()
            return -1
        return random.choice(self.ary_items)

    def getAll(self)-> list[int]:
        return self.ary_items


ds =  InstantAccessDS()

ds.insert(1)
print(ds.getAll()) #=> [1]
ds.insert(2)
ds.insert(21)
ds.delete(2)
ds.insert(12)
print(ds.getAll()) #=> [1, 21, 12]
# ds.insert(12) #=> InstantAccessDSError: 12 already present in collection
print(ds.getRandom()) #=> any one of [1, 21, 12]
ds.delete(1)
# ds.delete(2) #=> InstantAccessDSError: 2 not in collection
ds.delete(12)
ds.delete(21)
print(ds.getAll()) #=> []
print(ds.getRandom()) #=> InstantAccessDSError: No items present in the collection
print(ds.getAll()) #=> []
