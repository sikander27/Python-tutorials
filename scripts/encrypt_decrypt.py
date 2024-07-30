import hashlib
import os
import time
from datetime import datetime, timedelta


def hash_secret(secret_value: str, salt: bytes = None) -> str:
    if salt is None:
        salt = os.urandom(16)
    secret_value_bytes = secret_value.encode('utf-8')
    timestamp = str(int(time.time())).encode('utf-8')  # Current timestamp in seconds
    salted_secret = salt + secret_value_bytes + timestamp
    hash_object = hashlib.sha256(salted_secret)
    hash_hex = hash_object.hexdigest()
    return f"{salt.hex()}:{hash_hex}:{timestamp.decode('utf-8')}"


def verify_secret(secret_value: str, hashed_value: str, max_age_seconds: int = 300) -> bool:
    salt_hex, hash_hex, timestamp_str = hashed_value.split(':')
    timestamp = int(timestamp_str)
    current_time = int(time.time())

    # Check if the hash is older than max_age_seconds
    if current_time - timestamp > max_age_seconds:
        return False

    salt = bytes.fromhex(salt_hex)
    secret_value_bytes = secret_value.encode('utf-8')
    salted_secret = salt + secret_value_bytes + timestamp_str.encode('utf-8')
    hash_object = hashlib.sha256(salted_secret)
    new_hash_hex = hash_object.hexdigest()

    return new_hash_hex == hash_hex

# Example usage:
if __name__ == "__main__":
    secret = "my_super_secret_value"

    # Hash the secret
    hashed_secret = hash_secret(secret)
    print(f"Hashed Secret: {hashed_secret}")

    # Verify the secret (within 5 minutes)
    is_valid = verify_secret(secret, hashed_secret)
    print(f"Is the secret valid? {is_valid}")

    # Test with an incorrect secret
    is_valid = verify_secret("wrong_secret_value", hashed_secret)
    print(f"Is the secret valid with wrong input? {is_valid}")

    # Test with a timestamp older than 5 minutes
    old_timestamp = str(int(time.time()) - 600)
    old_hashed_secret = hash_secret(secret, salt=os.urandom(16))[:-10] + old_timestamp
    is_valid = verify_secret(secret, old_hashed_secret)
    print(f"Is the old secret valid? {is_valid}")
