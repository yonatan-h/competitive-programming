class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #entries : durations : index
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        tasks = deque(tasks)

        time = 0
        heap = [(0,-1,time)] #duration, index, entry
        order = []
        length = len(tasks)

        while heap:
            dur, ind, ent = heappop(heap)
            order.append(ind)

            next_time = time+dur
            if (tasks and not heap) and (next_time < tasks[0][0]):
                next_time = tasks[0][0]
            
            while tasks and tasks[0][0] <= next_time:
                e,d,i = tasks.popleft()
                heappush(heap,(d,i,e))
            time=next_time
  
        return order[1:]


