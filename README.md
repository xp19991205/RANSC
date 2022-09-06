py-ransac
=========

python implemetation of RANSAC algorithm with a line fitting example and a plane fitting example.
## 这个算法的主要思路
1. 每次迭代，从数据集中随机选择一部分数据，用于拟合模型（二元，也就是直线），每次根据A+By<Shread这个标准来判断内点，不断迭代，找到最大的内点个数。
作为最终的最优线性模型