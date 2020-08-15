## Multithreading :
A thread is a separate flow of execution. This means that your program will have two things happening at once.  
But the different threads do not actually execute at the same time: they merely appear to.  
The threads may be running on different processors, but they will only be running one at a time.

### When to use multithreading ? :
Multithreading is used in IO (input-output) bound programs.  
Tasks that spend much of their time waiting for external events are generally good candidates for threading.

### When not to use multithreading ? :
Multithreading shouldn't be used in CPU bound programs as it may slow down the program instead.  
Problems that require heavy CPU computation and spend little time waiting for external events might not run faster at all.  

