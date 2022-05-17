# python3

from collections import namedtuple
import numpy as np
import time

import heapq


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


class Worker:
    def __init__(self, id_, working_time = 0):
        self.id = id_
        self.working_time = working_time
        
    def __lt__(self, other):
        if self.working_time == other.working_time:
            return self.id < other.id
        return self.working_time < other.working_time
    
    def __gt__(self, other):
        if self.working_time == other.working_time:
            return self.id > other.id
        return self.working_time > other.working_time
        
class Jqueue:
    def __init__(self,n_workers, jobs):
        self.n_workers = n_workers
        self.jobs = jobs
        self.size = len(self.jobs)
        self.result = []
        
    def print_work(self):
        # print results
        for worker_id , start_time in self.result:
            print(worker_id, start_time)
    
    def assign_work(self):
        # assign works to workers        
        self.worker_queue = [Worker(i) for i in range(self.n_workers)]
        for j in self.jobs:
            worker = heapq.heappop(self.worker_queue)
            
            self.result.append((worker.id , worker.working_time))
            
            worker.working_time += j
            heapq.heappush(self.worker_queue, worker)

    def solve(self):
        self.assign_work()
        self.print_work()
        

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    work = Jqueue(n_workers, jobs)    
    work.solve()
    
    # result = assign_jobs_naive(n_workers,jobs)
    # for i in result:
    #     print(i.worker,i.started_at)
    

if __name__ == "__main__":
    main()
    

