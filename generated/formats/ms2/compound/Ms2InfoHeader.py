import typing
from generated.array import Array
from generated.formats.ms2.compound.FixedString import FixedString
from generated.formats.ms2.compound.Ms2BufferInfo import Ms2BufferInfo
from generated.formats.ms2.compound.Ms2SizedStrData import Ms2SizedStrData


class Ms2InfoHeader:

	"""
	Custom header struct
	includes fragments but none of the 3 data buffers
	"""

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# 'MS2 '
		self.magic = FixedString()

		# if 0x08 then 64bit, differentiates between ED and JWE, 0x08 for ED and PC
		self.version_flag = 0

		# 0x12 = PC, 0x13 = JWE, PZ
		self.version = 0

		# endianness?, usually zero
		self.bitswap = 0

		# always = 1
		self.seventh_byte = 1
		self.user_version = 0
		self.bone_names_size = 0
		self.bone_info_size = 0
		self.general_info = Ms2SizedStrData()

		# not in PC, or at least somewhere else
		self.buffer_info = Ms2BufferInfo()
		self.name_hashes = Array()
		self.names = Array()

	def read(self, stream):

		self.io_start = stream.tell()
		self.magic = stream.read_type(FixedString, (4,))
		self.version_flag = stream.read_byte()
		stream.version_flag = self.version_flag
		self.version = stream.read_byte()
		stream.version = self.version
		self.bitswap = stream.read_byte()
		self.seventh_byte = stream.read_byte()
		self.user_version = stream.read_uint()
		stream.user_version = self.user_version
		self.bone_names_size = stream.read_uint()
		self.bone_info_size = stream.read_uint()
		self.general_info = stream.read_type(Ms2SizedStrData)
		if not ((stream.version == 18) or (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)))):
			self.buffer_info = stream.read_type(Ms2BufferInfo)
		self.name_hashes.read(stream, 'Uint', self.general_info.name_count, None)
		self.names.read(stream, 'ZString', self.general_info.name_count, None)

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_type(self.magic)
		stream.write_byte(self.version_flag)
		stream.version_flag = self.version_flag
		stream.write_byte(self.version)
		stream.version = self.version
		stream.write_byte(self.bitswap)
		stream.write_byte(self.seventh_byte)
		stream.write_uint(self.user_version)
		stream.user_version = self.user_version
		stream.write_uint(self.bone_names_size)
		stream.write_uint(self.bone_info_size)
		stream.write_type(self.general_info)
		if not ((stream.version == 18) or (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)))):
			stream.write_type(self.buffer_info)
		self.name_hashes.write(stream, 'Uint', self.general_info.name_count, None)
		self.names.write(stream, 'ZString', self.general_info.name_count, None)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'Ms2InfoHeader [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* magic = ' + self.magic.__repr__()
		s += '\n	* version_flag = ' + self.version_flag.__repr__()
		s += '\n	* version = ' + self.version.__repr__()
		s += '\n	* bitswap = ' + self.bitswap.__repr__()
		s += '\n	* seventh_byte = ' + self.seventh_byte.__repr__()
		s += '\n	* user_version = ' + self.user_version.__repr__()
		s += '\n	* bone_names_size = ' + self.bone_names_size.__repr__()
		s += '\n	* bone_info_size = ' + self.bone_info_size.__repr__()
		s += '\n	* general_info = ' + self.general_info.__repr__()
		s += '\n	* buffer_info = ' + self.buffer_info.__repr__()
		s += '\n	* name_hashes = ' + self.name_hashes.__repr__()
		s += '\n	* names = ' + self.names.__repr__()
		s += '\n'
		return s
