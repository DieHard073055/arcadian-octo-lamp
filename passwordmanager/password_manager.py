#!usr/bin/python2.7
import sys
import generate_password as gen_pass
import clipboard
import encryption

# gen_pass.generate_password(25, -1, 1, 1, 1, 1)
# python password_manager [option] [pass key]
# options :
#	view_pass
#	gen_pass

data_file = 'password_manager.data'
data = []

def main():
	print gen_pass.generate_password(25, 'DiehardOfDeath', 1, 1, 1, 1)

def add_new_application():
	passwords = []
	print 'How many passwords would you like to generate:'
	num_pass = int(input())
	
	for i in range(num_pass):
		passwords.append(gen_pass.generate_password(25, -1, 1, 1, 1, 1))

	print "\n\tGENERATED PASSWORDS"
	print "---------------------------------------"
	for i in range(len(passwords)):
		print str(i+1) + ' - ' + passwords[i]
	
	print '\n\nSelected Password : '
	selected_pass = int(input()) -1

	print 'Selected Password : ' + passwords[selected_pass]
	clipboard.clipboard(passwords[selected_pass])
	print 'Password Copied to Clipboard'

	print '\n\n\nWhat is the Application Name you want the password for : '
	application_name = raw_input('Application Name : ')
	
	data.append([application_name, encryption.encrypt_data(passwords[selected_pass], 'paradise')])
	save_data(data)
	
def save_data(data):
	global data_file
	
	f = open(data_file, 'w')
	for item in data:
		f.write(item[0] + " " + item[1] + '\n')
	f.close()

def read_file():
	global data_file
	global data
		
	f = open(data_file, 'r')
	for line in f:
		data.append(line.split())
	f.close()
	
def view_password():
	global data

	print '\n\n\tPlease Select an Application'
	print '--------------------------------------------------\n'

	for i in range(len(data)):
		print str(i+1) + " - " + data[i][0]
	
	selected_app = int(input('\nApplication : '))
	clipboard.clipboard(encryption.decrypt_data(data[selected_app-1][1], 'paradise'))
	print 'Selected Application Password Copied to Clipboard'

def menu():
	while(1):
		print '\n\tWelcome to the password manager'
		print '\t1) Create a new Application Slot'
		print '\t2) Retrieve an Application Password'
		print '\t3) Exit'
		print '\n\tPlease Select an option:'
		
		option = int(input())
		
		if option == 1:
			add_new_application()
		elif option == 2:
			view_password()
		else:
			sys.exit(0)				
	
if __name__ == '__main__':
	#read_file()
	menu()
