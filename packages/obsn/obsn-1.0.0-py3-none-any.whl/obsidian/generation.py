import random
from string import ascii_letters, digits

possible_letters = ascii_letters + digits

def generate_udid(start: int = 100_000, end: int = 100_000_000) -> str:
    return "S" + str(random.randint(start, end))

def generate_rs(n: int) -> str:
    return ('').join(random.choices(possible_letters, k=n))

def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return ('-').join(map(generate_rs, parts))

def generate_upload_seed(data: str, chars: int = 50) -> str:
    if len(data) < chars:
        return data
    step = len(data) // chars
    return data[::step][:chars]

def generate_leaderboard_seed(jumps: int, percentage: int, seconds: int, has_played: bool = True) -> int:
    return 1482 * (has_played + 1) + (jumps + 3991) * (percentage + 8354) + ((seconds + 4085) ** 2) - 50028039

def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)
    string = ('').join(map(str, values))
    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor_cipher(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()
    return final