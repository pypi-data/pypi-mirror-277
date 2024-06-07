## IVM
This is a python binding for IVM cross-platform library for EyePoint Signature Analyzer.

### Installation
```
pip install ivm
```

### Minimal example
```python
from ivm import IvmDeviceHandle
from math import ceil

# Useful constants
MEASUREMENT_COMPLETE = IvmDeviceHandle.CheckMeasurementStatusResponse.ReadyStatus.MEASUREMENT_COMPLETE
FRAME_SIZE = IvmDeviceHandle.GetMeasurementRequest.FrameNumber.FRAME_SIZE

# Set correct device URI here
# Format for Windows: com:\\.\COM5
# Format for Linux: /dev/ttyACM0
device_uri = r'com:\\.\COM404'

try:
    device = IvmDeviceHandle(device_uri)
except RuntimeError:
    print(f"Cannot open device {device_uri}.")
    print("Please check URI and try again.")
    exit()
print("Device opened")

# Launch single measurement in non-blocking mode
device.start_measurement()
# Wait for measurement to finish
while device.check_measurement_status().ready_status != MEASUREMENT_COMPLETE:
    continue

# Number of points in a single measurement
number_of_points = device.get_measurement_settings().number_points
print(f"Number of points in a single curve measurement is {number_of_points}")

# Get all measurement results
currents = []
voltages = []
# Measurements are stored in frames of size FRAME_SIZE
number_of_frames = ceil(number_of_points/FRAME_SIZE)
for frame_index in range(number_of_frames):
    currents += list(device.get_measurement(frame_index).current)
    voltages += list(device.get_measurement(frame_index).voltage)

print("List of measured currents (in mA):")
print(*(f"{k:.4f}" for k in currents), sep=", ")

print("List of measured voltages (in V):")
print(*(f"{k:.4f}" for k in voltages), sep=", ")

# Close the device
device.close_device()
print("Device closed")
```

### More information
* You can visit Eyepoint website: https://eyepoint.physlab.ru/ru/ for other examples of using IVM python bindings
(for example, see https://eyepoint.physlab.ru/en/product/EyePoint_S2/, section "Examples of using the API and bindings for Python and C#")