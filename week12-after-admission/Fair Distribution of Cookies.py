class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies.sort(reverse=True)
        self.cookies = cookies

        self.children = [0]*k
        self.fairest = float("inf")

        self.distribute(0)
        return self.fairest

    def distribute(self, bag_index):

        if bag_index == len(self.cookies):
            most_cookies = max(self.children)
            self.fairest = min(self.fairest, most_cookies)
            return

        bag = self.cookies[bag_index]
        for i in range(len(self.children)):
            if self.children[i] + bag >= self.fairest:
                continue

            self.children[i] += bag
            self.distribute(bag_index + 1)
            self.children[i] -= bag

#6sub
#40min
