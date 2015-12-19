class Tape:
	#initialize Tape with local file
	def __init__(self,tape_fd):
		#self.tape is a list
		self.tape = tape_fd.read().split(" ")

	def __getitem__(self,index):
		return self.tape[index]

	def __setitem__(self,index,value):
		self.tape[index] = value

	def show(self):
		print(" ".join(self.tape))
                      
class Turing:
	def __init__(self,table_fd):
		#**********************************#
		#control method
		#state1 char1 state2 char1 direction
		#**********************************#
		#control method table interpretation
		self.control = []
		self.data = table_fd.read().split("\n")
		for item in self.data:
			self.control.append(item.split(" "))
		#Turing machine current state
		self.state = 0
		#Turing machine current positon on tape
		self.seek = 0

	#run Turing machine with tape
	def run(self,tape):
		while True:
			#filte with current state
			c_list = filter(lambda x:x[0]==str(self.state),self.control)
			#filte with current tape state
			c_list = filter(lambda x:x[1]==tape[self.seek],c_list)
			if c_list == []:
				return None
			self.state = c_list[0][2]
			tape[self.seek] = c_list[0][3]
			if c_list[0][4] == "r":
				self.seek += 1
			elif c_list[0][4] == "l":
				self.seek -= 1
			elif c_list[0][4] == "s":
				break


with open("tape.txt") as fd:
        ta = Tape(fd)

with open("method.txt") as fd:
	tu = Turing(fd)

ta.show()
tu.run(ta)
ta.show()
