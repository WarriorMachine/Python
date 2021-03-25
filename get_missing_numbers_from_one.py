def getMissingNumbersFromOne(array : list): #return 0 if nothing miss
		actual, missing, normal = sorted(array), [], []
		if len(actual) < 1: missing.append(0)
		else : [normal.append(x) for x in range(1, actual[-1]+1)]

		for _, no in enumerate(normal):
			if no not in actual: missing.append(no)

		if len(missing) < 1: return None

		return missing
