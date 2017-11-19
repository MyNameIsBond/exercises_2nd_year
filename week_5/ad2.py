from ex1 import *

class Reading_files:
	''' reads files and cretes lists 
	according to the leangth of the word '''

	def __init__(self,file_name):

		self.file = file_name


	def read_words(self):
		''' '''
		with open(self.file,'r') as f:
			for self.line in f:	
				return self.line.split()


	def store_words(self):
		''' '''

		srt = self.line.split()
		srt.sort(key=len)
		self.a = Linked_list()
		for i in srt:
			self.a.append(i)
			print ('\t:{}'.format(i))

			
		return self.a
			


	def __str__(self):
		''' '''
		return str(self.a)



if __name__ == '__main__':
	try:
		a = Reading_files('text_file.txt')
		a.read_words()
		a.store_words()
		print (a)
	except ValueError:
		pass
