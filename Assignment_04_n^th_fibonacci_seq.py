# Function to find the n-th Fibonacci number using Tabulation (Dynamic Programming)
def fib(n):
    if n<=1:
        return n
    dp = [0 , 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2]) 
    return dp[n]
print(f"The fibonacci number is : {fib(10)}")

#Output
The fibonacci number is : 55

# Function to find the n-th Fibonacci number using Memorization (Dynamic Programming)
memo = {}
def fib_s(n):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_s(n-1) + fib_s(n-2)
    return memo[n]

print(f"The fibonacci number is :{fib(15)} ")

#Output
The fibonacci number is :610 
