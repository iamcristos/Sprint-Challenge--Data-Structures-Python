class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    # self.storage = []

  def append(self, item):
        if self.current <= self.capacity:
              print(self.current)
              self.current += 1
              self.storage[self.current] = item
              return
        self.storage[0] = item

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