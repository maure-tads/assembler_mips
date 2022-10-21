import json
import re
import sys

class Assembler:

	def load_instructions_set(self, instructions_set):
		self.instructions_set = json.load(open(instructions_set))
		
	def load_program(self, program_path):
		self.program = re.sub(' +', ' ', open(program_path, 'r').read().strip().replace("  ", " ")).split('\n')

	def get_values_of(self, c):
		return c['arguments'], c['word'], c['immediate']

	def convert_number_to_binary(self, n_str, size):
		return ("{0:0" + str(size) + "b}").format(int(n_str))
	
	def convert_parameters_values(self, line, size, bits):
		for i in range(size):
			x = re.search("[0-9]+", line[i])
			line[i] = self.convert_number_to_binary(x.group(0) if x else line, bits)
		return line
			
	def toHex(self, word):
		i = 0
		while i < len(word):
			s = int(word[i:i+4], 2)
			i += 4
			res = f'{s:x}'
			print(res, end="")
		print()


	def process_line(self, line):
		line = line.split(' '); 
		if line[0] not in self.instructions_set:
			return
		command = self.instructions_set[line[0]]
		

		argc, word, immediate = self.get_values_of(command)
		if argc == 3:
			line = self.convert_parameters_values(line[1:argc+1], 3, 5)
			if 'a' in word:
				word = word.replace('t', line[1])
				word = word.replace('d', line[0])
				word = word.replace('a', line[2])
			else:
				word = word.replace('s', line[1])
				word = word.replace('t', line[2])
				word = word.replace('d', line[0])
		elif argc == 2:
			if immediate:
				line = self.convert_parameters_values(line[1:4], 2, 5)
				word = word.replace('s', line[1])
				word = word.replace('t', line[0])
				word = word.replace('*', self.convert_number_to_binary(line[2], 16))
			else:
				line = self.convert_parameters_values(line[1:3], 2, 5)
				word = word.replace('s', line[0])
				word = word.replace('t', line[1])
		return word

	def parse(self, program_path):
		self.load_program(program_path)
		for line in self.program:
			self.toHex(self.process_line(line))

	def print_instructions_set(self):
		for i in self.instructions_set:
			print(i, self.instructions_set[i])


a = Assembler()
a.load_instructions_set('dictionary.json')
a.parse('test.asm')