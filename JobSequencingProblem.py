from base.helpers import BaseSolution, SolutionHelper, SolutionData, List, helper, ExpectedOutput, Tuple, swap, minus_max
import math
from typing import Set


class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f'({self.taskId}, {self.deadline}, {self.profit})'

    def __eq__(self, o: object) -> bool:
        return self.taskId == o.taskId and self.deadline == o.deadline and self.profit != o.profit

class Solution(BaseSolution):

    def scheduleJobs(self, jobs: List[Tuple]) -> Set[int]:
        jobs : List[Job] = [Job(*job) for job in jobs]
        deadline_job_list : List[Job] = [None] * len(jobs)

        sorted_jobs_by_profit = sorted(jobs, key=lambda job: (job.profit, job.deadline), reverse=True)
        for job in sorted_jobs_by_profit:
            for i in reversed(range(0, min(job.deadline, len(deadline_job_list)))):
                if deadline_job_list[i] is None:
                    deadline_job_list[i] = job
                    break

        return {job.taskId for job in deadline_job_list if job is not None}

__solutions = [
    Solution(name="scheduleJobs", func=Solution.scheduleJobs)
]

__data = [

    SolutionData(
        input={"jobs" : [(1, 9, 15),
                              (2, 2, 2),
                              (3, 5, 18),
                              (4, 7, 1),
                              (5, 4, 25),
                              (6, 2, 20),
                              (7, 5, 8),
                              (8, 7, 10),
                              (9, 4, 12),
                              (10, 3, 5)]},
        expected_outputs=[ExpectedOutput({1, 3, 4, 5, 6, 7, 8, 9})]
    )

]

for solution in __solutions:
    for data in __data:
        helper.run_assert(solution=solution,
                          data=data)
else:
    print("OK!")