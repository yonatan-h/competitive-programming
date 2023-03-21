class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxLength = 0
        self.concatedStrings = set()
        self.arr = arr

        self.backTrack(-1)

        return self.maxLength

    def backTrack(self, last_added_index):

        self.maxLength = max(self.maxLength, len(self.concatedStrings))

        for i in range(last_added_index +1, len(self.arr)):
            if self.isCandidate(self.arr[i]):

                chunk_set = set(list(self.arr[i]))
                self.concatedStrings.update(chunk_set)

                self.backTrack(i)

                self.concatedStrings.difference_update(chunk_set)


    def isCandidate(self, string):
        chunk_set = set(list(string))
        if len(string) != len(chunk_set):
            return False 

        if self.concatedStrings.intersection(chunk_set):
                return False

        return True



