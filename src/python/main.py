import json
import re
import sys

class Assembler:

	def set_rotulos(self):
		self.rotulos = {
			"zero": 0,
			"at": 1,
			"v0": 2,
			"v1": 3,
			"a0": 4,
			"a1": 5,
			"a2": 6,
			"a3": 7,
			"t0": 8,
			"t1": 9,
			"t2": 10,
			"t3": 11,
			"t4": 12,
			"t5": 13,
			"t6": 14,
			"t7": 15,
			"s0": 16,
			"s1": 17,
			"s2": 18,
			"s3": 19,
			"s4": 20,
			"s5": 21,
			"s6": 22,
			"s7": 23,
			"t8": 24,
			"t9": 25,
			"k0": 26,
			"k1": 27,
			"gp": 28,
			"sp": 29,
			"fp": 30,
			"ra": 31
		}

	def load_instructions_set(self, instructions_set):
		self.instructions_set = json.load(open(instructions_set))
		
	def load_program(self, program_path):
		self.program = re.sub(' +', ' ', open(program_path, 'r').read().strip()).split('\n')

	def get_values_of(self, c):
		return c['arguments'], c['word'], c['immediate']

	def convert_number_to_binary(self, n_str, size):
		return ("{0:0" + str(size) + "b}").format(int(n_str))
	
	def convert_parameters_values(self, line, size, bits):
		for i in range(size):
			x = re.search("[^$]+", line[i]).group(0)
			if(x in self.rotulos):
				x = self.rotulos[x]
			line[i] = self.convert_number_to_binary(x, bits)
		return line
			
	def toHex(self, word):
		i = 0
		while i < len(word):
			s = int(word[i:i+4], 2)
			i += 4
			res = f'{s:x}'
			print(res, end="")
		print()



	def get_label_address(self, label):
		# self.indexer()
		# index = 0
		# for i in range(0, len(self.program)):
		# 	if label in self.program[i]:
		# 		index = i + 1

		# print(index)
		return

	def process_line(self, line):
		symbol = line.split(' '); 
		if symbol[0] not in self.instructions_set:
			label = re.findall(":$", symbol[0])
			section = re.findall("^.", symbol[0])
			if label:
				self.get_label_address(symbol[0])
			elif section:
				##TODO PROCESSAR SECOES
				#raise Exception('Seções ainda não são tratadas')
				return
			if len(symbol) <= 1:
				return
			else:
				symbol = symbol[1:]
		

		
		for i in range(0, len(symbol)):
			symbol[i] = re.search('[^, ]+', symbol[i]).group(0)
			x = re.findall('^#', symbol[i])
			if x:
				symbol[:i]
				break

		command = self.instructions_set[symbol[0]]

		argc, word, immediate = self.get_values_of(command)
		if argc == 3:
			symbol = self.convert_parameters_values(symbol[1:argc+1], 3, 5)
			if 'a' in word:
				word = word.replace('t', symbol[1])
				word = word.replace('d', symbol[0])
				word = word.replace('a', symbol[2])
			else:
				word = word.replace('s', symbol[1])
				word = word.replace('t', symbol[2])
				word = word.replace('d', symbol[0])
		elif argc == 2:
			if immediate:
				symbol = self.convert_parameters_values(symbol[1:4], 2, 5)
				word = word.replace('s', symbol[1])
				word = word.replace('t', symbol[0])
				word = word.replace('*', self.convert_number_to_binary(symbol[2], 16))
			else:
				symbol = self.convert_parameters_values(symbol[1:3], 2, 5)
				word = word.replace('s', symbol[0])
				word = word.replace('t', symbol[1])
		return word

	def parse(self, program_path):
		self.load_program(program_path)
		self.set_rotulos()
		for line in self.program:
			processed = self.process_line(line)
			if(not processed == None):
				self.toHex(processed)

	def print_instructions_set(self):
		for i in self.instructions_set:
			print(i, self.instructions_set[i])


a = Assembler()
a.load_instructions_set('./src/resources/dictionary.json')
a.parse(sys.argv[1])