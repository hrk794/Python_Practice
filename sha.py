import hashlib

print("The following hash algorithmd are available with hashlib:")
print(hashlib.algorithms_guaranteed)

str = "The test string"

# This encodes the string in bytes and feeds it to the hash function, and stores the result at location pointed by sha1_hash 
sha1_hash = hashlib.sha1(str.encode())


#prints the encoded hash in hexadecimal format
print(sha1_hash.hexdigest())


# This can be done with sha256, sha384, md5, sha224, and sha512
