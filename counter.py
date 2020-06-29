'''
Author : Mochammad Ihza Rizky Karim
'''
loop = True 
counter = 0

while loop:
	is_black = False

	if counter == 3 or counter == 6:
		counter += 1
		continue
	elif counter == 2 and counter % 2 == 0 or counter < 10 and counter > 0:
		is_black = True 
		print('Black', counter,'Pink')

	if counter > 15:
		loop = False
		break
	elif not is_black:
		print('counter ke-', counter)
	counter += 1
