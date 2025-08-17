import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 生成线性数据（y = 2x + 1，加上一点噪声）
np.random.seed(0)
X =  np.random.rand(100, 1) * 10  # 100 个样本，x 在 0~10 之间
y = 2 * X + 1 + np.random.rand(100, 1)  # 添加一些随机噪声


# 2. 训练线性回归模型
model = LinearRegression()
model.fit(X, y)


# 3. 查看模型参数
print("斜率 w =", model.coef_[0][0])
print("截距 b =", model.intercept_[0])


# 4. 预测
X_test = np.linspace(0, 10, 100).reshape(-1, 1)
y_pred = model.predict(X_test)

