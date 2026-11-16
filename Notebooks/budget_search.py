"""Budget bisection with certificates from a maximum-coverage MIP."""
from dataclasses import dataclass
from math import nan


@dataclass(frozen=True)
class BudgetResult:
    lower: float
    upper: float
    status: str
    non_optimal: int


def solve_coverage(model, budget_constraint, total, budget, *, time_limit=60, gap=0.001):
    """Return incumbent coverage and its upper bound, both as shares."""
    budget_constraint.RHS = budget
    model.setParam("TimeLimit", time_limit)
    model.setParam("MIPGap", gap)
    model.optimize()
    incumbent = model.ObjVal / total if model.SolCount else nan
    return incumbent, model.ObjBound / total


def search_budget(solve, target, max_budget, tolerance=0.05, *, optimal_status):
    """Find a budget bracket. An unresolved solve never moves either bound."""
    if not 0 < target <= 1 or max_budget < 0 or tolerance <= 0:
        raise ValueError("Use a target in (0, 1], a nonnegative budget and positive tolerance.")

    non_optimal = 0

    def classify(budget):
        nonlocal non_optimal
        incumbent, bound, status = solve(budget)
        non_optimal += status != optimal_status
        if incumbent >= target:
            return True
        if bound < target:
            return False
        return None

    at_cap = classify(max_budget)
    if at_cap is False:
        return BudgetResult(max_budget, nan, "above_cap", non_optimal)
    if at_cap is None:
        return BudgetResult(0.0, nan, "unresolved", non_optimal)

    low, high = 0.0, max_budget
    while high - low > tolerance:
        midpoint = (low + high) / 2
        feasible = classify(midpoint)
        if feasible is None:
            return BudgetResult(low, high, "unresolved", non_optimal)
        if feasible:
            high = midpoint
        else:
            low = midpoint
    return BudgetResult(low, high, "bracketed", non_optimal)
