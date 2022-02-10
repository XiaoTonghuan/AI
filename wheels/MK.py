from scipy.stats import norm
import numpy as np


def mk(x, alpha=0.1):  # 0<alpha<0.5 1-alpha/2为置信度
    n = len(x)

    # 计算S的值
    s = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            s += np.sign(x[i] - x[j])

    # 判断x里面是否存在重复的数，输出唯一数队列unique_x,重复数数量队列tp
    unique_x, tp = np.unique(x, return_counts=True)
    g = len(unique_x)

    # 计算方差VAR(S)
    if n == g:  # 如果不存在重复点
        var_s = (n * (n - 1) * (2 * n + 5)) / 18
    else:
        var_s = (n * (n - 1) * (2 * n + 5) - np.sum(tp * (tp - 1) * (2 * tp + 5))) / 18

    # 计算z_value
    if n <= 10:  # n<=10属于特例
        z = s / (n * (n - 1) / 2)
    else:
        if s > 0:
            z = (s - 1) / np.sqrt(var_s)
        elif s < 0:
            z = (s + 1) / np.sqrt(var_s)
        else:
            z = 0

    # 计算p_value，可以选择性先对p_value进行验证
    p = 2 * (1 - norm.cdf(abs(z)))

    # 计算Z(1-alpha/2)
    h = abs(z) > norm.ppf(1 - alpha / 2)

    # 趋势判断
    if (z < 0) and h:
        trend = 'decreasing'
    elif (z > 0) and h:
        trend = 'increasing'
    else:
        trend = 'no trend'

    return trend

a=[9.1,8.74,9.28,7.44]
print(mk(a))