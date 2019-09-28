# Python Concurrency
Task on python cuncurrency

Tested on copying `1000` `5mb` files from source directory to destionation directory using threads, processes 
and just a single thread

* Time results were measured. In concurrent copy tasks, 4 workers were used per pool.

| Mode  | Time|
| ------------- | ------------- |
| Processes  | 5.03 seconds  |
| Threads  | 8.17 seconds  |
| Single Thread  | 14.97 seconds  |


* Same task with 8 workers for each pool

| Mode  | Time|
| ------------- | ------------- |
| Processes  | 5.03 seconds  |
| Threads  | 6.06 seconds  |
| Single Thread  | not-measured |

As we can observe, processes outshine threads in terms of performance because they always run at the same time, while with threads,
it is not guaranteed that execution always happens in parallel. Threads can just run in overlapping periods of time which does not
necessarily mean always running in parallel. However, as we start to use more processes and more threads, we can see that results
become tighter.
