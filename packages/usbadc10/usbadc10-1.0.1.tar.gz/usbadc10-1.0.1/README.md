## USBADC10
This is a python binding for usbadc10 cross-platform library for USBADC10 - a device that converts an input analog signal into a discrete code, includes 10 channels of a 12—bit ADC, an STM32 microcontroller and a USB interface that supplies power and reads digitized data.

![image](https://raw.githubusercontent.com/EPC-MSU/UALab/3982c42a179a38d2dce1af6235d4ec88ee8cab51/media/usbadc10_board.jpg)

### Installation
```
pip install usbadc10
```

### Minimal example
```python
from usbadc10 import Usbadc10DeviceHandle

# Set correct device URI here
# Format for Windows: com:\\.\COM5
# Format for Linux: /dev/ttyACM0
device_uri = r'com:\\.\COM5'

device = Usbadc10DeviceHandle(device_uri)

raw_data_all_channels = list(device.get_conversion_raw().data)
print("List of raw ADC counts from all channels:\n", raw_data_all_channels)

voltage_all_channels = list(device.get_conversion().data)
print("List of voltages from all channels (in cV=10*mV):\n", voltage_all_channels)

voltage_all_channels_mV = [value/10 for value in voltage_all_channels]
print("List of voltages from all channels (in mV):\n", voltage_all_channels_mV)

# Close the device
device.close_device()

```

### More information
* usbadc10 website: https://usbadc10.physlab.ru/ru/ 