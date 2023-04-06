n = int(input())

if n == 0:
    print(0)
else:
    sequence = [0] * (n+1)
    sequence[1] = 1
    sum = 0
    for i in range(2, n+1):
        sequence[i] = sequence[i-1] + sequence[i-2]
      
    for i in range(n):
      sum += sequence[i]
    print(sequence[n])
# print(sequence)
