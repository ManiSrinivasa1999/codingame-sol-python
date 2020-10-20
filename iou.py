"""
The Intersection over Union (IoU) is known to be a
good metric for measuring overlap between two bounding boxes or masks.

It is calculated as Area of the intersection / Area of the union.

You will receive two bounding boxes:
- x_1, y_1, w_1, h_1
- x_2, y_2, w_2, h_2
where x and y represent the top-left coordinat
 and w and h represent the width and the height.

Compute the IoU!

Warning:
- The test cases are defined in a way that no
approximation are required (e.g., no result is 0.33333333...).
- Get rid of trailing 0s (1.0 should be 1).
Input
Line 1: x_1, y_1, w_1, h_1
Line 2: x_2, y_2, w_2, h_2
Output
Line 1: The IoU
Constraints
0 ≤ x_1, y_1, x_2, y_2 < 1000
0 < w_1, h_1, w_2, h_2 < 1000
Example
Input
1 1 2 2
2 1 2 3
Output
0.25
"""
