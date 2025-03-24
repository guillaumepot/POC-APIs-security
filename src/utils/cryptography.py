#src/utils/hashing.py

# Lib
import os


def generate_secret_key() -> bytes:
    return os.urandom(32)


if __name__ == '__main__':
    print(f"Random secret key: {generate_secret_key()}")