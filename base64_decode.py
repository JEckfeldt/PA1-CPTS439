import base64

def main():
    # Base64-encoded string to be decoded (with added padding)
    encoded_string = "SU9UU0VDMTAxe0IwMHQyUjAwdH0" + "=" * ((4 - len("SU9UU0VDMTAxe0IwMHQyUjAwdH0") % 4) % 4)

    # Decode the base64-encoded string
    decoded_bytes = base64.b64decode(encoded_string)

    # Convert the decoded bytes to a string (assuming it's a text string)
    decoded_string = decoded_bytes.decode('utf-8')

    # Print the decoded string
    print("Decoded string:", decoded_string)

if __name__ == "__main__":
    main()
