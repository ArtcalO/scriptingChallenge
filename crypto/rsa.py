import inverse_modulo 
p = int(input("Entrer la valeur de p : "))
q = int(input("Entrer la valeur de q : "))
e = int(input("Entrer la valeur de e : "))

n = q*p
lambda_n = (q-1)*(p-1)
inverse = inverse_modulo.inverseModulo(e,lambda_n)
	

print(f"n={n}")
print(f"lambda_n={lambda_n}")
print(f"e={e}")

print("Clé publique")
print(f"2 nombres : n = {n}, e={e}")

print("Clé privé")
print(f"2 nombres : n = {n}, d={inverse}")