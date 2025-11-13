def visualize_recurrence(n, level=0):
    """
    Visualize T(n) = 2T(n/2) + n
    Prints the cost at each recursion level
    """
    indent = "  " * level  # for structure
    
    if n <= 1:  # base case
        print(f"{indent}T({n}) = 1")
        return 1
    
    # cost at this level
    cost_at_level = n
    print(f"{indent}T({n}) = 2*T({n}//2) + {n}")
    
    
    left = visualize_recurrence(n // 2, level + 1)
    right = visualize_recurrence(n // 2, level + 1)
    
    total = left + right + cost_at_level
    print(f"{indent}Total cost for T({n}) = {total}")
    return total


total_cost = visualize_recurrence(8)
print("\nTotal T(8) =", total_cost)
