# GIL (Global interpreter lock)
First lets talk about how the python delelopement got to the point of introducing the infemous GIL to the python programming.  
So what led to the introduction of GIl in python, it was **thread**.  
We will talk about the problem created by threads in a while but first take a look at the concept of threads.  
Python threading allows you to have different parts of your program run concurrently and can simplify your design.  
If you’ve got some experience in Python and want to speed up your program using threads, then threading can be very useful  
(it some cases(CPU bound programs) it may slow down the execution time)

*NOTE: A thread is a separate flow of execution. This means that your program will have two things happening at once.  
       But the different threads do not actually execute at the same time: they merely appear to.*  
       
**REFERENCE COUNTING :**  
                                          a                    b
