import random

def run_ransac(data, estimate, is_inlier, sample_size, goal_inliers, max_iterations, stop_at_goal=True, random_seed=None):
    best_ic = 0
    best_model = None
    random.seed(random_seed)
    # random.sample cannot deal with "data" being a numpy array
    data = list(data)
    for i in range(max_iterations):
        s = random.sample(data, int(sample_size)) #从原始数据中选择n个样本点
        m = estimate(s) #根据样本点估计模型参数(主要步骤，利用SVD分解中的V矩阵最后一行的值，就是模型参数)
        ic = 0 #计算模型的内点个数主要通过[c1 c2 c3][[x1,x2,x3],[y1,y2,y3],[1,1,1]]的点集实现
        for j in range(len(data)): #遍历所有的样本点，找出内点
            if is_inlier(m, data[j]): #模型的主要目的是为了找到使得内点最多的模型
                ic += 1

        print(s)
        print('estimate:', m,)
        print('# inliers:', ic)

        if ic > best_ic:
            best_ic = ic
            best_model = m
            if ic > goal_inliers and stop_at_goal:
                break
    print('took iterations:', i+1, 'best model:', best_model, 'explains:', best_ic)
    return best_model, best_ic
