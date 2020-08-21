# Binary search:
Binary Search is an efficient search algorithm that works on sorted arrays. 
Binary Search works on a divide-and-conquer approach. 
More specifically, it compares the middle element of the sorted array to the element it's searching for in order to decide where to continue the search.  

If the target element is larger than the middle element - it can't be located in the first half of the collection so it's discarded. The same goes the other way around.  

### e.g.  
Let us take a sorted list(if the list is not sotrted then use `sort()` method to sort the list)  

list = [1, 2, 3, 5, 7, 8, 9, 10]  

**STEP-1: Dividing the list in two parts:**  
lower position = 0  

upper position (= length of the list - 1 = 8 - 1) = 7  

mid position = (lower position + upper position)//2 = 3  
mid value = 5  

The list got divided into two parts: 1, 2, 3, 5 & 7, 8, 9, 10  

*NOTE: '//' flood division -> gives the value without the decimal part*  

**STEP-2: checking for the result**  
We will compare the mid value with the item to be searched.  

Suppose we are searching 9 in the list, key = 9  

If mid value is equal to the key value then we got our result, the output will be "5"  

If mid value is smaller than the key value, we will take the left part(1, 2, 3, 5) of the list and the right part(7, 8, 9, 10) gets discarded.  
If mid value is greater than the key value, we will take the right part(7, 8, 9, 10) of the list and the right left part(1, 2, 3, 5) gets discarded.  

If we get the left part of the list then lower position will remain the same and the upper position will change, upper position = mid - 1 (i.e. 2nd position).  
If we get the right part of the list then upper position will remain the same and the lower position will change, lower position = mid + 1 (i.e. 4th position).  

No matter which part we get, we will apply step 1 & 2 again and again until we get the desired result.  

In our example we will divide the right part again i.e. 7, 8 & 9, 10  
Here the mid position is 5th and the mid value is 8.  
Since key value(9) is greater than the mid value, we will take the right part i.e. 9, 10  

Now again we will divide the list i.e. 9 & 10  
Here the mid position is 6th and the mid value is 9.  
Since the key value is equal to the mid value, we got our result i.e. **6th position on the list**.


