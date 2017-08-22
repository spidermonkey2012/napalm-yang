
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

from . import constrained_path
from . import unconstrained_path
from . import static_lsps
class lsps(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LSP definitions and configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__constrained_path','__unconstrained_path','__static_lsps',)

  _yang_name = 'lsps'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constrained_path = YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__unconstrained_path = YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__static_lsps = YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps']

  def _get_constrained_path(self):
    """
    Getter method for constrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path (container)

    YANG Description: traffic-engineered LSPs supporting different
path computation and signaling methods
    """
    return self.__constrained_path
      
  def _set_constrained_path(self, v, load=False):
    """
    Setter method for constrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constrained_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constrained_path() directly.

    YANG Description: traffic-engineered LSPs supporting different
path computation and signaling methods
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constrained_path must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__constrained_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constrained_path(self):
    self.__constrained_path = YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_unconstrained_path(self):
    """
    Getter method for unconstrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path (container)

    YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
    """
    return self.__unconstrained_path
      
  def _set_unconstrained_path(self, v, load=False):
    """
    Setter method for unconstrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unconstrained_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unconstrained_path() directly.

    YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unconstrained_path must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__unconstrained_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unconstrained_path(self):
    self.__unconstrained_path = YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_static_lsps(self):
    """
    Getter method for static_lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps (container)

    YANG Description: statically configured LSPs, without dynamic
signaling
    """
    return self.__static_lsps
      
  def _set_static_lsps(self, v, load=False):
    """
    Setter method for static_lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_lsps() directly.

    YANG Description: statically configured LSPs, without dynamic
signaling
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_lsps must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__static_lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_lsps(self):
    self.__static_lsps = YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  constrained_path = __builtin__.property(_get_constrained_path, _set_constrained_path)
  unconstrained_path = __builtin__.property(_get_unconstrained_path, _set_unconstrained_path)
  static_lsps = __builtin__.property(_get_static_lsps, _set_static_lsps)


  _pyangbind_elements = {'constrained_path': constrained_path, 'unconstrained_path': unconstrained_path, 'static_lsps': static_lsps, }


from . import constrained_path
from . import unconstrained_path
from . import static_lsps
class lsps(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LSP definitions and configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__constrained_path','__unconstrained_path','__static_lsps',)

  _yang_name = 'lsps'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__constrained_path = YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__unconstrained_path = YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__static_lsps = YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps']

  def _get_constrained_path(self):
    """
    Getter method for constrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path (container)

    YANG Description: traffic-engineered LSPs supporting different
path computation and signaling methods
    """
    return self.__constrained_path
      
  def _set_constrained_path(self, v, load=False):
    """
    Setter method for constrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_constrained_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_constrained_path() directly.

    YANG Description: traffic-engineered LSPs supporting different
path computation and signaling methods
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """constrained_path must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__constrained_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_constrained_path(self):
    self.__constrained_path = YANGDynClass(base=constrained_path.constrained_path, is_container='container', yang_name="constrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_unconstrained_path(self):
    """
    Getter method for unconstrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path (container)

    YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
    """
    return self.__unconstrained_path
      
  def _set_unconstrained_path(self, v, load=False):
    """
    Setter method for unconstrained_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unconstrained_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unconstrained_path() directly.

    YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unconstrained_path must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__unconstrained_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unconstrained_path(self):
    self.__unconstrained_path = YANGDynClass(base=unconstrained_path.unconstrained_path, is_container='container', yang_name="unconstrained-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_static_lsps(self):
    """
    Getter method for static_lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps (container)

    YANG Description: statically configured LSPs, without dynamic
signaling
    """
    return self.__static_lsps
      
  def _set_static_lsps(self, v, load=False):
    """
    Setter method for static_lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps/static_lsps (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_lsps() directly.

    YANG Description: statically configured LSPs, without dynamic
signaling
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_lsps must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__static_lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_lsps(self):
    self.__static_lsps = YANGDynClass(base=static_lsps.static_lsps, is_container='container', yang_name="static-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  constrained_path = __builtin__.property(_get_constrained_path, _set_constrained_path)
  unconstrained_path = __builtin__.property(_get_unconstrained_path, _set_unconstrained_path)
  static_lsps = __builtin__.property(_get_static_lsps, _set_static_lsps)


  _pyangbind_elements = {'constrained_path': constrained_path, 'unconstrained_path': unconstrained_path, 'static_lsps': static_lsps, }


