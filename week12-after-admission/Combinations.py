class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.combinations = []

        self.add_combination([])
        return self.combinations


    def add_combination(self, cur_comb):
        last_appended = cur_comb[-1] if cur_comb else 0

        if len(cur_comb) == self.k:
            self.combinations.append(cur_comb[:])
            return

        missing_nums = self.k - len(cur_comb) 
        addable_nums = self.n - last_appended
        if missing_nums > addable_nums:
            return

        for right_num in range(last_appended+1, self.n+1):
            cur_comb.append(right_num)
            self.add_combination(cur_comb)
            cur_comb.pop()

#10sub
#120min