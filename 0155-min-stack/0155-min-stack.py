class MinStack(object):
    def __init__(self):
        self.items = []
    
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])
    
    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.items[-1][0]
    
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return 0
        else:
            return self.items[-1][1]