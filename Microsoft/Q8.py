class Solution:
    def __init__(self):
        self._map = {}
        self._level = 1

    def connect(self, root):
        self._level += 1
        if root.right:           
            self.connect(root.right)  
        if root.left:
            self.connect(root.left)
        self._level -= 1

        if self._map.get(self._level):
            root.nextRight = self._map.get(self._level)
            
        self._map[self._level] = root