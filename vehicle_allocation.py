from scipy.optimize import linprog

# 目的関数の係数（コスト最小化）
c = [50, 70, 30]  # 各車両のコスト

# 制約条件（車両の容量）
A = [
    [10, 20, 30],  # 荷物1
    [15, 25, 35],  # 荷物2
]
b = [50, 70]  # 各車両の最大容量

# 0以上の制約
bounds = [(0, None) for _ in c]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

print("最適な割り当て:", result.x)