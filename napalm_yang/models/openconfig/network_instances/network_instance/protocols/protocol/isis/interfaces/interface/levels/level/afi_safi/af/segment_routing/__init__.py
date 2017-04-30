
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import prefix_sids
import adjacency_sids
class segment_routing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operatioanl state parameters relating to segment
routing for an interface within the IGP.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_sids','__adjacency_sids',)

  _yang_name = 'segment-routing'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sids = YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__prefix_sids = YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'afi-safi', u'af', u'segment-routing']

  def _get_prefix_sids(self):
    """
    Getter method for prefix_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/prefix_sids (container)

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing IGP-Prefix SID for this
interface.
    """
    return self.__prefix_sids
      
  def _set_prefix_sids(self, v, load=False):
    """
    Setter method for prefix_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/prefix_sids (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_sids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_sids() directly.

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing IGP-Prefix SID for this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_sids must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_sids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_sids(self):
    self.__prefix_sids = YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_adjacency_sids(self):
    """
    Getter method for adjacency_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids (container)

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
    """
    return self.__adjacency_sids
      
  def _set_adjacency_sids(self, v, load=False):
    """
    Setter method for adjacency_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sids() directly.

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sids must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__adjacency_sids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sids(self):
    self.__adjacency_sids = YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  prefix_sids = __builtin__.property(_get_prefix_sids, _set_prefix_sids)
  adjacency_sids = __builtin__.property(_get_adjacency_sids, _set_adjacency_sids)


  _pyangbind_elements = {'prefix_sids': prefix_sids, 'adjacency_sids': adjacency_sids, }


import prefix_sids
import adjacency_sids
class segment_routing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/afi-safi/af/segment-routing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operatioanl state parameters relating to segment
routing for an interface within the IGP.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_sids','__adjacency_sids',)

  _yang_name = 'segment-routing'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__adjacency_sids = YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__prefix_sids = YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'levels', u'level', u'afi-safi', u'af', u'segment-routing']

  def _get_prefix_sids(self):
    """
    Getter method for prefix_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/prefix_sids (container)

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing IGP-Prefix SID for this
interface.
    """
    return self.__prefix_sids
      
  def _set_prefix_sids(self, v, load=False):
    """
    Setter method for prefix_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/prefix_sids (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_sids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_sids() directly.

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing IGP-Prefix SID for this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_sids must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_sids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_sids(self):
    self.__prefix_sids = YANGDynClass(base=prefix_sids.prefix_sids, is_container='container', yang_name="prefix-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_adjacency_sids(self):
    """
    Getter method for adjacency_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids (container)

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
    """
    return self.__adjacency_sids
      
  def _set_adjacency_sids(self, v, load=False):
    """
    Setter method for adjacency_sids, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/afi_safi/af/segment_routing/adjacency_sids (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency_sids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency_sids() directly.

    YANG Description: Configuration and operational state parameters relating to
the advertisement of a segment routing adjacency SID for this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency_sids must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__adjacency_sids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency_sids(self):
    self.__adjacency_sids = YANGDynClass(base=adjacency_sids.adjacency_sids, is_container='container', yang_name="adjacency-sids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  prefix_sids = __builtin__.property(_get_prefix_sids, _set_prefix_sids)
  adjacency_sids = __builtin__.property(_get_adjacency_sids, _set_adjacency_sids)


  _pyangbind_elements = {'prefix_sids': prefix_sids, 'adjacency_sids': adjacency_sids, }


