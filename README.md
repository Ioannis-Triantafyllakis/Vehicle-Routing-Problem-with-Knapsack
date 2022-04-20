# Vehicle-Routing-Problem-with-Knapsack
In this project, i find the optimal routes of **5 cargo trucks** starting from a **cental warehouse**.</br> 
</br>
The algorithms used in this project are the **Vehicle Routing Problem** with the **Minimum Insertions** method and the **Knapsack Problem**.</br>
</br>
In every route, each truck serves a number of customers, and has a maximum "serving" capacity. Each truck also chooses which customers to serve according to a profit to cost ratio (The knapsack problem) since not all customers can be served. </br>
</br>
When the final solution is found, it gets further improved with a **Variable Neighborhood Descent Algorithm** (which includes **Swap Move** and **Relocation Move** of the customers already chosen). The aim of VND is to decrease the cost of the exisiting solution.</br>
</br>
In the following .png (MinIns.png), the 5 routes of the last iteration can be seen. Still, there are many overlaps, so the routes will be optimized with a VND algorithm</br>
![Routes after last iteration](https://github.com/Ioannis-Triantafyllakis/Vehicle-Routing-Problem-with-Knapsack/blob/main/MinIns.png) </br>
</br>
In the following .png (final_vnd.png), the 5 routes after the Relocation Moves and Swap Moves that the Variable Neighborhood Algorithm implemented can be seen. It can easily be seen that overlaps do not exist, and while having the same profit as we initially had, the cost is significantly lower.</br>
![Routes after VND](https://github.com/Ioannis-Triantafyllakis/Vehicle-Routing-Problem-with-Knapsack/blob/main/final_vnd.png) </br>
</br>
As the .png above (final_vnd.png) is the final solution, it is important to know how much we managed to lower the cost by using the VND algorithm, while keeping the same profit. In the following .png (SearchTrajectory.png) we can see that after 21 iterations, the cost (objective function) was lowered from aprox. 740, to around 680.</br>
![Search trajectory](https://github.com/Ioannis-Triantafyllakis/Vehicle-Routing-Problem-with-Knapsack/blob/main/SearchTrajectory.png) </br>
</br>
At last, in the following .png (output.png) we can see the algorithm's output in the console. At first, there are the 5 routes (from MinIns.png) without any optimization, and then after 14 Relocation Moves and 7 Swap Moves from the VND algorithms, we get the final solution (5 routes) which has significantly lower cost (683 instead of the initial cost of 740)</br>
![Console output](https://github.com/Ioannis-Triantafyllakis/Vehicle-Routing-Problem-with-Knapsack/blob/main/output.PNG) </br>
