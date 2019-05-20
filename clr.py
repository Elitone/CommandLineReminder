import os
import pickle

yes_list = ['y', 'Y', 'yes', 'YES', 'Yes']
programs = {}

class Program:
	def __init__(self, program_name):
		self.program_name = program_name
		self.commands = {}

	def add_command(self, command, note):
		self.commands[command] = note

	def remove_command(self, command):
		self.commands.pop(command)

	def modify_command(self, command, new_command):
		if command in self.commands.keys():
			self.commands[new_command] = self.commands.pop(command)

	def modify_note(self, command, new_note):
		if command in self.commands.keys():
			self.commands[command] = new_note

	def modify_program_name(self, new_name):
		self.program_name = new_name

	def print_commands(self):
		global counter
		counter = {}
		i = 0
		print(f'Program name: {self.program_name}')
		for c in self.commands.keys():
			counter[i] = c
			print(f'	[{i}]	{c}	> {self.commands[c]}')
			i += 1

def saved_program_names():
	print('\nProgram database:')
	for p in programs.keys():
		print(f'		{p}')

def save_database_programs():
	with open('programs.db', 'wb') as programs_database:
		pickle.dump(programs, programs_database)

def load_database_programs():
	with open('programs.db', 'rb') as programs_database:
		return pickle.load(programs_database)

def main_text():

	print("""

<<<                  Command line reminder (CLR)                            >>>

<<<  Made by: Elit-one Yamamoto  |   Welcome to Command line reminder (CLR) >>>
<<<  Version: 0.1.0.0 (Beta)     |   Database for all command line tools    >>>
--------------------------------------------------------------------------------""")

def main_menu():
	os.system('clear')
	main_text()
	print("""
-1 Add new program
-2 Remove program
-3 Show saved programs
-4 Show all entry of db
-5 Select program and work
-6 Export
-7 Import
-0 Exit
""")

def select_program_and_work_menu():
	os.system('clear')
	main_text()
	print("""
-1 Print all command
-2 Add command
-3 Remove command
-4 Modify command
-5 Modify note
-6 Modify name of program
-0 Exit
""")

if __name__ == '__main__':
	load = input('Load database? [y-n]: ')
	try:
		if load in yes_list:
			programs = load_database_programs()
	except FileNotFoundError:
		os.system('clear')
		input('Database file not found!\n\nPress any key to continue')

	while True:
		main_menu()
		try:
			menu_choice = int(input('Choice [0-7]: '))
			if menu_choice == 1:
				program_name = input('Program name: ').strip()
				if program_name == '':
					os.system('clear')
					input('Impossible to save a blank name\nPress any key to continue!')

				elif program_name not in programs.keys():
					command = input('Insert new command: ')
					note = input('Insert note: ')
					if command and note != '':
						x = Program(program_name)
						x.add_command(command, note)
						programs[x.program_name] = x

				else:
					os.system('clear')
					input('Program already in database\nPress any key to continue')

			elif menu_choice == 2:
				os.system('clear')
				saved_program_names()
				program_to_remove = input('\nWhich program you want remove: ')
				if program_to_remove in programs.keys():
					del programs[program_to_remove]
					print(f'Program <{program_to_remove}> deleted')

				else:
					os.system('clear')
					input(f'Impossible to remove! \nProgram <{program_to_remove}> not found in database.\n\nPress any key to continue')
					
			elif menu_choice == 3:
				os.system('clear')
				saved_program_names()
				input('\nPress any key to continue')

			elif menu_choice == 4:
				os.system('clear')
				for n in programs.keys():
					print(f'\nProgram name: {n}')
					x = programs[n]
					for c in x.commands:
						print(f'		{c}  >  {x.commands[c]}')
				input('\nPress any key to continue')

			elif menu_choice == 5:
				os.system('clear')
				saved_program_names()
				program_to_modify = input('\nOn which program you want work: ')
				if program_to_modify in programs.keys():
					x = programs[program_to_modify]
					while True:
						select_program_and_work_menu()
						try:
							select_menu_choice = int(input('Choice [0-6]: '))
							if select_menu_choice == 1:
								os.system('clear')
								x.print_commands()
								input()

							elif select_menu_choice == 2:
								command_to_add = input('Command: ')
								note_to_add = input('Note: ')
								if (command_to_add and note_to_add != ''):
									x.add_command(command_to_add, note_to_add)

							elif select_menu_choice == 3:
								os.system('clear')
								x.print_commands() 
								command_numero = int(input('Command number to remove: '))
								if command_numero in counter.keys():
									command_to_remove = counter[command_numero]
									x.remove_command(command_to_remove)

							elif select_menu_choice == 4:
								x.print_commands()
								command_numero = int(input('Command number: '))
								if command_numero in counter.keys():
									os.system('clear')
									command_to_modify = counter[command_numero]
									print(command_to_modify)
									new_command = input('\nInsert new command: ')
									if new_command != '':
										x.modify_command(command_to_modify, new_command)

							elif select_menu_choice == 5:
								x.print_commands()
								note_number = int(input('\nInsert note number: '))
								if note_number in counter.keys():
									os.system('clear')
									note_to_modify = counter[note_number]
									print(x.commands[note_to_modify])
									new_note = input('Insert new note: ')
									if new_note != '':
										x.modify_note(note_to_modify, new_note)

							elif select_menu_choice == 6:
								print(f'Actual name: {program_to_modify}')
								new_name = input('Insert new_name: ')
								if new_name != '':
									x.modify_program_name(new_name)
									programs[x.program_name] = programs.pop(program_to_modify)

							elif select_menu_choice == 0:
								break

						except ValueError:
							select_program_and_work_menu()
				else:
					os.system('clear')
					input(f'Program <{program_to_modify}> not found\nPress any key to continue')

			elif menu_choice == 6:
				save_database_programs()

			elif menu_choice == 7:
				programs = load_database_programs()

			elif menu_choice == 0:
				os.system('clear')
				exit = input('Exit now? [y-n]: ')
				if exit in yes_list:
					save = input('You want save beafore exit? [y-n]: ')
					if save in yes_list:
						save_database_programs()
					else:
						print('Database not saved')
					break

		except ValueError:
			main_menu()
