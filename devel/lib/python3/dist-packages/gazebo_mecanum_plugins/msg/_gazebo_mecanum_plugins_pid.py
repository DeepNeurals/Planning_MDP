# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gazebo_mecanum_plugins/gazebo_mecanum_plugins_pid.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class gazebo_mecanum_plugins_pid(genpy.Message):
  _md5sum = "9eb89efea79b06cdde55828e8174754b"
  _type = "gazebo_mecanum_plugins/gazebo_mecanum_plugins_pid"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 LR_P
float64 LR_I
float64 LR_D
float64 LF_P
float64 LF_I
float64 LF_D
float64 RF_P
float64 RF_I
float64 RF_D
float64 RR_P
float64 RR_I
float64 RR_D"""
  __slots__ = ['LR_P','LR_I','LR_D','LF_P','LF_I','LF_D','RF_P','RF_I','RF_D','RR_P','RR_I','RR_D']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       LR_P,LR_I,LR_D,LF_P,LF_I,LF_D,RF_P,RF_I,RF_D,RR_P,RR_I,RR_D

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gazebo_mecanum_plugins_pid, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.LR_P is None:
        self.LR_P = 0.
      if self.LR_I is None:
        self.LR_I = 0.
      if self.LR_D is None:
        self.LR_D = 0.
      if self.LF_P is None:
        self.LF_P = 0.
      if self.LF_I is None:
        self.LF_I = 0.
      if self.LF_D is None:
        self.LF_D = 0.
      if self.RF_P is None:
        self.RF_P = 0.
      if self.RF_I is None:
        self.RF_I = 0.
      if self.RF_D is None:
        self.RF_D = 0.
      if self.RR_P is None:
        self.RR_P = 0.
      if self.RR_I is None:
        self.RR_I = 0.
      if self.RR_D is None:
        self.RR_D = 0.
    else:
      self.LR_P = 0.
      self.LR_I = 0.
      self.LR_D = 0.
      self.LF_P = 0.
      self.LF_I = 0.
      self.LF_D = 0.
      self.RF_P = 0.
      self.RF_I = 0.
      self.RF_D = 0.
      self.RR_P = 0.
      self.RR_I = 0.
      self.RR_D = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_12d().pack(_x.LR_P, _x.LR_I, _x.LR_D, _x.LF_P, _x.LF_I, _x.LF_D, _x.RF_P, _x.RF_I, _x.RF_D, _x.RR_P, _x.RR_I, _x.RR_D))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 96
      (_x.LR_P, _x.LR_I, _x.LR_D, _x.LF_P, _x.LF_I, _x.LF_D, _x.RF_P, _x.RF_I, _x.RF_D, _x.RR_P, _x.RR_I, _x.RR_D,) = _get_struct_12d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_12d().pack(_x.LR_P, _x.LR_I, _x.LR_D, _x.LF_P, _x.LF_I, _x.LF_D, _x.RF_P, _x.RF_I, _x.RF_D, _x.RR_P, _x.RR_I, _x.RR_D))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 96
      (_x.LR_P, _x.LR_I, _x.LR_D, _x.LF_P, _x.LF_I, _x.LF_D, _x.RF_P, _x.RF_I, _x.RF_D, _x.RR_P, _x.RR_I, _x.RR_D,) = _get_struct_12d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_12d = None
def _get_struct_12d():
    global _struct_12d
    if _struct_12d is None:
        _struct_12d = struct.Struct("<12d")
    return _struct_12d
