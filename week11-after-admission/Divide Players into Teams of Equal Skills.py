class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        return divide_players(skills)

        
def divide_players(skills):
    if len(skills) == 0:
        return -1
    
    skills.sort()
    
    left  = 0
    right = len(skills)-1
    
    sum_chemistry = 0
    team_skill = skills[left] + skills[right]
    
    for _ in range(len(skills)//2):
        this_team_skill = skills[left] + skills[right]
        
        if this_team_skill != team_skill:
            return -1
        
        sum_chemistry += skills[left]*skills[right]
        
        left += 1
        right -= 1
    
    return sum_chemistry
        
#15min
#1sub