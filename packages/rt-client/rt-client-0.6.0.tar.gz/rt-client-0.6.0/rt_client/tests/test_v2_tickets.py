import unittest
from unittest import mock

from rt_client.v2.tickets import TicketManager
from rt_client import exceptions


class V2TicketsTestCase(unittest.TestCase):
    def test_get_all_method_is_not_supported(self):
        manager = TicketManager(mock.MagicMock(name="Client"))
        self.assertRaises(exceptions.UnsupportedOperation, manager.get_all)
