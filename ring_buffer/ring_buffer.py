class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    # self.storage = []

  def append(self, item):
        if self.current == self.capacity:
              self.current = 0
        self.storage[self.current] = item
        self.current += 1   

  def get(self):
    for i in self.storage:
        if i is None:
              self.storage.remove(i)
          
    return self.storage
    pass
  

check = RingBuffer(5);

check.append('a')
check.append('b')
check.append('c')
check.append('d')
check.append('e')
check.append('d')

print(check.get())