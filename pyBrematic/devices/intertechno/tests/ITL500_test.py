# -*- coding: utf-8 -*-
import unittest

from pyBrematic.devices import AutoPairDevice
from pyBrematic.devices.intertechno import ITL500
from pyBrematic.gateways import BrennenstuhlGateway, IntertechnoGateway


class TestITL500(unittest.TestCase):
    def setUp(self):
        self.bsgw = BrennenstuhlGateway("192.168.178.2")
        self.itgw = IntertechnoGateway("192.168.178.3")

        seed = 8712387
        self.dev = ITL500(123, seed)

    def test_up(self):
        up_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(up_signal_ITGW, self.dev.get_signal(self.itgw, AutoPairDevice.ACTION_UP))

        up_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(up_signal_BSGW, self.dev.get_signal(self.bsgw, AutoPairDevice.ACTION_UP))

    def test_down(self):
        down_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(down_signal_ITGW, self.dev.get_signal(self.itgw, AutoPairDevice.ACTION_DOWN))

        down_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,15,15,3,15,15,3,3,15,3,3,15,15,15,3,15,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(down_signal_BSGW, self.dev.get_signal(self.bsgw, AutoPairDevice.ACTION_DOWN))

    def test_other_seed(self):
        seed2 = 89090823173454879234
        dev_new = ITL500(1234, seed2)

        up_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        down_signal_ITGW = "0,0,5,10976,98,67,0,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,112,0"
        self.assertEqual(up_signal_ITGW, dev_new.get_signal(self.itgw, AutoPairDevice.ACTION_UP))
        self.assertEqual(down_signal_ITGW, dev_new.get_signal(self.itgw, AutoPairDevice.ACTION_DOWN))

        up_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,15,3,3,3,3,3,3,3,15,3,3,3,15," + "3,126"
        down_signal_BSGW = "TXP:0,0,5,10976,98,66,3,29," + "15,3,15,15,3,3,3,3,3,15,3,3,15,15,3,3,15,15,3,3,15,15,15,3,15,3,3,3,15,3,3,3,15,3,3,3,15,3,3,3,3,3,15,3,3,3,15," + "3,126"
        self.assertEqual(up_signal_BSGW, dev_new.get_signal(self.bsgw, AutoPairDevice.ACTION_UP))
        self.assertEqual(down_signal_BSGW, dev_new.get_signal(self.bsgw, AutoPairDevice.ACTION_DOWN))