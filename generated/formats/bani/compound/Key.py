from generated.formats.bani.compound.Vector3Short import Vector3Short
from generated.formats.bani.compound.Vector3Ushort import Vector3Ushort


class Key:

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.euler = Vector3Short()
		self.translation = Vector3Ushort()

	def read(self, stream):

		self.io_start = stream.tell()
		self.euler = stream.read_type(Vector3Short)
		self.translation = stream.read_type(Vector3Ushort)

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_type(self.euler)
		stream.write_type(self.translation)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'Key [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* euler = ' + self.euler.__repr__()
		s += '\n	* translation = ' + self.translation.__repr__()
		s += '\n'
		return s
