def inverseModulo(b,n):
	A1=1
	A2=0
	A3=n
	B1=0
	B2=1
	B3= b%n
	Q=0
	print(f"L'inverse de {b}(mod{n})\n")
	print(f"\t{'Q' :<5}|{'A1' :^10}|{'A2' :^10}|{'A3' :^10}|{'B1' :^10}|{'B2':^10}|{'B3':^10}")
	print("\t------------------------------------------------------------------------|")
	print(f"\t{Q :<5}|{A1 :^10}|{A2 :^10}|{A3 :^10}|{B1 :^10}|{B2:^10}|{B3:^10}")
	print("\t------------------------------------------------------------------------|")
	while B3 !=1:
		Q=int(A3/B3)
		T1,T2,T3=(A1-(Q*B1)),(A2-(Q*B2)),(A3-(Q*B3))
		A1,A2,A3=B1,B2,B3
		B1,B2,B3=T1,T2,T3
		print(f"\t{Q :<5}|{A1 :^10}|{A2 :^10}|{A3 :^10}|{B1 :^10}|{B2:^10}|{B3:^10}")
		print("\t------------------------------------------------------------------------|")
	print("\n")
	inverse=B2%n
	print(f"L'inverse de {b}(mod {n}) = {inverse}")

	return inverse