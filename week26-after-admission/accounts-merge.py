class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_name = {}
        reps = {}

        for account in accounts:
            name = account[0]

            for mail in account[1:]:
                mail_to_name[mail] = name

                reps[mail] = account[1] 
        

        def find_rep(mail):
            if reps[mail] == mail:
                return mail
            else:
                parent = reps[mail]
                rep = find_rep(parent)
                reps[mail] = rep

                return rep
        
        def union(mail1, mail2):
            rep1 = find_rep(mail1)
            rep2 = find_rep(mail2)

            reps[rep2] = rep1
        
        for account in accounts:
            for mail in account[1:]:
                union(account[1], mail)
        
        merged = defaultdict(list)
        for account in accounts:
            for mail in account[1:]:
                merged[find_rep(mail)].append(mail)
        
        for rep in merged.keys():
            merged[rep] = list(set(merged[rep]))
            merged[rep].sort()
            merged[rep].insert(0, mail_to_name[rep])
        
        return list(merged.values())


        