"""
    Umweltbundesamt Air Data API

    Air data API of Umweltbundesamt  # noqa: E501

    The version of the OpenAPI document: 2.0.1
    Contact: immission@uba.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.luftqualitaet.model.network import Network

from deutschland import luftqualitaet

globals()["Network"] = Network
from deutschland.luftqualitaet.model.inline_response2006_networks import (
    InlineResponse2006Networks,
)


class TestInlineResponse2006Networks(unittest.TestCase):
    """InlineResponse2006Networks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2006Networks(self):
        """Test InlineResponse2006Networks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineResponse2006Networks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
