import sys
import binascii
import numpy as np
from snow.CryptoMobile.CM import *
import matplotlib.pyplot as plt

def walsh_transform(window_size,num_bytes):
	# generating a keystream
	keystream=snow._generate_keystream(num_bytes)
	binary_keystream = bin(int.from_bytes(keystream, byteorder='big'))
	# The bin() function returns a string with a '0b' prefix, so you might want to remove it.
	binary_keystream = binary_keystream[2:]
	keystream_arr= []
	#converting the key stream to an array of bits
	for i in binary_keystream:
		keystream_arr.append(int(i))
	keystream_arr = np.array(keystream_arr)
	walsh_transform=np.zeros(2**window_size)
	coeff=np.zeros(window_size)
	#calculating the walsh transform for all possible coefficients using a window of the given size
	for c in range(0,2**window_size):
		coeff=[(c >> j) & 1 for j in range(0,window_size)]
		coeff = coeff[::-1]
		for i in range(1,num_bytes-window_size+1):
			window_ele=keystream_arr[i-1:i+window_size-1]
			walsh_transform[c]+=((-1)**(keystream_arr[i+window_size]^(np.dot(coeff,window_ele)%2)))
	walsh_transform = np.abs(walsh_transform)
	#finding the coefficient that best approximates the keystream
	max_val_coeff = np.argmax(walsh_transform)
	print('The coefficients of the LFSR that best approximates the keystream are:',bin(max_val_coeff),'or',max_val_coeff)
	# Code to plot the graph for walsh transform
	plt.figure(figsize=(10,6))

	x=[m for m in range(2**window_size)]

	plt.title('Approximating the Snow Cipher using LFSR')
	plt.xlabel('Coefficients of size '+ str(2**window_size) + ' bits')
	plt.ylabel('Walsh Transform')
	plt.plot(x,walsh_transform)
	plt.plot(max_val_coeff, max(walsh_transform), marker="o", markersize=10, markeredgecolor="red", markerfacecolor="red")
	plt.savefig('./plots/q2_plot.png',dpi=300)
	plt.show()
	return walsh_transform


#Boiler Plate Code
count   = 1923412495
bearer  = 12
direct  = 1
bitlen  = 8

k = '2bd6459f82c5b300952c49104881ff48'
i = 'ea024714ad5c4d84df1f9b251c0bf45f'

if (len(sys.argv)>1):
	message=str(sys.argv[1])

if (len(sys.argv)>2):
	k=str(sys.argv[2])

if (len(sys.argv)>3):
	i=str(sys.argv[3])

key=binascii.a2b_hex(k)
iv=binascii.a2b_hex(i)

snow    = SNOW3G()
snow._initialize(key, iv)

walsh_transform_arr = walsh_transform(4,32)
print(walsh_transform_arr)



