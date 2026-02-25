# homophonic_decrypt_file.py

from collections import Counter

# ----------------------------
# CONFIG
# ----------------------------
INPUT_FILE = "11.txt"
OUTPUT_FILE = "decrypted_partial.txt"

# ----------------------------
# Your known key (char -> numbers)
# ----------------------------
raw_key = {
    ',':  [158],
    '.':  [770],
    '-':  [659],
    '"':  [799],
    "'":  [648],
    ';':  [662],
    '!':  [460],
    '?':  [296],
    '_':  [477],
    '(':  [885],
    ')':  [275],
    ':':  [331],
    '\n': [955, 506, 309],
    '4':  [394],
    '7':  [186],
    'I': [380, 433, 672, 638],
    ' ': [165, 825, 530, 765, 262, 451, 948, 613, 188, 586, 448, 686, 256, 395, 848, 436, 395, 317],
    'T': [175, 565, 822, 386, 565, 303, 370, 273, 679],
    'N': [496, 734, 201],
    'S': [103, 783],

}

# Build inverse key: number -> char
key = {}
for ch, nums in raw_key.items():
    for n in nums:
        key[f"{n:03d}"] = ch   # force 3-digit strings


# Helpers
def read_cipher(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def clean(text):
    return "".join(c for c in text if c.isdigit())

def chunk(text, n=3):
    return [text[i:i+n] for i in range(0, len(text), n)]

def decrypt(chunks, key):
    out = []
    unknown = Counter()

    for c in chunks:
        if c in key:
            out.append(key[c])
        else:
            out.append(f"[{c}]")
            unknown[c] += 1

    return "".join(out), unknown


# RUN
cipher_raw = read_cipher(INPUT_FILE)

digits = clean(cipher_raw)
chunks = chunk(digits, 3)

plaintext, unknowns = decrypt(chunks, key)

# Save output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(plaintext)
