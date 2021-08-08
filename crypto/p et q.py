from math import *
n=230651
p=0
q=0
sqrt_n=int(sqrt(n))
for x in range(1,sqrt_n):
	if n%x==0:
		p=x
q=int(n/p)
print(f"Dans N={n} : P={p} et Q={q}")
n=int(p*q)
print(f"Produit P:{p} et Q:{q} = {n}")