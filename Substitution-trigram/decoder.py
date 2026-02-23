# decoder.py

ciphertext = """
231371775256783199760881717395130368496299565737395457303448154737130380734496765692443101680386256431621939201586306796457381573756765975805797722638586796312372847496613111213495760380201586548805851833857457760103822
""".strip().replace(" ", "").replace("\n", "")

# Known mappings
mapping = {
    "391": " ",
    "615": "A",
    "739": "B",
    "211": "C",
    "737": "D",
    "606": "E",
    "896": "G",
    "184": "F",
    "468": "H",
    "441": "I",
    "000": "J",
    "218": "K",
    "954": "L",
    "464": "M",
    "525": "N",
    "622": "O",
    "406": "P",
    "053": "Q",
    "303": "R",
    "599": "S",
    "657": "T",
    "949": "U",
    "120": "V",
    "961": "W",
    "044": "X",
    "867": "Y",
    "686": "Z",
    "287": ".",
    "452": ",",
    "174": ":",
}

def chunk(text, n=3):
    return [text[i:i+n] for i in range(0, len(text), n)]

def decrypt(chunks, mapping):
    plaintext = []
    unknown = set()

    for c in chunks:
        if c in mapping:
            plaintext.append(mapping[c])
        else:
            plaintext.append(f"[{c}]")   # mark unknowns
            unknown.add(c)

    return "".join(plaintext), unknown

chunks = chunk(ciphertext, 3)
plaintext, unknown_codes = decrypt(chunks, mapping)

print("\n--- DECRYPTED TEXT ---\n")
print(plaintext)

print("\n--- UNKNOWN CODES ---\n")
for code in sorted(unknown_codes):
    print(code)