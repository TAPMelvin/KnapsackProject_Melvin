import sys
import time

def coin_combination_solver(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_used = [None] * (target + 1)

    for i in range(1, target + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[target] == float('inf'):
        return None

    # Reconstruct the solution
    solution = []
    current = target
    while current > 0:
        coin = coin_used[current]
        solution.append(coin)
        current -= coin

    return solution

def process_line(line):
    parts = line.strip().split(', ')
    problem_size, target = parts[0], int(parts[1])
    coins = [int(x) for x in parts[2:]]
    return problem_size, target, coins

def main():
    for line in sys.stdin:
        start_time = time.time()  # Start timing
        
        problem_size, target, coins = process_line(line)
        solution = coin_combination_solver(coins, target)
        
        end_time = time.time()  # End timing
        execution_time = end_time - start_time  # Calculate execution time
        
        print(f"Problem Size: {problem_size}")
        print(f"Target: {target}")
        print(f"Available coins: {coins}")
        
        if solution:
            print(f"Solution found!")
            print(f"Number of coins used: {len(solution)}")
        else:
            print("No solution found for the given coins and target amount.")
        
        print(f"Execution time: {execution_time:.6f} seconds")  # Display execution time
        print("-" * 50)
        print()  # Add a blank line after each problem's output

if __name__ == "__main__":
    main()