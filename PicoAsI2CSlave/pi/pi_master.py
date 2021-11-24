import smbus
bus = smbus.SMBus(1)

#writing
bus.write_byte(0x41,12)
bus.write_byte(0x41,15)

#reading
bus.read_byte(0x41)

