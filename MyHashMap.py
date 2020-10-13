class Bucket:
  def __init__(self):
    self.Bucket=[]

  def update(self,key,value):
    condition=False
    for i,kv in enumerate(self.Bucket):
      if key==kv[0]:
        self.Bucket[i]=(key,value)
        condition=True
        break
    if not condition:
      self.Bucket.append((key,value))
  
  def get(self,key):
    for (k,v) in self.Bucket:
      if k==key:
        return v
    return -1

  def remove(self,key):
    for i,kv in enumerate(self.Bucket):
      if kv[0]==key:
        del self.Bucket[i]



class MyHashMap:
  def __init__(self):
    self.key_space=2069
    self.hash_table=[Bucket() for j in range(self.key_space)]

  def put(self,key,value):
    hash_key = key % self.key_space
    self.hash_table[hash_key].update(key, value)

  def get(self,key):
    hash_key = key % self.key_space
    return self.hash_table[hash_key].get(key)

  def remove(self, key):
    hash_key = key % self.key_space
    self.hash_table[hash_key].remove(key)
