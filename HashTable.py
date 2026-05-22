class HashTable:
    collection={
    }
    def hash(self, string):
        return sum(ord(char)for char in string)
    def add(self, key, value):
        hashed=self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed]={}
        self.collection[hashed][key]= value
    def remove(self,key):
        hashed=self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
    
    def lookup(self,key):
        hashed=self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]
        return None
