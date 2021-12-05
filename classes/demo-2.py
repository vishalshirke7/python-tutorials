# Class Methods


class Employee:

	raise_amount = 2

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.email = first_name + '.' + last_name + '@company.com'

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	#Alternative constructors
	@classmethod
	def format_string(cls, emp_str):
		first_name, last_name, pay = emp_str.split('-')
		return cls(first_name, last_name, pay)

emp1 = Employee('Vishal', 'Shirke', 10000000)
emp2 = Employee('Prashant', 'Shirke', 10000000)
#  Employee.set_raise_amount(3) == emp1.set_raise_amount(3)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Similar to Datetime module
emp1_str = 'vishal-shirke-555555'
Employee.format_string(emp1_str)