import json
import re
import sys

class Assembler:

	def set_reg_names(self):
		self.reg_names = {
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
		self.program = [line.strip() for line in self.program if line.strip() != '']
		self.program = [line for line in self.program if not line.startswith(".")]
		i = 0
		j = 0
		temp_program = []
		while i < len(self.program):
			addr = " " + str(j*4 + 0x00400000)
			if self.program[i].endswith(":"):
				temp_program.append(self.program[i] + " " + self.program[i + 1] + addr)
				i = i + 1
			else:
				temp_program.append(self.program[i] + addr)
			i = i + 1
			j = j + 1
		self.program = temp_program
		self.labels = {}
		for l in self.program:
			l = l.split()
			if l[0].endswith(":"):
				self.labels[l[0]] = l[-1]

		print(self.labels)

	def get_values_of(self, c):
		return c['arguments'], c['word'], c['immediate']


	def t_complement(self,n):
		b = ""
		for i in range(16):
			b += str(n >> 15-i & 1)
		return b

	def convert_number_to_binary(self, n_str, size):
		n = int(n_str)
		return ("{0:0" + str(size) + "b}").format(n) if n >= 0 else self.t_complement(n)
	
	def convert_parameters_values(self, line, size, bits):
		for i in range(size):
			x = re.search("[^$]+", line[i]).group(0)
			if(x in self.reg_names):
				x = self.reg_names[x]
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

	def process_line(self, line):
		symbol = line.split(' ')
		if symbol[0] not in self.instructions_set:
			if symbol[0].endswith(":"):
				symbol = symbol[0:]
			elif symbol[0].startswith("."):
				##TODO PROCESSAR SECOES
				#raise Exception('Seções ainda não são tratadas')
				return
			if len(symbol) <= 1:
				return
			else:
				symbol = symbol[1:]
		
		for i in range(0, len(symbol)):
			symbol[i] = re.search('^-?[^, ]+', symbol[i]).group(0)
			x = re.findall('^#', symbol[i])
			if x:
				symbol[:i]
				break
		command = self.instructions_set[symbol[0]]

		argc, word, immediate = self.get_values_of(command)
		if '$'in word:
			if argc == 0:
				##TODO Calcular OFFSET
				label = symbol[1] + ":"
				addr = symbol[-1] 
				word = word.replace('$', self.convert_number_to_binary(addr, 26))
			if argc == 2:
				addr = symbol[-1]
				word = word.replace('$', self.convert_number_to_binary(addr, 16))
				symbol = self.convert_parameters_values(symbol[1:argc+1], 2, 5)
				word = word.replace('s', symbol[1])
				word = word.replace('t', symbol[0])
		elif argc == 3:
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
		self.set_reg_names()
		# self.indexer()
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