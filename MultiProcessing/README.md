## Multiprocessing :
Multiprocessing refers to the ability of a system to support more than one processor at the same time.  
Applications in a multiprocessing system are broken to smaller routines that run independently.  
The operating system allocates these threads to the processors improving performance of the system.  
In Python, the multiprocessing module includes a very simple and intuitive API for dividing work between multiple processes.

### When to use multiprocessing ? :
Multiprocessing is used in CPU bound programs.  
Problems that require heavy CPU computation and spend little time waiting for external events are effective with multiprocessing.

### When not ot use multiprocessing ? :
In I/O bound programs multithreading will make the execution much faster as compared to multiprocessing.



