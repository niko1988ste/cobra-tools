import typing
from generated.array import Array
from generated.formats.fgm.compound.Color import Color


class TextureInfo:

	"""
	part of fgm fragment, per texture involved
	"""

	def __init__(self, arg=None, template=None):
		self.name = ''
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# byte offset to name in fgm buffer
		self.offset = 0

		# 7=has 2 8=uses texture indices
		self.is_textured = 0

		# stores index into shader and array index of texture
		self.indices = Array()

		# stores index into shader
		self.indices = Array()

		# Stores (usually) 2 rgba colors
		self.colors = Array()

		# Stores rgba color
		self.colors = Array()

	def read(self, stream):

		self.io_start = stream.tell()
		self.offset = stream.read_uint()
		self.is_textured = stream.read_uint()
		if not (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8))) and self.is_textured == 8:
			self.indices.read(stream, 'Uint', 4, None)
		if ((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)) and self.is_textured == 8:
			self.indices.read(stream, 'Uint', 1, None)
		if not (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8))) and self.is_textured == 7:
			self.colors.read(stream, Color, 4, None)
		if ((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)) and self.is_textured == 7:
			self.colors.read(stream, Color, 1, None)

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):

		self.io_start = stream.tell()
		stream.write_uint(self.offset)
		stream.write_uint(self.is_textured)
		if not (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8))) and self.is_textured == 8:
			self.indices.write(stream, 'Uint', 4, None)
		if ((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)) and self.is_textured == 8:
			self.indices.write(stream, 'Uint', 1, None)
		if not (((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8))) and self.is_textured == 7:
			self.colors.write(stream, Color, 4, None)
		if ((stream.user_version == 24724) or (stream.user_version == 25108)) and ((stream.version == 19) and (stream.version_flag == 8)) and self.is_textured == 7:
			self.colors.write(stream, Color, 1, None)

		self.io_size = stream.tell() - self.io_start

	def __repr__(self):
		s = 'TextureInfo [Size: '+str(self.io_size)+', Address:'+str(self.io_start)+'] ' + self.name
		s += '\n	* offset = ' + self.offset.__repr__()
		s += '\n	* is_textured = ' + self.is_textured.__repr__()
		s += '\n	* indices = ' + self.indices.__repr__()
		s += '\n	* colors = ' + self.colors.__repr__()
		s += '\n'
		return s
