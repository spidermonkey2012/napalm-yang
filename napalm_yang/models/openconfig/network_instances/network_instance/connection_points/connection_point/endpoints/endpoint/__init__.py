
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import config
import state
import local_
import remote
class endpoint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__endpoint_id','__config','__state','__local_','__remote',)

  _yang_name = 'endpoint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote = YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__local_ = YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'connection-points', u'connection-point', u'endpoints', u'endpoint']

  def _get_endpoint_id(self):
    """
    Getter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/endpoint_id (leafref)

    YANG Description: A pointer to the configured identifier for the
endpoint
    """
    return self.__endpoint_id
      
  def _set_endpoint_id(self, v, load=False):
    """
    Setter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/endpoint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_id() directly.

    YANG Description: A pointer to the configured identifier for the
endpoint
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__endpoint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_id(self):
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config (container)

    YANG Description: Configuration parameters relating to the
endpoint
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to the
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/state (container)

    YANG Description: Operational state parameters relating to the
endpoint
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/local (container)

    YANG Description: Configuration and operational state parameters
relating to a local interface
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/local (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.

    YANG Description: Configuration and operational state parameters
relating to a local interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_remote(self):
    """
    Getter method for remote, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/remote (container)

    YANG Description: Configuration and operational state parameters
relating to a remote interface
    """
    return self.__remote
      
  def _set_remote(self, v, load=False):
    """
    Setter method for remote, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/remote (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote() directly.

    YANG Description: Configuration and operational state parameters
relating to a remote interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote(self):
    self.__remote = YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  endpoint_id = __builtin__.property(_get_endpoint_id, _set_endpoint_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  local_ = __builtin__.property(_get_local_, _set_local_)
  remote = __builtin__.property(_get_remote, _set_remote)


  _pyangbind_elements = {'endpoint_id': endpoint_id, 'config': config, 'state': state, 'local_': local_, 'remote': remote, }


import config
import state
import local_
import remote
class endpoint(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/connection-points/connection-point/endpoints/endpoint. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of the endpoints (interfaces or remote
connection points that can be used for this
connection point). The active endpoint is selected
based on the precedence that it is configured
with
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__endpoint_id','__config','__state','__local_','__remote',)

  _yang_name = 'endpoint'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__remote = YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__local_ = YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'connection-points', u'connection-point', u'endpoints', u'endpoint']

  def _get_endpoint_id(self):
    """
    Getter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/endpoint_id (leafref)

    YANG Description: A pointer to the configured identifier for the
endpoint
    """
    return self.__endpoint_id
      
  def _set_endpoint_id(self, v, load=False):
    """
    Setter method for endpoint_id, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/endpoint_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_endpoint_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_endpoint_id() directly.

    YANG Description: A pointer to the configured identifier for the
endpoint
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """endpoint_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__endpoint_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_endpoint_id(self):
    self.__endpoint_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="endpoint-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config (container)

    YANG Description: Configuration parameters relating to the
endpoint
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to the
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/state (container)

    YANG Description: Operational state parameters relating to the
endpoint
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters relating to the
endpoint
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/local (container)

    YANG Description: Configuration and operational state parameters
relating to a local interface
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/local (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.

    YANG Description: Configuration and operational state parameters
relating to a local interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=local_.local_, is_container='container', yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_remote(self):
    """
    Getter method for remote, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/remote (container)

    YANG Description: Configuration and operational state parameters
relating to a remote interface
    """
    return self.__remote
      
  def _set_remote(self, v, load=False):
    """
    Setter method for remote, mapped from YANG variable /network_instances/network_instance/connection_points/connection_point/endpoints/endpoint/remote (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote() directly.

    YANG Description: Configuration and operational state parameters
relating to a remote interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote(self):
    self.__remote = YANGDynClass(base=remote.remote, is_container='container', yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  endpoint_id = __builtin__.property(_get_endpoint_id, _set_endpoint_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  local_ = __builtin__.property(_get_local_, _set_local_)
  remote = __builtin__.property(_get_remote, _set_remote)


  _pyangbind_elements = {'endpoint_id': endpoint_id, 'config': config, 'state': state, 'local_': local_, 'remote': remote, }


