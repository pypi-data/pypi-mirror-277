
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.cluster_api import ClusterApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from qdrant_openapi.api.cluster_api import ClusterApi
from qdrant_openapi.api.collections_api import CollectionsApi
from qdrant_openapi.api.points_api import PointsApi
from qdrant_openapi.api.service_api import ServiceApi
from qdrant_openapi.api.snapshots_api import SnapshotsApi
