prev2 = 0
prev1 = 1
print(prev2)
print(prev1)
for fibo in range(12):
    new_fibo = prev2+ prev1
    prev2 = prev1
    prev1 = new_fibo
    print(new_fibo)

