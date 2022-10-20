import json
import re

class Assembler:

	def load_instructions_set(self, instructions_set):
		self.instructions_set = json.load(open(instructions_set))
		
	def load_program(self, program_path):
		self.program = open(program_path, 'r').read().split('\n')

	def get_values_of(self, c):
		return c['arguments'], c['word'], c['immediate']
	
	def convert_parameters_values(self, line):
		for i in range(1, len(line)):
			
			
	
	def process_line(self, line):
		line = line.split(' '); 
		if line[0] not in self.instructions_set:
			return;

		self.convert_parameters_values(line)

		argc, word, immediate = self.get_values_of(self.instructions_set[line[0]])
		# if argc == 3:
		# 	if 'a' in word:
		# 		print("op $1 $2 $3")
		# 	else:
		# 		word = word.replace('s', line[2])
		# 		word = word.replace('t', line[3])
		# 		word = word.replace('d', line[1])
		# 		print(word)
		# elif argc == 2:
		# 	if immediate:
		# 		print("opi $1 $2 10")
		# 	else:
		# 		print("op $1 $2")

	def parse(self, program_path):
		self.load_program(program_path)
		for line in self.program:
			self.process_line(line)

	def print_instructions_set(self):
		for i in self.instructions_set:
			print(i, self.instructions_set[i])


a = Assembler()
a.load_instructions_set('dictionary.json')
a.parse('test.asm')
#a.print_instructions_set()