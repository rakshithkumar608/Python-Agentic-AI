# You're building a smart thermostat alert system:
# * if the device_status is "active"
# * And temperature > 35 -> Warn: "High temperature alert!"
# *Else: "Temperature normal!"
# *If device is off -> "Device offline"


device_status = "active"
temparature = 38

if device_status == "active":
  if temparature > 35:
    print("High temparature alert!")
  else:
    print("Temparature is normal")
else:
  print("Device is offline")