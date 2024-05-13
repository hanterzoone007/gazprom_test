a = [[1,2,3], [4,5,6]]

b = [{'k'+str(index+1):j  for index, j in enumerate(i)} for i in a]
print(b)