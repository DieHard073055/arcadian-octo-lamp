#!usr/bin/python2.7


def main():

	print 'Your password : ' + generate_password(25, -1, 1, 1, 1, 1)
	
	
def generate_password(string_length=6, seed=-1, capital_letters=1, simple_letters=1, numbers=1, i_symbols=1 ):
	
	#All the required imports
	import random
	import time
	
	#All the required characters for generating passwords
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	symbols = ['!','@','#','$','%','^','*','(',')','_','-','+','=','{','}','[',']',':',';',',','.','?','|','~']
	
	#variable to hold the password
	output = ''
	
	#set the keys for selecting the 
	keys = []
	
	if capital_letters == 1:
		keys.append('c')
		
	if simple_letters == 1:
		keys.append('s')
		
	if numbers == 1:
		keys.append('n')
		
	if i_symbols == 1:
		keys.append('y')
		
	
	#set the seed
	if seed == -1:
		seed = time.time()
	
	random.seed(seed)
	
	
	for letters in range(string_length):
		
		selected_key = keys[random.randint(0, len(keys) -1)]
		if selected_key == 'c':
			output = output + alpha[random.randint(0, len(alpha)-1)].upper()
		elif selected_key == 's':
			output = output + alpha[random.randint(0, len(alpha)-1)]
		elif selected_key == 'n':
			output = output + str(random.randint(0, 9))
		elif selected_key == 'y':
			output = output + symbols[random.randint(0, len(symbols)-1)]
	
	
	return output
	


	
if __name__ == '__main__':
	main()
