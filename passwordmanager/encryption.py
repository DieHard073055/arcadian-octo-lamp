#!usr/bin/python2.7
from Crypto import Random
from Crypto.Cipher import AES
import base64



def main():
	#define the key and Byte size
	key = 'paradise'
	BYTE = 32
	
	#Make sure the key is less than 32
	if len(key) >= 32:
		key = key[:32]
	else:
		key = _cover(key, BYTE)
	
	enc = 'Ieb+H7VSh8cHd02TCRZAx34z8hVT0Ie83MTxEJAmVA6QLGKBEM2aQ1mo8bPGgGg8'
	print '\nRaw text : ' + enc + '\n'
	#enc = encrypt(enc, BYTE, key)
	print decrypt(enc, key)

def encrypt_data(data, key):
	BYTE = 32
	 #Make sure the key is less than 32
        if len(key) >= 32:
                key = key[:32]
        else:
                key = _cover(key, BYTE)
	return encrypt(data, BYTE, key)

def encrypt(raw, BYTE, key):
	raw = _cover(raw, BYTE)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	raw = base64.b64encode(iv + cipher.encrypt(raw))
	
	return raw
	
def decrypt(encrypted_raw, key):
	encrypted_raw = base64.b64decode(encrypted_raw)
	iv = encrypted_raw[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	encrypted_raw = _uncover(cipher.decrypt(encrypted_raw[AES.block_size:]))
	
	return encrypted_raw
	
def decrypt_data(encrypted_raw, key):
	BYTE = 32
	if len(key) >= 32:
		key = key[:32]
	else:
		key = _cover(key, BYTE)
		
	return decrypt(encrypted_raw, key)

def _cover(raw, BYTE):
	return raw + ( BYTE - len(raw) %  BYTE) * chr( BYTE - len(raw) %  BYTE)
	
def _uncover(raw):
	return raw[:-ord(raw[len(raw)-1:])]



if __name__ == '__main__':
	
	
	main()
