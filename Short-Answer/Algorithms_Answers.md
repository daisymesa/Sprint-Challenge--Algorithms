#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The run time of this snippet would be O(n). One operation needs to be done, and the time will increase as n increases or decreases.

b) The run time of this snippet would be O(n^3). Three operations need to be done and as the size of the input increases, the runtime wil grow at a slightly faster rate. The nested loop makes this solution less scalable.

c) The run time of this snippet would be O(n) (linear). The time will increase as the size of the input/bunnies increases or decreases.

## Exercise II

-   If n represents the number of stories, we need to divide n by 2, to find the mid point in the floors.
-   If the egg is thrown off this mid point, and it breaks:
-   We need to find the new mid point, in the lower floors.
-   If the egg did not break:
-   We need to find a new mid point in the upper floors.
-   We can repeat these steps until we find the value of f.

This would solve the problem using a binary search, which has a time complexity of O(log n).
