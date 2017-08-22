
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

from . import config
from . import state
from . import ingress
from . import transit
from . import egress
class static_lsp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: list of defined static LSPs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__config','__state','__ingress','__transit','__egress',)

  _yang_name = 'static-lsp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__transit = YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps', u'static-lsp']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/name (leafref)

    YANG Description: Reference the name list key
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference the name list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/config (container)

    YANG Description: Configuration data for the static lsp
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for the static lsp
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/state (container)

    YANG Description: Operational state data for the static lsp
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for the static lsp
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


  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress (container)

    YANG Description: Static LSPs for which the router is an
 ingress node
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: Static LSPs for which the router is an
 ingress node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_transit(self):
    """
    Getter method for transit, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/transit (container)

    YANG Description: Static LSPs for which the router is an
 transit node
    """
    return self.__transit
      
  def _set_transit(self, v, load=False):
    """
    Setter method for transit, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/transit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transit() directly.

    YANG Description: Static LSPs for which the router is an
 transit node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__transit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transit(self):
    self.__transit = YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/egress (container)

    YANG Description: Static LSPs for which the router is an
 egress node
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/egress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: Static LSPs for which the router is an
 egress node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  ingress = __builtin__.property(_get_ingress, _set_ingress)
  transit = __builtin__.property(_get_transit, _set_transit)
  egress = __builtin__.property(_get_egress, _set_egress)


  _pyangbind_elements = {'name': name, 'config': config, 'state': state, 'ingress': ingress, 'transit': transit, 'egress': egress, }


from . import config
from . import state
from . import ingress
from . import transit
from . import egress
class static_lsp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/static-lsps/static-lsp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: list of defined static LSPs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__config','__state','__ingress','__transit','__egress',)

  _yang_name = 'static-lsp'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__transit = YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'static-lsps', u'static-lsp']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/name (leafref)

    YANG Description: Reference the name list key
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference the name list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/config (container)

    YANG Description: Configuration data for the static lsp
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for the static lsp
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/state (container)

    YANG Description: Operational state data for the static lsp
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for the static lsp
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


  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress (container)

    YANG Description: Static LSPs for which the router is an
 ingress node
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/ingress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: Static LSPs for which the router is an
 ingress node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=ingress.ingress, is_container='container', yang_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_transit(self):
    """
    Getter method for transit, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/transit (container)

    YANG Description: Static LSPs for which the router is an
 transit node
    """
    return self.__transit
      
  def _set_transit(self, v, load=False):
    """
    Setter method for transit, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/transit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transit() directly.

    YANG Description: Static LSPs for which the router is an
 transit node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__transit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transit(self):
    self.__transit = YANGDynClass(base=transit.transit, is_container='container', yang_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/egress (container)

    YANG Description: Static LSPs for which the router is an
 egress node
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps/static_lsp/egress (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: Static LSPs for which the router is an
 egress node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=egress.egress, is_container='container', yang_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  ingress = __builtin__.property(_get_ingress, _set_ingress)
  transit = __builtin__.property(_get_transit, _set_transit)
  egress = __builtin__.property(_get_egress, _set_egress)


  _pyangbind_elements = {'name': name, 'config': config, 'state': state, 'ingress': ingress, 'transit': transit, 'egress': egress, }


