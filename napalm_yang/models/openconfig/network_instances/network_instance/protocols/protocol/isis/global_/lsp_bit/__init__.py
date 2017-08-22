
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import overload_bit
from . import attached_bit
class lsp_bit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS LSP Operational Bits.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__overload_bit','__attached_bit',)

  _yang_name = 'lsp-bit'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attached_bit = YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__overload_bit = YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit']

  def _get_overload_bit(self):
    """
    Getter method for overload_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit (container)

    YANG Description: This container defines Overload Bit configuration.
    """
    return self.__overload_bit
      
  def _set_overload_bit(self, v, load=False):
    """
    Setter method for overload_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overload_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overload_bit() directly.

    YANG Description: This container defines Overload Bit configuration.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overload_bit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__overload_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overload_bit(self):
    self.__overload_bit = YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_attached_bit(self):
    """
    Getter method for attached_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit (container)

    YANG Description: This container defines Attached Bit.
    """
    return self.__attached_bit
      
  def _set_attached_bit(self, v, load=False):
    """
    Setter method for attached_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attached_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attached_bit() directly.

    YANG Description: This container defines Attached Bit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attached_bit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__attached_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attached_bit(self):
    self.__attached_bit = YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  overload_bit = __builtin__.property(_get_overload_bit, _set_overload_bit)
  attached_bit = __builtin__.property(_get_attached_bit, _set_attached_bit)


  _pyangbind_elements = {'overload_bit': overload_bit, 'attached_bit': attached_bit, }


from . import overload_bit
from . import attached_bit
class lsp_bit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS LSP Operational Bits.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__overload_bit','__attached_bit',)

  _yang_name = 'lsp-bit'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__attached_bit = YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__overload_bit = YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit']

  def _get_overload_bit(self):
    """
    Getter method for overload_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit (container)

    YANG Description: This container defines Overload Bit configuration.
    """
    return self.__overload_bit
      
  def _set_overload_bit(self, v, load=False):
    """
    Setter method for overload_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/overload_bit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overload_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overload_bit() directly.

    YANG Description: This container defines Overload Bit configuration.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overload_bit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__overload_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overload_bit(self):
    self.__overload_bit = YANGDynClass(base=overload_bit.overload_bit, is_container='container', yang_name="overload-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_attached_bit(self):
    """
    Getter method for attached_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit (container)

    YANG Description: This container defines Attached Bit.
    """
    return self.__attached_bit
      
  def _set_attached_bit(self, v, load=False):
    """
    Setter method for attached_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attached_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attached_bit() directly.

    YANG Description: This container defines Attached Bit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attached_bit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__attached_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attached_bit(self):
    self.__attached_bit = YANGDynClass(base=attached_bit.attached_bit, is_container='container', yang_name="attached-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  overload_bit = __builtin__.property(_get_overload_bit, _set_overload_bit)
  attached_bit = __builtin__.property(_get_attached_bit, _set_attached_bit)


  _pyangbind_elements = {'overload_bit': overload_bit, 'attached_bit': attached_bit, }


