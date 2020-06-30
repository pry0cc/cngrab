#!/usr/bin/python3

import ssl,sys

cert = ssl.get_server_certificate((sys.argv[1], 443)) #Retrieve SSL server certificate
cert = ssl.PEM_cert_to_DER_cert(cert) #Convert certificate to DER format
begin = cert.rfind(b'\x06\x03\x55\x04\x03') + 7 #Find the last occurence of this byte string indicating the CN, add 7 bytes to startpoint to account for length of byte string and padding
end = begin + cert[begin - 1] #Set endpoint to startpoint + the length of the CN
print(cert[begin:end].decode('utf-8')) #Retrieve the CN from the DER encoded certificate