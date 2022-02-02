# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.airquality_api import AirqualityApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.luftqualitaet.api.airquality_api import AirqualityApi
from deutschland.luftqualitaet.api.annualtabulation_api import AnnualtabulationApi
from deutschland.luftqualitaet.api.exceedances_api import ExceedancesApi
from deutschland.luftqualitaet.api.measurements_api import MeasurementsApi
from deutschland.luftqualitaet.api.metadata_api import MetadataApi
