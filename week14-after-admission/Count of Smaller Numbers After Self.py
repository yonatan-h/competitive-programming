class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.smallers = [0]*len(nums)
        numies = [(nums[i], i) for i in range(len(nums))]

        self.reverse_sort(numies)
        return self.smallers
        

    def reverse_sort(self, numies):
        if len(numies) <= 1: return numies

        mid = len(numies)//2
        lefties = self.reverse_sort(numies[:mid])
        righties = self.reverse_sort(numies[mid:])

        return self.merge(lefties, righties)


    def merge(self, lefties, righties):
        lefties = deque(lefties)
        righties = deque(righties)
        merged = []

        while lefties or righties:
            if lefties: left, left_index = lefties[0]
            else: left = -float("inf")

            if righties: right, right_index = righties[0]
            else: right = -float("inf")

            if left > right:
                self.smallers[left_index] += len(righties)
                merged.append(lefties.popleft())
                
            else:
                merged.append(righties.popleft())
                

        return merged
                


                


