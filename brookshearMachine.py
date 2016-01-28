#!/usr/bin/env python3

import operator

class BrookshearMachine():

	def __init__(self):
		self.pc= ''
		self.ir=''
		self.memory=dict()
		self.registers={'0'=0, '1'=0, '2'=0, '3'=0, '4'=0, '5'=0,
						'6'=0, '7'=0, '8'=0, '9'=0, 'A'=0, 'B'=0,
						'C'=0, 'D'=0, 'E'=0, 'F'=0}
		pass

	def setPC(self, value):
		if value[0] == ['A'-'F'] or value[0] == ['0'-'9']:
			if value[1] == ['A'-'F'] or value[1] == ['0'-'9']:
				self.pc=value

	def setIR(self, value):
		if 'int' in type(value):
			if value <= 15:
				self.ir = value

	def load(self, r, x, y):
		'''
		LOAD the register R with bit pattern XY
		'''
		self.registers[str(r)] == str(x+y)
		pass

	def memLoad(self, r, x, y):
		'''
		LOAD the register R with bit pattern found in the memory cell at XY
		'''
		self.registers[str(r)] = self.memory[str(x+y)]

	def store(self, r, x, y):
		'''
		STORE the bit pattern found in register R in the memory cell at XY
		'''
		self.memory[str(x+y)] = self.registers[str(r)]

	def move(self, r, s):
		'''
		MOVE the bit pattern found in register R to register S
		'''
		self.registers[str(r)] = self.registers[str(s)]
		self.registers[str(s)] = 0

	def add(self, r, s, t):
		'''
		ADD the bit patterns in registers S & T as though they were two's
		complement representation & leave the result in register R
		'''
		temp = s + t
		if temp > 255:
			temp = 0
		self.registers[str(r)] = temp

	def bmOr(self, r, s, t):
		'''
		OR the bit patterns in registers S and t and place the result in register R
		'''
		temp = bin(s) or bin(t)
		if temp > 255:
			temp = 0
		self.registers[str(r)] = temp

	def bmAnd(self, r, s, t):
		'''
		AND the bit patterns in register S and T and place the result in register R
		'''
		temp = bin(s) and bin(t)
		if temp > 255:
			temp = 0
		self.registers[str(r)] = temp

	def xor(self, r, s, t):
		'''
		XOR the bit patterns in register S and T and place theresult in register R
		'''
		temp = operator.xor(s, t)
		if temp > 255:
			temp = 0
		self.registers[str(r)] = temp

	def rotate(self, r, x):
		'''
		ROTATE the bit pattern in register R one bit to the right X times
		'''
		pass

	def jump(self, r, x, y):
		'''
		JUMP to the instruction located in the memory cell at address XY if
		the bit pattern in register R is equal to the bit pattern in register 0,
		otherwise, continue with the normal sequence of execution
		'''
		pass

	def halt(self, r, x, y):
		'''
		HALT execution
		'''
		pass

	def fetch(self):
		pass

	def increment(self):
		self.ir += 2

	def decode(self):
		pass

	def execute(self):
		if self.ir[0] == '1':
			pass
		elif self.ir[0] == '2':
			pass
		elif self.ir[0] == '3':
			pass
		elif self.ir[0] == '4':
			pass
		elif self.ir[0] == '5':
			pass
		elif self.ir[0] == '6':
			pass
		elif self.ir[0] == '7':
			pass
		elif self.ir[0] == '8':
			pass
		elif self.ir[0] == '9':
			pass
		elif self.ir[0] == 'A':
			pass
		elif self.ir[0] == 'B':
			pass
		elif self.ir[0] == 'C':
			pass
		elif self.ir[0] == 'D':
			pass
		elif self.ir[0] == 'E':
			pass
		elif self.ir[0] == 'F':
			pass
		pass

	def run(self):
		self.fetch()
		self.increment()
		self.decode()
		self.execute()