
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/timers/spf/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS SPF timers.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__spf_hold_interval','__spf_first_interval','__spf_second_interval','__adaptive_timer',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__spf_hold_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__spf_first_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__adaptive_timer = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)
    self.__spf_second_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'timers', u'spf', u'state']

  def _get_spf_hold_interval(self):
    """
    Getter method for spf_hold_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_hold_interval (uint64)

    YANG Description: SPF Hold Down time interval in milliseconds.
    """
    return self.__spf_hold_interval
      
  def _set_spf_hold_interval(self, v, load=False):
    """
    Setter method for spf_hold_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_hold_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_hold_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_hold_interval() directly.

    YANG Description: SPF Hold Down time interval in milliseconds.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_hold_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_hold_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_hold_interval(self):
    self.__spf_hold_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_spf_first_interval(self):
    """
    Getter method for spf_first_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_first_interval (uint64)

    YANG Description: Time interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
    return self.__spf_first_interval
      
  def _set_spf_first_interval(self, v, load=False):
    """
    Setter method for spf_first_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_first_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_first_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_first_interval() directly.

    YANG Description: Time interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_first_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_first_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_first_interval(self):
    self.__spf_first_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_spf_second_interval(self):
    """
    Getter method for spf_second_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_second_interval (uint64)

    YANG Description: Time interval in milliseconds between the first and second
SPF calculation.
    """
    return self.__spf_second_interval
      
  def _set_spf_second_interval(self, v, load=False):
    """
    Setter method for spf_second_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_second_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_second_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_second_interval() directly.

    YANG Description: Time interval in milliseconds between the first and second
SPF calculation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_second_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_second_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_second_interval(self):
    self.__spf_second_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_adaptive_timer(self):
    """
    Getter method for adaptive_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/adaptive_timer (oc-isis-types:adaptive-timer-type)

    YANG Description: ISIS adaptive timer types (linear, exponential).
    """
    return self.__adaptive_timer
      
  def _set_adaptive_timer(self, v, load=False):
    """
    Setter method for adaptive_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/adaptive_timer (oc-isis-types:adaptive-timer-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adaptive_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adaptive_timer() directly.

    YANG Description: ISIS adaptive timer types (linear, exponential).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adaptive_timer must be of a type compatible with oc-isis-types:adaptive-timer-type""",
          'defined-type': "oc-isis-types:adaptive-timer-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)""",
        })

    self.__adaptive_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adaptive_timer(self):
    self.__adaptive_timer = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)

  spf_hold_interval = __builtin__.property(_get_spf_hold_interval)
  spf_first_interval = __builtin__.property(_get_spf_first_interval)
  spf_second_interval = __builtin__.property(_get_spf_second_interval)
  adaptive_timer = __builtin__.property(_get_adaptive_timer)


  _pyangbind_elements = {'spf_hold_interval': spf_hold_interval, 'spf_first_interval': spf_first_interval, 'spf_second_interval': spf_second_interval, 'adaptive_timer': adaptive_timer, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/timers/spf/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS SPF timers.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__spf_hold_interval','__spf_first_interval','__spf_second_interval','__adaptive_timer',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__spf_hold_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__spf_first_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    self.__adaptive_timer = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)
    self.__spf_second_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'timers', u'spf', u'state']

  def _get_spf_hold_interval(self):
    """
    Getter method for spf_hold_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_hold_interval (uint64)

    YANG Description: SPF Hold Down time interval in milliseconds.
    """
    return self.__spf_hold_interval
      
  def _set_spf_hold_interval(self, v, load=False):
    """
    Setter method for spf_hold_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_hold_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_hold_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_hold_interval() directly.

    YANG Description: SPF Hold Down time interval in milliseconds.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_hold_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_hold_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_hold_interval(self):
    self.__spf_hold_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), default=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64)(5000), is_leaf=True, yang_name="spf-hold-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_spf_first_interval(self):
    """
    Getter method for spf_first_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_first_interval (uint64)

    YANG Description: Time interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
    return self.__spf_first_interval
      
  def _set_spf_first_interval(self, v, load=False):
    """
    Setter method for spf_first_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_first_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_first_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_first_interval() directly.

    YANG Description: Time interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_first_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_first_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_first_interval(self):
    self.__spf_first_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-first-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_spf_second_interval(self):
    """
    Getter method for spf_second_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_second_interval (uint64)

    YANG Description: Time interval in milliseconds between the first and second
SPF calculation.
    """
    return self.__spf_second_interval
      
  def _set_spf_second_interval(self, v, load=False):
    """
    Setter method for spf_second_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/spf_second_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf_second_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf_second_interval() directly.

    YANG Description: Time interval in milliseconds between the first and second
SPF calculation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf_second_interval must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
        })

    self.__spf_second_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf_second_interval(self):
    self.__spf_second_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="spf-second-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)


  def _get_adaptive_timer(self):
    """
    Getter method for adaptive_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/adaptive_timer (oc-isis-types:adaptive-timer-type)

    YANG Description: ISIS adaptive timer types (linear, exponential).
    """
    return self.__adaptive_timer
      
  def _set_adaptive_timer(self, v, load=False):
    """
    Setter method for adaptive_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/timers/spf/state/adaptive_timer (oc-isis-types:adaptive-timer-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adaptive_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adaptive_timer() directly.

    YANG Description: ISIS adaptive timer types (linear, exponential).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adaptive_timer must be of a type compatible with oc-isis-types:adaptive-timer-type""",
          'defined-type': "oc-isis-types:adaptive-timer-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)""",
        })

    self.__adaptive_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adaptive_timer(self):
    self.__adaptive_timer = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'LINEAR': {}, u'EXPONENTIAL': {}},), is_leaf=True, yang_name="adaptive-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:adaptive-timer-type', is_config=False)

  spf_hold_interval = __builtin__.property(_get_spf_hold_interval)
  spf_first_interval = __builtin__.property(_get_spf_first_interval)
  spf_second_interval = __builtin__.property(_get_spf_second_interval)
  adaptive_timer = __builtin__.property(_get_adaptive_timer)


  _pyangbind_elements = {'spf_hold_interval': spf_hold_interval, 'spf_first_interval': spf_first_interval, 'spf_second_interval': spf_second_interval, 'adaptive_timer': adaptive_timer, }


