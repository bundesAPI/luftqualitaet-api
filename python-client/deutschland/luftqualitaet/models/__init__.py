# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.luftqualitaet.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.luftqualitaet.model.airquality import Airquality
from deutschland.luftqualitaet.model.airquality_date_start_cet import (
    AirqualityDateStartCET,
)
from deutschland.luftqualitaet.model.airquality_date_start_cet3_and_following import (
    AirqualityDateStartCET3AndFollowing,
)
from deutschland.luftqualitaet.model.airquality_station_id import AirqualityStationId
from deutschland.luftqualitaet.model.airqualitylimits import Airqualitylimits
from deutschland.luftqualitaet.model.airqualitylimits_station_id import (
    AirqualitylimitsStationId,
)
from deutschland.luftqualitaet.model.annualbalance import Annualbalance
from deutschland.luftqualitaet.model.component import Component
from deutschland.luftqualitaet.model.inline_response200 import InlineResponse200
from deutschland.luftqualitaet.model.inline_response2001 import InlineResponse2001
from deutschland.luftqualitaet.model.inline_response2002 import InlineResponse2002
from deutschland.luftqualitaet.model.inline_response2003 import InlineResponse2003
from deutschland.luftqualitaet.model.inline_response2004 import InlineResponse2004
from deutschland.luftqualitaet.model.inline_response2004_data import (
    InlineResponse2004Data,
)
from deutschland.luftqualitaet.model.inline_response2005 import InlineResponse2005
from deutschland.luftqualitaet.model.inline_response2006 import InlineResponse2006
from deutschland.luftqualitaet.model.inline_response2006_components import (
    InlineResponse2006Components,
)
from deutschland.luftqualitaet.model.inline_response2006_limits1 import (
    InlineResponse2006Limits1,
)
from deutschland.luftqualitaet.model.inline_response2006_limits2 import (
    InlineResponse2006Limits2,
)
from deutschland.luftqualitaet.model.inline_response2006_networks import (
    InlineResponse2006Networks,
)
from deutschland.luftqualitaet.model.inline_response2006_scopes import (
    InlineResponse2006Scopes,
)
from deutschland.luftqualitaet.model.inline_response2006_stations import (
    InlineResponse2006Stations,
)
from deutschland.luftqualitaet.model.inline_response2006_xref import (
    InlineResponse2006Xref,
)
from deutschland.luftqualitaet.model.limit import Limit
from deutschland.luftqualitaet.model.measure import Measure
from deutschland.luftqualitaet.model.measurelimit import Measurelimit
from deutschland.luftqualitaet.model.network import Network
from deutschland.luftqualitaet.model.scope import Scope
from deutschland.luftqualitaet.model.station import Station
from deutschland.luftqualitaet.model.stationsetting import Stationsetting
from deutschland.luftqualitaet.model.stationtype import Stationtype
from deutschland.luftqualitaet.model.threshold import Threshold
from deutschland.luftqualitaet.model.transgression import Transgression
from deutschland.luftqualitaet.model.transgressiontype import Transgressiontype
