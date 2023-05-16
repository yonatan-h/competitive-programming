from collections import defaultdict, deque

class LockingTree:

    def __init__(self, parents):
        self.tree = parents
        self.lockers = [None]*len(parents)
        self.adj_list = defaultdict(list)

        for child in range(len(parents)):
            parent = parents[child]
            self.adj_list[parent].append(child)
        

    def lock(self, num: int, user: int) -> bool:
        if self.lockers[num] == None:
            self.lockers[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lockers[num] == user:
            self.lockers[num] = None
            return True
        else:
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        if self.lockers[num] != None:
            return False
        if not self.has_locked_descendants(num):
            return False
        if not self.all_unlocked_ancestors(num):
            return False
        
        self.unlock_descendants(num)
        self.lock(num, user)
        return True
    
    def unlock_descendants(self, num):
        queue = deque()
        queue.append(num)

        while queue:
            node = queue.pop()
            children = self.adj_list[node]
            for child in children:
                self.lockers[child] = None
            queue.extend(children)

    def has_locked_descendants(self, num):
        queue = deque()
        queue.append(num)

        while queue:
            node = queue.pop()
            if self.lockers[node] != None:
                return True
            children = self.adj_list[node]
            queue.extend(children)

        return False
            

    def all_unlocked_ancestors(self, num):
        cur_node = num

        while cur_node != -1:
            parent = self.tree[cur_node]
            if self.lockers[parent] != None:
                return False
            cur_node = parent

        return True






        


# Your LockingTree object will be instantiated and called as such:
obj = LockingTree([-1,0,0,1,1,2,2])
print(obj.lock(5,99))
print(obj.upgrade(2,5))
print(obj.lock(2,995))
print(obj.lock(5,995))