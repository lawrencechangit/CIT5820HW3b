from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
	#generate public key
	#Your code here
	keypair=keys.gen_keypair(curve=curve.secp256k1)
	public_key = keypair[1]
	
	#generate signature
	#Your code here
	signature=ecdsa.sign(m, keypair[0], curve.secp256k1, hashfunc=sha256)
	r = signature[0]
	s = signature[1]

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )
