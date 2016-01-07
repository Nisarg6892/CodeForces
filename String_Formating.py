n = int(raw_input())

length = len(bin(n))

for x in range(1, n+1) :

	octal = str(oct(x))[1:]
	hexadecimal = str(hex(x))[2:]
	binary = str(bin(x))[2:]

	print (length-len(str(x)))*' '+x, (length-len(octal))*' '+x, (length-len(hexadecimal))*' '+x, (length-len(binary))*' '+x

