class Header3Data1Pc:

	"""
	Data struct for headers of type 7
	"""

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.width = 0
		self.height = 0

		# may be depth
		self.array_size = 0

		# num_mips
		self.num_mips = 0

	def read(self, stream):

		self.io_start = stream.tell()
		self.width = stream.read_ushort()
		self.height = stream.read_ushort()
		self.array_size = stream.read_ushort()
		self.num_mips = stream.read_ushort()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_ushort(self.width)
		stream.write_ushort(self.height)
		stream.write_ushort(self.array_size)
		stream.write_ushort(self.num_mips)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'Header3Data1Pc [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* width = ' + self.width.__repr__()
		s += '\n	* height = ' + self.height.__repr__()
		s += '\n	* array_size = ' + self.array_size.__repr__()
		s += '\n	* num_mips = ' + self.num_mips.__repr__()
		s += '\n'
		return s
