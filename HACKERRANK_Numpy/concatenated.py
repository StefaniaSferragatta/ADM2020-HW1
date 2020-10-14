import numpy

N,M,P = map(int,input().split())
p_cols1 =numpy.array([input().split() for _ in range(N)],int)
p_cols1.shape = (N,P)

p_cols2 =numpy.array([input().split() for _ in range(M)],int)
p_cols2.shape = (M,P)

concatenated = numpy.concatenate((p_cols1, p_cols2), axis = 0)
print(concatenated)
