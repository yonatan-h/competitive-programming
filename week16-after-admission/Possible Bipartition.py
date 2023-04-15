class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        self.graph = defaultdict(list)
        for dislike in dislikes:
            disliker = dislike[0]
            disliked = dislike[1]
            self.graph[disliker].append(disliked)
            self.graph[disliked].append(disliker)

        self.group1 = set()
        self.group2 = set()

        for person in list(self.graph.keys()):
            if person in self.group1: continue
            if person in self.group2: continue

            has_joker = self.groupify(person, True)
            print(self.group1)
            if has_joker: return False

        return True

    def groupify(self, person, in_1):
        if in_1:
            self.group1.add(person)
        else:
            self.group2.add(person)


        if person in self.group1 and person in self.group2:
            return True
        
        opposite_group = self.group2 if in_1 else self.group1
        for disliked in self.graph[person]:
            if disliked in opposite_group:
                continue
            
            has_joker = self.groupify(disliked, not in_1)
            if has_joker: return True
            

        
