class Test():
	def __init__(self, nbr):
		self.nbr = self.__multiplie(nbr)
	
	def multiplie(self, nbr):
		return nbr * 2
	
	__multiplie = multiplie


class Test2(Test):
	def multiplie(self, nbr, multiplicateur):
		return nbr * multiplicateur
		
if __name__ == "__main__":
	a = Test(3)
	b = Test2(3)
	
	
