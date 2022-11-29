from base.helpers import BaseSolution, SolutionHelper, SolutionData, List, helper, ExpectedOutput, Tuple, swap, minus_max
import math
from typing import Set


class Solution(BaseSolution):

    def rec(self, nums: list, n: int, total_1: int, total_2: int, total_3: int,
            set_1, set_2, set_3):

        if total_1 == 0 and total_2 == 0 and total_3 == 0:
            return True

        if n < 0:
            return False

        is_done = False
        if total_1 - nums[n] >= 0:
            is_done = self.rec(nums=nums, n=n - 1, total_1=total_1 - nums[n], total_2=total_2, total_3=total_3, set_1=set_1,
                               set_2=set_2, set_3=set_3)
            if is_done:
                set_1.add(nums[n])

        if not is_done and total_2 - nums[n] >= 0:
            is_done = self.rec(nums=nums, n=n - 1, total_1=total_1, total_2=total_2 - nums[n], total_3=total_3, set_1=set_1,
                               set_2=set_2, set_3=set_3)
            if is_done:
                set_2.add(nums[n])

        if not is_done and total_3 - nums[n] >= 0:
            is_done = self.rec(nums=nums, n=n - 1, total_1=total_1, total_2=total_2, total_3=total_3 - nums[n], set_1=set_1,
                               set_2=set_2, set_3=set_3)
            if is_done:
                set_3.add(nums[n])

        return is_done

    def partition(self, S: List[int]) -> List[List[int]]:
        nums_sum = sum(S)
        total_per_partition = nums_sum // 3

        set_1, set_2, set_3 = set(), set(), set()

        if not nums_sum % 3 == 0:
            return None

        ret = self.rec(nums=S,
                        n=len(S) - 1,
                        total_1=total_per_partition,
                        total_2=total_per_partition,
                        total_3=total_per_partition,
                        set_1=set_1,
                        set_2=set_2,
                        set_3=set_3
                        )


        if ret:
            print(f"DONE : {set_1}, set_2={set_2}, set_3={set_3}")

        return ret



__solutions = [
    Solution(name="partition", func=Solution.partition)
]

__data = [

    SolutionData(
        input={"S": [7, 3, 2, 1, 5, 4, 8]},
        expected_outputs=[
            ExpectedOutput(True)
        ]
    )
]

for solution in __solutions:
    for data in __data:
        helper.run_assert(solution=solution,
                          data=data)
else:
    print("OK!")