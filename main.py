import json
# f = open('dictionary.json')
# data = json.load(f)
# asm = open('test.asm', 'r').read().split('\n')
# for i in asm:
# 	parse(i)


class Assembler:

	def load_instructions_set(self, instructions_set):
		self.instructions_set = json.load(open(instructions_set))
		
	def load_program(self, program_path):
		self.program = open(program_path, 'r').read().split('\n')
	
	def process_line(self, line):
		line = line.split(' '); 
		if line[0] not in self.instructions_set:
			return;
		print(line)
		

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