import sys

def xor(data, key):
    # Ensure the key is repeated to match the length of the data
    repeated_key = key * (len(data) // len(key)) + key[:len(data) % len(key)]

    # Perform the XOR operation byte by byte
    result = bytearray()
    for i in range(len(data)):
        # Handle both bytes and integers correctly
        if isinstance(data[i], int):
            result.append(data[i] ^ repeated_key[i])
        else:
            result.append(data[i] ^ ord(repeated_key[i]))

    return bytes(result)

def main():
    # Read the data from stdin (standard input)
    data = sys.stdin.buffer.read()

    # Get the key from the command-line argument
    key = sys.argv[1]

    # Perform the XOR operation
    encrypted_data = xor(data, key.encode())

    # Print the result
    sys.stdout.buffer.write(encrypted_data)

if __name__ == "__main__":
    main()
