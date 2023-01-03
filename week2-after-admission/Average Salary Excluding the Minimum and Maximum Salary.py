class Solution:
    def average(self, salary: List[int]) -> float:
        return average_in_between(salary)

def average_in_between(salaries):

    if len(salaries)==1:
        return 0

    min_salary = salaries[0]
    max_salary = salaries[0]
    sum = 0

    for salary in salaries:
        min_salary = min(min_salary, salary)
        max_salary = max(max_salary, salary)
        sum += salary
    
    sum -= min_salary
    sum -= max_salary
    print(sum)
    average = sum/(len(salaries)-2)
    return average

#7min
#1sub