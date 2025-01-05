# README

## **Overview**

This project implements a simple linear programming example using Python's `scipy.optimize` library to solve a resource allocation problem. Specifically, it minimizes the cost of allocating delivery vehicles while adhering to capacity constraints. This is a classic optimization problem commonly used in logistics and operations research.

---

## **How It Works**

1. **Objective Function**:
   - The goal is to minimize the total cost of using delivery vehicles. The costs are defined in the vector `c`.

2. **Constraints**:
   - Capacity constraints are defined using matrices `A` and `b`, representing the capacities of the vehicles for each type of item.

3. **Bounds**:
   - Each vehicle allocation must be greater than or equal to 0 (no negative allocations).

4. **Solver**:
   - The `scipy.optimize.linprog` function is used to solve the optimization problem using the `highs` method.

5. **Output**:
   - The result contains the optimal allocation of resources (vehicles) to minimize cost while meeting the constraints.

---

## **Code Example**

```python
from scipy.optimize import linprog

# Objective function coefficients (cost minimization)
c = [50, 70, 30]  # Cost per vehicle

# Constraints (vehicle capacities)
A = [
    [10, 20, 30],  # Item 1
    [15, 25, 35],  # Item 2
]
b = [50, 70]  # Maximum capacity for each vehicle

# Bounds (non-negative allocation)
bounds = [(0, None) for _ in c]

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

print("Optimal allocation:", result.x)