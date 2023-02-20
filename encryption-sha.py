#sha (secure hash algorithm) are a set of crypto graphic hash functions

import hashlib

test_sha = True

pc_makers = ['Dell',
    'HP',
    'Lenovo',
    'Acer',
    'Asus',
    'ASUS',
    'Apple',
    'MSI',
    'Razer',
    'Alienware',
    'Intel',
    'AMD',
    'NVIDIA',
    'Gigabyte',
    'Kingston',
    'Samsung',
    'Microsoft',
    'Western Digital',
    'Palit',
    'ZOTAC',
    'Asrock',
    'Cooler Master',
    'ICYBOX',
    'Creative'
    'Raspberry Pi']


def test_sha(value_to_test):
    while True:
        hash_instance = hashlib.sha256(value_to_test.encode())
        string_hash = hash_instance.hexdigest() 
        # print(value_to_test)
        print(string_hash)

        if string_hash == 'f96dcd14273d3eb067b188a7536c7ce8cde51374525d0d2822aa8d7a534248b4':
            print('RESULT: ' + value_to_test)
            return False

    #hexidigest() returns the encoded data in hexadecimal format
    # print(result.hexdigest())
    # #number of hex digits in the string * 4 binary digits = 256
    # print(result.block_size)

    # #bytes
    # print(result.digest_size)


#encode() converts the string into bytes to be accepted by the hash function.
while test_sha == True:
    for pc_maker in pc_makers:
        test_sha(pc_maker.capitalize())
        test_sha(pc_maker)
        test_sha(pc_maker.upper())
        test_sha(pc_maker.lower())