base_x = int(input("Entrer la valeur de x : "))
exp = int(input("Entrer l'exposant : "))
mod = int(input("Entrer n (ou modulo) : "))

print(f"\n{base_x} |------> {base_x}**{exp}(mod {mod})")
y=1
base_2 = [1,]
base2_accepted_values=[]
x_expo_base2 = []
while y*2 <= exp:
	base_2.append(y*2)
	y*=2
base_2_rev = base_2
base_2_rev.reverse()

for x in base_2_rev:
	y=exp-x
	if y >= 0:
		base2_accepted_values.append(x)
		exp=y

for x in base2_accepted_values:
	y = (base_x**x)%mod
	x_expo_base2.append(y)

print("En base 2\n")
for x in base_2:
	print(x)

print("Valeurs accepté\n")
for x in base2_accepted_values:
	print(x)

produit=1
for x in x_expo_base2:
	produit*=x

produit=produit%mod
print("La reponse finale est : ")
print(f"{produit}(mod {mod})")

