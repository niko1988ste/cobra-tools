class Material0:

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# index into name buffer
		self.name_index = 0

		# always zero
		self.zero = 0

	def read(self, stream):

		self.io_start = stream.tell()
		self.name_index = stream.read_uint()
		self.zero = stream.read_uint()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_uint(self.name_index)
		stream.write_uint(self.zero)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'Material0 [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* name_index = ' + self.name_index.__repr__()
		s += '\n	* zero = ' + self.zero.__repr__()
		s += '\n'
		return s
