from heapq import heappush,heappop,heapify

class CombinedContainer:
    def __init__(self,val,logo):
        self.value = -val
        self.logo = logo
        
    def __lt__(self,obj):
        if self.value != obj.value:
            return self.value < obj.value
        else:
            return self.logo < obj.logo
			

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans, task_map = 0, {}
        for task in tasks:
            task_map[task] = task_map.get(task,0) + 1
        mycont = [CombinedContainer(value,key) for key,value in task_map.items()]
        heapify(mycont)
        i, tans = 0, n+1
        while i<len(tasks):
            if n-tans>=0:
                ans += n-tans+1
            popping,tans = [],0
            while mycont:
                elm = heappop(mycont)
                elm.value += 1
				
                if elm.value:
                    popping.append(elm)
                tans,i = tans+1, i+1
                if tans > n:
                    break
            ans += tans
            while popping:
                heappush(mycont,popping.pop(0))
        return ans
