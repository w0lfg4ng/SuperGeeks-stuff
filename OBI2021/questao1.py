N = int(input())
B = []
for x in range(N):
  A = int(input())
  B.append(A)
  if(B[0] + N-1 == N and B[1] + N-2 == N):
    print("S")
