
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/static-routes/static/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for static routes
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix','__set_tag',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)
    self.__set_tag = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'static-routes', u'static', u'state']

  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/prefix (inet:ip-prefix)

    YANG Description: Destination prefix for the static route, either IPv4 or
IPv6.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/prefix (inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: Destination prefix for the static route, either IPv4 or
IPv6.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with inet:ip-prefix""",
          'defined-type': "inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)


  def _get_set_tag(self):
    """
    Getter method for set_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/set_tag (oc-pt:tag-type)

    YANG Description: Set a generic tag value on the route. This tag can be
used for filtering routes that are distributed to other
routing protocols.
    """
    return self.__set_tag
      
  def _set_set_tag(self, v, load=False):
    """
    Setter method for set_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/set_tag (oc-pt:tag-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_tag() directly.

    YANG Description: Set a generic tag value on the route. This tag can be
used for filtering routes that are distributed to other
routing protocols.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_tag must be of a type compatible with oc-pt:tag-type""",
          'defined-type': "oc-pt:tag-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)""",
        })

    self.__set_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_tag(self):
    self.__set_tag = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)

  prefix = __builtin__.property(_get_prefix)
  set_tag = __builtin__.property(_get_set_tag)


  _pyangbind_elements = {'prefix': prefix, 'set_tag': set_tag, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/static-routes/static/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for static routes
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix','__set_tag',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)
    self.__set_tag = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'static-routes', u'static', u'state']

  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/prefix (inet:ip-prefix)

    YANG Description: Destination prefix for the static route, either IPv4 or
IPv6.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/prefix (inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: Destination prefix for the static route, either IPv4 or
IPv6.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with inet:ip-prefix""",
          'defined-type': "inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ip-prefix', is_config=False)


  def _get_set_tag(self):
    """
    Getter method for set_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/set_tag (oc-pt:tag-type)

    YANG Description: Set a generic tag value on the route. This tag can be
used for filtering routes that are distributed to other
routing protocols.
    """
    return self.__set_tag
      
  def _set_set_tag(self, v, load=False):
    """
    Setter method for set_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/static_routes/static/state/set_tag (oc-pt:tag-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_tag() directly.

    YANG Description: Set a generic tag value on the route. This tag can be
used for filtering routes that are distributed to other
routing protocols.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_tag must be of a type compatible with oc-pt:tag-type""",
          'defined-type': "oc-pt:tag-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)""",
        })

    self.__set_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_tag(self):
    self.__set_tag = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'}),], is_leaf=True, yang_name="set-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-pt:tag-type', is_config=False)

  prefix = __builtin__.property(_get_prefix)
  set_tag = __builtin__.property(_get_set_tag)


  _pyangbind_elements = {'prefix': prefix, 'set_tag': set_tag, }


