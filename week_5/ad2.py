from ex1 import *

class Reading_files:
	'''reads files and cretes lists 
	according to the leangth of the word'''

	def __init__(self,file_name):

		self.file = file_name


	def read_words(self):
		'''reads the file and returns it splited.'''
		with open(self.file,'r') as f:
			for self.line in f:
				pass


	def store_words(self):
		'''stores the linked list'''

		srt = self.line.split()
		srt.sort(key=len)

		instances = [Linked_list() for i in range(len(srt))]
		
		for self.i in instances:
			
			for word in srt:
				print (self.i)
				return self.i.append(word)
			

	def __str__(self):
		'''prints the list.'''
		return str(self.a)



if __name__ == '__main__':
	try:
		a = Reading_files('text_file.txt')
		a.read_words()
		a.store_words()
		# print (a)
	except ValueError:
		pass
