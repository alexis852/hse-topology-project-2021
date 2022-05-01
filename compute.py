from simplicial import *
from itertools import permutations 

n = 12
intervals = [2, 3, 3, 4]
Tonn = SimplicialComplex()
for i in range(n):
    Tonn.addSimplex(id = i)
for x in range(n):
    for sigma in permutations(intervals):
        basis = [
            x,
           (x + sigma[0]) % n,
           (x + sigma[0] + sigma[1]) % n,
           (x + sigma[0] + sigma[1] + sigma[2]) % n
        ]
        try:
            Tonn.addSimplexWithBasis(bs = basis)
            print(basis)
        except Exception: # if a simplex is aldeady in Tonn, then nothing to do
            pass

print('Euler characteristic = {}'.format(Tonn.eulerCharacteristic()))
print('Betti numbers: {}'.format(Tonn.bettiNumbers()))
