"""
This module provides classes for interfacing with a MCP492X devices.
"""
from myDevices.devices.spi import SPI
from myDevices.devices.analog import DAC
from myDevices.plugins.analog import AnalogOutput


class MCP492X(SPI, DAC):
    """Base class for interacting with a MCP492X extensions."""

    def __init__(self, chip, channel_count, vref):
        """Initializes MCP492X device.

        Arguments:
        chip: The chip select
        channel_count: Number of channels on the device
        vref: The reference voltage
        """
        SPI.__init__(self, int(chip), 0, 8, 10000000)
        DAC.__init__(self, channel_count, 12, float(vref))
        self.buffered=False
        self.gain=False
        self.shutdown=False
        self.values = [0 for i in range(channel_count)]

    def __str__(self):
        """Returns friendly name."""
        return "MCP492%d(chip=%d)" % (self._analogCount, self.chip)

    def __analogRead__(self, channel, diff=False):
        """Read the analog input. Overrides ADC.__analogRead__.

        channel: Channel on the device
        diff: True if using differential input
        """
        return self.values[channel]
        
    def __analogWrite__(self, channel, value):
        """Writes the value to the specified channel. Overrides DAC.__analogWrite__."""
        d = bytearray(2)
        d[0]  = 0
        d[0] |= (channel & 0x01) << 7
        d[0] |= (self.buffered & 0x01) << 6
        d[0] |= (not self.gain & 0x01) << 5
        d[0] |= (not self.shutdown & 0x01) << 4
        d[0] |= (value >> 8) & 0x0F
        d[1]  = value & 0xFF
        self.writeBytes(d)
        self.values[channel] = value


class MCP4921(MCP492X):
    """Class for interacting with a MCP4921 extension."""

    def __init__(self, chip=0, vref=3.3):
        """Initializes MCP4921 device.

        Arguments:
        chip: The chip select
        vref: The reference voltage
        """
        MCP492X.__init__(self, chip, 1, vref)


class MCP4922(MCP492X):
    """Class for interacting with a MCP4922 extension."""

    def __init__(self, chip=0, vref=3.3):
        """Initializes MCP4922 device.

        Arguments:
        chip: The chip select
        vref: The reference voltage
        """
        MCP492X.__init__(self, chip, 2, vref)


class MCP4922Test(MCP4922):
    """Class for simulating a MCP4922 device."""

    def __init__(self):
        """Initializes the test class."""
        self.bytes = None
        MCP4922.__init__(self)

    def writeBytes(self, data):
        """Write data bytes."""
        self.bytes = data
