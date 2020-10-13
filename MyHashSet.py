class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.hashset = [[] for i in range(self.capacity)]
        
    def __get_size(self) -> int:
        return len(self.hashset)
    
    def __get_hash(self, key: int) -> int:
        if key == 0:
            return 0
        return key % self.capacity
    
    def __resize(self):
        self.capacity = int(self.capacity * 1.5)
        new = [[] for i in range(self.capacity)]
        for i, sub in enumerate(self.hashset):
            new[i] = sub
        self.hashset = new
        print(self.capacity)

    def add(self, key: int) -> None:
        # The addition of this method call causes a "Time Limit Exceeded" failure
        #if self.capacity - self.__get_size() < 10:
        #    self.__resize()
        hash_val = self.__get_hash(key)
        if not self.contains(key):
            self.hashset[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = self.__get_hash(key)
        if self.contains(key):
            self.hashset[hash_val].remove(key)
            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_val = self.__get_hash(key)
        for e in self.hashset[hash_val]:
            if e == key:
                return True
        return False