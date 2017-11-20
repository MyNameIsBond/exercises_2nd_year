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

		sorted_list = self.line.split()
		sorted_list.sort(key=len)
		len_counter = 0

		instances = [Linked_list() for i in range(len(sorted_list))]
		for self.i in instances:
			print ('this is not!')
			for word in sorted_list:
				print ('this is it!')
				if len_counter <= len(sorted_list):
					if len_counter == len(word):
						self.i.append(word)
					else:
						len_counter += 1
				else:
					return None
			print (self.i)

	def __str__(self):
		'''prints the list.'''
		return str(self.i)



if __name__ == '__main__':
	try:
		a = Reading_files('text_file.txt')
		a.read_words()
		a.store_words()
		print (a)
	except ValueError:
		pass
