
import base64    


def decode_base64(encoded_str):
    # Add character if necessary
    missing_padding = len(encoded_str) % 4
    if missing_padding != 0:
        encoded_str += '=' * (4 - missing_padding)

    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str
