import serial
list='aabbcc112233'

hex=list.decode('hex')
print hex
strSerial = "abc"  
strHex = binascii.b2a_hex(strSerial)  
#print strHex   
strhex = strHex.decode("hex")  
#print strhex   
self.l_serial.write(strhex);  
