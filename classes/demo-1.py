# # Class Variables


# class Employee:

# 	raise_amount = 2

# 	def __init__(self, first_name, last_name, pay):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.pay = pay
# 		self.email = first_name + '.' + last_name + '@company.com'

# 	def apply_raise(self):
# 		self.pay = int(self.pay * self.raise_amount)


# emp1 = Employee('Vishal', 'Shirke', 10000000)
# emp1.raise_amount = 3
# emp1.apply_raise()
# print(emp1.pay)


# emp2 = Employee('Prashant', 'Shirke', 10000000)
# emp2.apply_raise()
# print(emp2.pay)

# Class Variables


class Employee:

	def __init__(self, first_name, last_name, pay):
		self._first_name = first_name
		self.__last_name = last_name
		self.__pay = pay
		self.email = first_name + '.' + last_name + '@company.com'

	def get_first_name(self):
		return self._first_name

	def set_first_name(self, first_name):
		self._first_name = first_name

	def get_last_name(self):
		return self.__last_name

	def set_last_name(self, last_name):
		self.__last_name = last_name


emp1 = Employee('Vishal', 'Shirke', 10000000)
# print(emp1.get_first_name(), emp1.get_last_name())
# emp1.set_first_name('john'), emp1.set_last_name('wil')
# print(emp1.get_first_name(), emp1.get_last_name())
print(emp1._first_name)
print(Employee.last_name)