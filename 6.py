# Devuelve todos los subconjuntos de L que suman exactamente n
# L = lista de enteros positivos
# n = entero
def subconjuntos_suma_exacta(L, n):
	l = len(L)
	if l == 0:
		return []
	elif l == 1:
		return L[0] == n
	else:
		# x es parte del subconjunto final
		x = L[0]
		xs = L[1:-1]
		subconjuntos_con_x = subconjuntos_suma_exacta(xs, n-x)

		# x no es parte del subconjunto final
		subconjuntos_sin_x = subconjuntos_suma_exacta(xs, n)
		return subconjuntos_con_x + subconjuntos_sin_x