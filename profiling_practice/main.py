import time
import cProfile
import pstats
from io import StringIO

class CodeOptimizer:
    def __init__(self):
        self.data = list(range(1,10000))

    @staticmethod
    def innef():
        result = []
        for i in range(1,10000):
            result.append(i**2)
        return result

    @staticmethod
    def optimized():
        return [i**2 for i in range(1,10000)]

    @staticmethod
    def profile_func(func):
        print(f'\nProfiled funtioncs: {func.__name__}')
        pr = cProfile.Profile()
        pr.enable()
        func()
        pr.disable

        s = io.StringIO
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats(10)
        print(s.getvalue())

    @staticmethod
    def real_life_example():
        employees = [
            {'name': 'Bob', 'salary': 120000},
            {'name': 'Alice', 'salary': 80000},
            {'name': 'Charlie', 'salary': 100000},
            {'name': 'David', 'salary': 95000},
        ]
        start_time = time.time()
        high_earner = []
        for employee in employees:
            if employee['salary'] > 100000:
                high_earner.append(employee)
        end_time = time.time()
        print('Slow result:', high_earner, 'Time ', end_time - start_time)
        start_time = time.time()
        high_earner = [employee for employee in employees if employee['salary'] > 100000]
        end_time = time.time()
        print('Optimized result:', high_earner, 'Time ', end_time - start_time)
        
    def big_o():
        print('\nComparison O(n^2) and O(n):')
        def quadratic_complexity(data):
            pairs = []
            for i in data:
                for j in data:
                    pairs.append((i,j))
            return pairs
        
        def linear_complexity(data):
            return [i*2 for i in data]
        
        data = list(range(1,1000))
        start_time = time.time()
        quadratic_complexity(data)
        print()
    
    def run_class(self):
        self.real_life_example()
        self.big_o()

if __name__ == "__main__":
    lesson = CodeOptimizer()
    lesson.run_class()

