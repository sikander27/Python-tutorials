import hashlib
import os


def hash_secret(secret_value: str, salt: bytes = None) -> str:
    """
    Hashes a secret value using SHA-256 with an optional salt.

    Parameters:
    - secret_value (str): The secret value to be hashed.
    - salt (bytes): Optional salt to use for hashing. If not provided, a new salt will be generated.

    Returns:
    - str: The hexadecimal representation of the hash.
    """
    if salt is None:
        # Generate a new salt if not provided
        salt = os.urandom(16)

    # Encode the secret value to bytes
    secret_value_bytes = secret_value.encode('utf-8')

    # Combine the salt and the secret value
    salted_secret = salt + secret_value_bytes

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(salted_secret)

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    # Return the salt and hash in a combined format
    return salt.hex() + ':' + hash_hex


def verify_secret(secret_value: str, hashed_value: str) -> bool:
    """
    Verifies a secret value against a previously hashed value.

    Parameters:
    - secret_value (str): The secret value to verify.
    - hashed_value (str): The previously hashed value in the format 'salt:hash'.

    Returns:
    - bool: True if the secret value matches the hash, False otherwise.
    """
    # Split the hashed value into salt and hash components
    salt_hex, hash_hex = hashed_value.split(':')

    # Convert the salt from hexadecimal to bytes
    salt = bytes.fromhex(salt_hex)

    # Hash the secret value with the provided salt
    new_hash = hash_secret(secret_value, salt=salt)

    # Compare the newly generated hash with the provided hash
    return new_hash == hashed_value

# Example usage:
if __name__ == "__main__":
    secret = "wtfe286T4P3zv49MJyJqcL3p#5uw*rz*4+ncw$5pk"

    # Hash the secret
    hashed_secret = hash_secret(secret)
    print(f"Hashed Secret: {hashed_secret}")

    # Verify the secret
    is_valid = verify_secret(secret, hashed_secret)
    print(f"Is the secret valid? {is_valid}")

    # Test with an incorrect secret
    is_valid = verify_secret("wrong_secret_value", hashed_secret)
    print(f"Is the secret valid with wrong input? {is_valid}")
