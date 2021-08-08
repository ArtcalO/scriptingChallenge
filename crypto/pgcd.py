x=13298020
b=2549
mod=1
while mod !=0 :
	mod = x%b
	x,b=b,mod

print("PGCD est : ",x, b)
