#src/utils/hashing.py

# Lib
from passlib.context import CryptContext

# Init context
context = CryptContext(
                        schemes = ["argon2"],
                        deprecated = "auto",
                        argon2__time_cost = 4,
                        argon2__memory_cost = 2**15,
                        argon2__parallelism = 4,
                        argon2__hash_len = 32
                        )



def hash_string(to_hash: str) -> str:
    return context.hash(to_hash)

def verify_hash(to_verify:str, hashed_value:str) -> bool:
        return context.verify(to_verify, hashed_value)



if __name__ == '__main__':
    to_hash = input("Enter the string to hash: \n")
    hashed_string = hash_string(to_hash)
    print(f"your hash: {hashed_string}")