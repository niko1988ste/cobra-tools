class BaniFragmentData1:

	"""
	Seems to be the same for all bani anims of one bani file
	"""

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.unknown_0 = 0
		self.unknown_1 = 0
		self.unknown_2 = 0

		# these first 4 are zeros but I think may be offset stuff we've seen before
		self.unknown_3 = 0

		# 96 in parrots case
		self.bytes_per_frame = 0

		# how many bytes for each bone per frame
		self.bytes_per_bone = 0

		# Number of frames for all bani files in banis buffer, 18*96 gives the size of banis buffer for parrot
		self.num_frames = 0

		# matches number of bones parrot has
		self.num_bones = 0

		# translation range
		self.translation_center = 0

		# translation range
		self.translation_first = 0

	def read(self, stream):

		self.io_start = stream.tell()
		self.unknown_0 = stream.read_uint()
		self.unknown_1 = stream.read_uint()
		self.unknown_2 = stream.read_uint()
		self.unknown_3 = stream.read_uint()
		self.bytes_per_frame = stream.read_uint()
		self.bytes_per_bone = stream.read_uint()
		self.num_frames = stream.read_uint()
		self.num_bones = stream.read_uint()
		self.translation_center = stream.read_float()
		self.translation_first = stream.read_float()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_uint(self.unknown_0)
		stream.write_uint(self.unknown_1)
		stream.write_uint(self.unknown_2)
		stream.write_uint(self.unknown_3)
		stream.write_uint(self.bytes_per_frame)
		stream.write_uint(self.bytes_per_bone)
		stream.write_uint(self.num_frames)
		stream.write_uint(self.num_bones)
		stream.write_float(self.translation_center)
		stream.write_float(self.translation_first)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'BaniFragmentData1 [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* unknown_0 = ' + self.unknown_0.__repr__()
		s += '\n	* unknown_1 = ' + self.unknown_1.__repr__()
		s += '\n	* unknown_2 = ' + self.unknown_2.__repr__()
		s += '\n	* unknown_3 = ' + self.unknown_3.__repr__()
		s += '\n	* bytes_per_frame = ' + self.bytes_per_frame.__repr__()
		s += '\n	* bytes_per_bone = ' + self.bytes_per_bone.__repr__()
		s += '\n	* num_frames = ' + self.num_frames.__repr__()
		s += '\n	* num_bones = ' + self.num_bones.__repr__()
		s += '\n	* translation_center = ' + self.translation_center.__repr__()
		s += '\n	* translation_first = ' + self.translation_first.__repr__()
		s += '\n'
		return s
