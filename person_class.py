class Person:
	population = 0

	def _init_(self, myAge):
		self.age = myAge
		Person.population += 1
	def get_population(self):
		return Person.population
	def get_age(self):
		return self.age