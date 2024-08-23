### [Critical path](https://www.acmicpc.net/problem/1948)

Difficulty : Platinum 5

#### statement
The World Nation is a one-way road with no cycles. However, it is said that countless people set out from a starting city to a destination city to draw a map of the World Nation and explore all possible routes.

The people who drew this map were so friendly that they decided to meet at the destination city after they finished drawing the map. If so, how many hours after leaving the departure city can they all meet? That is, the time it takes for the last person to arrive.

Some people have to run non-stop for a minute to meet at this time. Count the number of roads these people pass by.

The departure city has 0 incoming roads, and the destination city has 0 outgoing roads.


#### Input

The first line contains the number of cities n (1 ≤ n ≤ 10,000), and the second line contains the number of roads m (1 ≤ m ≤ 100,000). From the third line to the m+2 line, the following road information is given. First, the number of the starting city of the road is given, then the number of the destination city, and finally, the time taken to pass the road is given. The time taken to pass the road is a natural number less than or equal to 10,000.

And on the m+3rd line, the departure and arrival cities from which the people drawing the map depart are given.

All cities are reachable from the departure city, and all cities are reachable from the destination city.

#### Output
On the first line, print the time they meet, and on the second line, print the number of roads they must travel without stopping for even one minute.



>**IDEA**
* People who do not take any rest is arriving at the last node with maximum duration.
* The number of loads = the number of different nodes that making the biggest time duration.  



>**How I solve it**

```python

```