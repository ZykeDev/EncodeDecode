
def decode(input, k):
	l = len(input)
	output = []
	
	for i in range(0, l, k):
		dstr = decode_block(input[i:i+k])
		
		output.append(dstr)


	print("".join(output))
	return "".join(output)


# Bruteforcely decodes a block using the same hashing function
def decode_block(code):
	k = len(code)
	code = int(code)

	for a in range(31, 127):
		possible = customhash(a)

		if code == possible:
			return chr(a)

	return "_"



def customhash(val):
	val *= 17
	if val < 1000:
		val *= 10

	return val






input = "142817681785195554401785195554401649544019721717195519725440185317171955195516491751171778205440"
decode(input, 4)