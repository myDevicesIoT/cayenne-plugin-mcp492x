# Cayenne MCP492X Plugin
A plugin allowing the [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent) to read data from and write data to MCP492X devices (MCP4921, MCP4922) and display it in the [Cayenne Dashboard](https://cayenne.mydevices.com).

## Requirements
### Hardware
* [Rasberry Pi](https://www.raspberrypi.org).
* An MCP492X device, e.g. [MCP4922](https://www.microchip.com/wwwproducts/en/MCP4922).

### Software
* [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent). This can be installed from the [Cayenne Dashboard](https://cayenne.mydevices.com).
* [Git](https://git-scm.com/).

## Getting Started

### 1. Installation

   From the command line run the following commands to install this plugin.
   ```
   cd /etc/myDevices/plugins
   sudo git clone https://github.com/myDevicesIoT/cayenne-plugin-mcp492x.git
   ```

### 2. Modifying the plugin

   Specify the device you are using by setting the `class` value under the `MCP` section in the `cayenne_mcp492x.plugin` file.
   By default this is set to `MCP4922` but it can also be set `MCP4921`.

   If you use a `MCP4921` device instead of a `MCP4922` or you do not want the raw channel values to be displayed in the Cayenne 
   dashboard you can disable any of the individual input sections in `cayenne_mcp492x.plugin`.

### 3. Restarting the agent

   Restart the agent so it can load the plugin.
   ```
   sudo service myDevices restart
   ```
   Temporary widgets for the plugin should now show up in the [Cayenne Dashboard](https://cayenne.mydevices.com). You can make them permanent by clicking the plus sign.

   NOTE: If the temporary widgets do not show up try refreshing the [Cayenne Dashboard](https://cayenne.mydevices.com) or restarting the agent again using `sudo service myDevices restart`.