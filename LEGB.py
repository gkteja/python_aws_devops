x= 'global x'
def outer():
	def inner():
		x = 'local x'
		print (x)
	inner()

	x = 'outer x'
	print(x)
outer()


print(x)