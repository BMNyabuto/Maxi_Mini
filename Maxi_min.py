def find_max_min(ArrayValues):
 	Result = []
 	if isinstance(ArrayValues, list) == True:
 		ArrayValues.sort()
 		minValue = ArrayValues[0]
 		maxValue = ArrayValues[-1]

 	Result.append(minValue)