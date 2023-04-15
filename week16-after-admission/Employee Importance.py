"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.sum_importance = 0
        self.employees= {}
        for employee in employees:
            self.employees[employee.id] = employee

        self.count_importance(id)
        return self.sum_importance
        
    def count_importance(self, id):
        self.sum_importance += self.employees[id].importance

        for sub_id in self.employees[id].subordinates:
            self.count_importance(sub_id)

