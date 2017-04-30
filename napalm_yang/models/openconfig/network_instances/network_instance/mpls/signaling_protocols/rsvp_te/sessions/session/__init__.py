
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import record_route_objects
import state
class session(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of RSVP sessions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_index','__record_route_objects','__state',)

  _yang_name = 'session'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_objects = YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__local_index = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'sessions', u'session']

  def _get_local_index(self):
    """
    Getter method for local_index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/local_index (leafref)

    YANG Description: Reference to the local index for the RSVP
session
    """
    return self.__local_index
      
  def _set_local_index(self, v, load=False):
    """
    Setter method for local_index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/local_index (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_index() directly.

    YANG Description: Reference to the local index for the RSVP
session
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_index must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__local_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_index(self):
    self.__local_index = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_record_route_objects(self):
    """
    Getter method for record_route_objects, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects (container)

    YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
    """
    return self.__record_route_objects
      
  def _set_record_route_objects(self, v, load=False):
    """
    Setter method for record_route_objects, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_objects is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_objects() directly.

    YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_objects must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__record_route_objects = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_objects(self):
    self.__record_route_objects = YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/state (container)

    YANG Description: Operational state parameters relating to the
RSVP session
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the
RSVP session
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  local_index = __builtin__.property(_get_local_index)
  record_route_objects = __builtin__.property(_get_record_route_objects)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = {'local_index': local_index, 'record_route_objects': record_route_objects, 'state': state, }


import record_route_objects
import state
class session(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/sessions/session. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of RSVP sessions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_index','__record_route_objects','__state',)

  _yang_name = 'session'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__record_route_objects = YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__local_index = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'sessions', u'session']

  def _get_local_index(self):
    """
    Getter method for local_index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/local_index (leafref)

    YANG Description: Reference to the local index for the RSVP
session
    """
    return self.__local_index
      
  def _set_local_index(self, v, load=False):
    """
    Setter method for local_index, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/local_index (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_index() directly.

    YANG Description: Reference to the local index for the RSVP
session
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_index must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__local_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_index(self):
    self.__local_index = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_record_route_objects(self):
    """
    Getter method for record_route_objects, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects (container)

    YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
    """
    return self.__record_route_objects
      
  def _set_record_route_objects(self, v, load=False):
    """
    Setter method for record_route_objects, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/record_route_objects (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record_route_objects is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record_route_objects() directly.

    YANG Description: Enclosing container for MPLS RRO objects associated with the
traffic engineered tunnel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record_route_objects must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__record_route_objects = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record_route_objects(self):
    self.__record_route_objects = YANGDynClass(base=record_route_objects.record_route_objects, is_container='container', yang_name="record-route-objects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/state (container)

    YANG Description: Operational state parameters relating to the
RSVP session
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions/session/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the
RSVP session
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  local_index = __builtin__.property(_get_local_index)
  record_route_objects = __builtin__.property(_get_record_route_objects)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = {'local_index': local_index, 'record_route_objects': record_route_objects, 'state': state, }


