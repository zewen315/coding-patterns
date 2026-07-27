# Memoization vs DP

| Memoization (Top-down)     | DP (Bottom-up)         |
| -------------------------- | ---------------------- |
| Recursion + Cache          | Iteration + Table      |
| Start from the answer      | Start from base cases  |
| Compute only needed states | Compute all states     |
| Easier to write            | Usually more efficient |
| Uses recursion stack       | No recursion stack     |

```python
memo = {}

def fib(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

# DP vs Greedy

| Dynamic Programming | Greedy |
|---------------------|---------|
| Explore all possibilities | Make the best local choice |
| Compares multiple previous states | Uses only the current best choice |
| Guarantees the global optimum | Requires the greedy-choice property |
| Usually uses a `dp[]` table | Usually uses variables / sorting |
| Time: O(n²) or more | Often O(n) or O(n log n) |

## Use DP when
- The answer depends on multiple previous states.
- You need to compare different choices.
- Local optimum does NOT always lead to the global optimum.

Examples:
- House Robber
- Coin Change
- Knapsack
- Longest Increasing Subsequence

## Use Greedy when
- A locally optimal choice is always globally optimal.
- Once a decision is made, you never need to reconsider it.

Examples:
- Jump Game
- Merge Intervals
- Non-overlapping Intervals
- Meeting Rooms
- Huffman Coding

## Rule of Thumb

Greedy:
> Can I safely make the best choice now without regretting it later?

DP:
> Do I need to compare multiple previous states to guarantee the optimal answer?