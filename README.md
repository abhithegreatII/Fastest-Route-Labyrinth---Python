# Fastest-Route-Labyrinth---Python
A maze consists of Passables and Unpassables... Can you find the shortest path out of the Labyrinth?


## How to Run

Input of the function are the column and row of the start and likewise for your chosen endpoint of the labyrinth.
For example, abstand((0,0),(2,14)):
  This would be the starting point (column=0,row=0) and end point (column=2,row=14).
  The output of the above example should be: 18; which is the shortest of all paths from start to end.
  Beware that this code also prints each row to see how the labyrinth looks like after the breadth first search has completed.

### Create your own Labyrinth
Open the dat.py file and create a labyrinth of Passables (P) and Unpassables(U). You can imagine Unpassables as walls and the Passables as open paths.
Make sure that each column and row have the same amount of entries. (So each column could have 6 entries, and each row could have 10 entries).
