class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if self.current == self.capacity:
    # if len(self.storage) == self.capacity:
    #   self.current = 0
    #   self.append(item)
    # self.storage[self.current] = item
    # self.current += 1

    # if (self.current - 1) == self.capacity:
    # if self.current == self.capacity:
    #   self.current = 0
    #   # self.append(item)
    # self.storage[self.current] = item
    # self.current += 1

    self.storage[self.current] = item

    # if (self.current + 1) == self.capacity:
    if self.current == self.capacity - 1:
      self.current = 0
    else:
      self.current += 1



  def get(self):
    # if self.current > 0:
    # return self.storage

    # return self.storage[:self.current]

    if self.storage[-1] == None:
      return self.storage[:self.current]
    else:
      return self.storage