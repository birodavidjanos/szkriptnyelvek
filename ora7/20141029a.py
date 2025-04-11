#"yunkostanotkatan"
#„So you really love the ilon sata zhone music.”

hex_input = """
4D69 61 6E657665 616E6E616B 61 68656C7969
6B617063736F6C6F6B6F7A706F6E746E616B2C 61686F6C
6D616A646E656D 656C6B617074616B
"""

# Összes hexaszó szóközökkel elválasztva → listába
hex_words = hex_input.split()

# Minden szót 4 karakteres blokkokra bontunk, ha kell zfill-lel kiegészítjük
hex_blocks = []
for word in hex_words:
    for i in range(0, len(word), 4):
        block = word[i:i+4].zfill(4)
        hex_blocks.append(block)

# A 4 karakteres hex blokkokat összefűzzük
hex_string = ''.join(hex_blocks)

# Hex string → bájtok
byte_data = bytes.fromhex(hex_string)

# UTF-16 big-endian dekódolás
decoded = byte_data.decode('utf-16-be')

print(decoded)
