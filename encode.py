# Marco Vincenzi
#
# The following is an experimental way to encode a given string
# by converting it into ASCII, computing a hash with a knwon
# k-chars hashing function, transmit it and then decode it
# with a brutefoce approach, sequentially computing every possible
# char and comparing it with the recieved one.

# The idea came to mind while thinking about safe ways to openly share
# text only certain people were capable of reading. There are plenty of
# other, more secure methods, though this one only requires the knowledge
# of the hashing function by both parties.

k = 4

# Encode a string
def encode(string):
	ascii_string = [ord(c) for c in string]

	hashed = compute_hash(ascii_string)

	print(hashed)
	return hashed



# Custom hashing function
def compute_hash(astr):
	rmd = len(astr) % k
	hashed = []

	# Make sure the text is mod k
	if rmd != 0:
		for i in range(k-rmd):
			astr.append(ord(' ')) 
	
	# The hash is computed in groups of k-chars, then concat'd
	for i in range(0, len(astr), k):
		tstr = astr[i:i+k]
		hstr = []

		for c in tstr:
			hstr.append(customhash(c))


		h = "".join(map(str, hstr))
		hashed.append(h)
	

	return "".join(hashed)


# Custom hashing function. TODO improve
def customhash(val):
	val *= 17
	if val < 1000:
		val *= 10

	return val




if __name__ == "__main__":
	encode("This is a test message.")
