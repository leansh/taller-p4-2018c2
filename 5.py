def recorrido_del_caballo(A, x, y, i):
	A[x][y] = i+1
	movimientos = obtener_movimientos(x, y)
	movimientos_legales = [mov for mov in movimientos if A[mov.x][mov.y] != 0] # los no repetidos
	cant_mov_legales = len(movimientos_legales)
	if cant_mov_legales == 0:
		if i == 63:
			#termine exitosamente
			return true
		else:
			# algo estuvo mal, entonces deshago un paso y pruebo las otras alternativas
			A[x][y] = 0
			return false
	else:
		for mov in movimientos_legales:
			res = recorrido_del_caballo(A, mov.x, mov.y, i+1)
			if res:
				return true # si alguno fue exitoso, retorno ahi nomas
		return false # ninguno fue exitoso en este camino
