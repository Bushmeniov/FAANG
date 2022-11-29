from typing import Tuple, Text, Union, Any, Callable, List, Dict, Deque, OrderedDict
import enum
import sys

minus_max = - sys.maxsize

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array

class ExpectedOutput():
    def __init__(self, value):
        self.value = value

class SolutionData():
    def __init__(self, input : Dict, expected_outputs : List[ExpectedOutput]):
        self.input = input
        self.expected_outputs = expected_outputs

class BaseSolution():

    def __init__(self, name, func : Callable):
        self.name = name
        self.func = func

    def solve(self, input : Dict):
        return self.func(self, **input)

class SolutionHelper():

    def run_assert(self, solution : BaseSolution, data : SolutionData):
        try:
            from copy import deepcopy
            result = solution.solve(deepcopy(data.input))

            for exp_out in data.expected_outputs:
                if result == exp_out.value:
                    return True
            else:
                raise AssertionError

        except AssertionError:
            print(f"Solution : {solution.name}, status = FAILURE"
                  f"\ninput={data.input}"
                  f"\nresult={result}"
                  f"\nexpected_output={[exp_out.value for exp_out in data.expected_outputs]}")
            raise AssertionError

helper = SolutionHelper()



