class B:
	def __init__(self,number):
		self.number = number

arrayB= []

class A:
	def __init__(self):
		self.array= []

	def add(self):
		for i in range(len(arrayB)):
			self.array.append(arrayB[i])

def main():
	for i in range(100):
		arrayB.append(B(i))

	arrayA = []

	for i in range(10):
		arrayA.append(A())
		arrayA[i].add()

	arrayA[0].array[2]=3
	print "Hi"
	print arrayA[0].array[2]
	print arrayA[1].array[2]
	
main()
