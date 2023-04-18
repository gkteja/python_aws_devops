"""
error handeling 

"""

try:
	f = open('demo.txt','r')
	# msg = my_msg

except FileNotFoundError as e:
	print(e)

except Exception as kt:
	print(kt)

else:
	print(f.read())
	f.close()

finally:
	print('executing...')

