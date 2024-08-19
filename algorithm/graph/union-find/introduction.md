# Union Find

Union Find algorithm consists of Union function and Find function.

>**Union function**

Normally, it receives two values for the function. It decides which one is representing node. 
<br> A more bigger value is the index of representing node in the list and a more smaller one is value. For example, there is the list called lis and a = 1, b = 3 are given. After union function, the list is described as lis[b] = a

Basically, Union function is to compare values and to set the representing values based on the order. 

>**Find function**

 Find function is the most important part in the Union find algorithm. 
 <br> There are steps in the union function
 1. Check if the value in the list equals the index of the value in the list.

    1-1. if value = index, return the value

    1-2. if value != index, it is going back to the index that had different index as the value given.
    <br> It ultimatley finds the index is the same as the value of the index in the list. 
    <br> For example
```python
    def find(v):
        if v == list[v]:
            return v:
        else:
            list[v] = find[list[v]]
            return list[v]
    # in this recursive function, function is like stack and  when recursive function is called, it goes back to previous function with the value of current function.  
```
>**[Best example to understand Union find easily](https://github.com/yeasung240/algorithm/blob/main/algorithm/graph/union-find/problem-1.md)**





        
    
    
    



