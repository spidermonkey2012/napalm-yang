
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv6/addresses/address/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State data for each IPv6 address on the
interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ip','__prefix_length','__origin','__status',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_LAYER': {}, u'DHCP': {}, u'RANDOM': {}, u'OTHER': {}, u'STATIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9a-fA-F:\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv6-address-no-zone', is_config=False)
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TENTATIVE': {}, u'DEPRECATED': {}, u'INACCESSIBLE': {}, u'INVALID': {}, u'DUPLICATE': {}, u'PREFERRED': {}, u'UNKNOWN': {}, u'OPTIMISTIC': {}},), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='enumeration', is_config=False)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)

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
      return [u'interfaces', u'interface', u'routed-vlan', u'ipv6', u'addresses', u'address', u'state']

  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/ip (inet:ipv6-address-no-zone)

    YANG Description: [adapted from IETF IP model RFC 7277]

The IPv6 address on the interface.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/ip (inet:ipv6-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The IPv6 address on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9a-fA-F:\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv6-address-no-zone', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with inet:ipv6-address-no-zone""",
          'defined-type': "inet:ipv6-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9a-fA-F:\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv6-address-no-zone', is_config=False)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9a-fA-F:\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv6-address-no-zone', is_config=False)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/prefix_length (uint8)

    YANG Description: [adapted from IETF IP model RFC 7277]

The length of the subnet prefix.
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/prefix_length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The length of the subnet prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..128']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)


  def _get_origin(self):
    """
    Getter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/origin (ip-address-origin)

    YANG Description: [adapted from IETF IP model RFC 7277]

The origin of this address, e.g., static, dhcp, etc.
    """
    return self.__origin
      
  def _set_origin(self, v, load=False):
    """
    Setter method for origin, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/origin (ip-address-origin)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The origin of this address, e.g., static, dhcp, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_LAYER': {}, u'DHCP': {}, u'RANDOM': {}, u'OTHER': {}, u'STATIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin must be of a type compatible with ip-address-origin""",
          'defined-type': "openconfig-if-ip:ip-address-origin",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_LAYER': {}, u'DHCP': {}, u'RANDOM': {}, u'OTHER': {}, u'STATIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)""",
        })

    self.__origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin(self):
    self.__origin = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINK_LAYER': {}, u'DHCP': {}, u'RANDOM': {}, u'OTHER': {}, u'STATIC': {}},), is_leaf=True, yang_name="origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='ip-address-origin', is_config=False)


  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/status (enumeration)

    YANG Description: [adapted from IETF IP model RFC 7277]

The status of an address.  Most of the states correspond
to states from the IPv6 Stateless Address
Autoconfiguration protocol.
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/addresses/address/state/status (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The status of an address.  Most of the states correspond
to states from the IPv6 Stateless Address
Autoconfiguration protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TENTATIVE': {}, u'DEPRECATED': {}, u'INACCESSIBLE': {}, u'INVALID': {}, u'DUPLICATE': {}, u'PREFERRED': {}, u'UNKNOWN': {}, u'OPTIMISTIC': {}},), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with enumeration""",
          'defined-type': "openconfig-if-ip:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TENTATIVE': {}, u'DEPRECATED': {}, u'INACCESSIBLE': {}, u'INVALID': {}, u'DUPLICATE': {}, u'PREFERRED': {}, u'UNKNOWN': {}, u'OPTIMISTIC': {}},), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='enumeration', is_config=False)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TENTATIVE': {}, u'DEPRECATED': {}, u'INACCESSIBLE': {}, u'INVALID': {}, u'DUPLICATE': {}, u'PREFERRED': {}, u'UNKNOWN': {}, u'OPTIMISTIC': {}},), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='enumeration', is_config=False)

  ip = __builtin__.property(_get_ip)
  prefix_length = __builtin__.property(_get_prefix_length)
  origin = __builtin__.property(_get_origin)
  status = __builtin__.property(_get_status)


  _pyangbind_elements = {'ip': ip, 'prefix_length': prefix_length, 'origin': origin, 'status': status, }


