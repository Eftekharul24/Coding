#Python: Using task algorithm

from fractions import Fraction as Fr

def bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0] # (which is Bn)

bn = [(i, bernoulli(i)) for i in range(61)]
bn = [(i, b) for i,b in bn if b]
width = max(len(str(b.numerator)) for i,b in bn)
for i,b in bn:
    print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))


#Python: Optimised task algorithm


from fractions import Fraction as Fr
def bernoulli2():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
        yield A[0] # (which is Bm)
        m += 1

bn2 = [ix for ix in zip(range(61), bernoulli2())]
bn2 = [(i, b) for i,b in bn2 if b]
width = max(len(str(b.numerator)) for i,b in bn2)
for i,b in bn2:
    print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))