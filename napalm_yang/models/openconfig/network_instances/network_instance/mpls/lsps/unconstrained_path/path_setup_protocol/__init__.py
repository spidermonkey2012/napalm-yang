
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

class path_setup_protocol(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/unconstrained-path/path-setup-protocol. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: select and configure the signaling method for
 the LSP
  """
  _pyangbind_elements = {}

  

class path_setup_protocol(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/unconstrained-path/path-setup-protocol. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: select and configure the signaling method for
 the LSP
  """
  _pyangbind_elements = {}

  

