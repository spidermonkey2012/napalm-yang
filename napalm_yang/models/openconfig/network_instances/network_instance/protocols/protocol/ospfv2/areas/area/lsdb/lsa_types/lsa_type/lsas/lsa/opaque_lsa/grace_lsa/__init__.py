
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import tlvs
class grace_lsa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/grace-lsa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Grace LSA is utilised when a remote system is undergoing
graceful restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tlvs',)

  _yang_name = 'grace-lsa'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tlvs = YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'grace-lsa']

  def _get_tlvs(self):
    """
    Getter method for tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs (container)

    YANG Description: TLVs of the Grace LSA
    """
    return self.__tlvs
      
  def _set_tlvs(self, v, load=False):
    """
    Setter method for tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tlvs() directly.

    YANG Description: TLVs of the Grace LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tlvs(self):
    self.__tlvs = YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  tlvs = __builtin__.property(_get_tlvs)


  _pyangbind_elements = {'tlvs': tlvs, }


import tlvs
class grace_lsa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/grace-lsa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Grace LSA is utilised when a remote system is undergoing
graceful restart
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tlvs',)

  _yang_name = 'grace-lsa'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tlvs = YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'grace-lsa']

  def _get_tlvs(self):
    """
    Getter method for tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs (container)

    YANG Description: TLVs of the Grace LSA
    """
    return self.__tlvs
      
  def _set_tlvs(self, v, load=False):
    """
    Setter method for tlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/grace_lsa/tlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tlvs() directly.

    YANG Description: TLVs of the Grace LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__tlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tlvs(self):
    self.__tlvs = YANGDynClass(base=tlvs.tlvs, is_container='container', yang_name="tlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  tlvs = __builtin__.property(_get_tlvs)


  _pyangbind_elements = {'tlvs': tlvs, }


