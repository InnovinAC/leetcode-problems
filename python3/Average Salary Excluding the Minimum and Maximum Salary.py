class Solution:
    def average(self, salary: List[int]) -> float:
        new_list = [a for a in salary if a not in [min(salary), max(salary)]]
        sum_list = 0
        for x in new_list:
            sum_list += x
        return  sum_list/len(new_list)
