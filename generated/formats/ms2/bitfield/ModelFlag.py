from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember


class ModelFlag(BasicBitfield):

	"""
	Determines the data held by a mesh.
	Count from the end!!!
	"""
	basic_info = BitfieldMember(pos=9, mask=0x200, return_type=bool)
	weights = BitfieldMember(pos=4, mask=0x10, return_type=bool)

	def set_defaults(self):
		pass

	def read(self, stream):
		self._value = stream.read_uint()

	def write(self, stream):
		stream.write_uint(self._value)
