print('hello')  # ASCII
print(ord('a'))
print(ord('A'))
a = 'hello'
chars = []

for i in a:
    chars.append(ord(i))

print(chars)

s = ''
for i in chars:
    s += chr(i)
print(s)

for i in range(128):
    print(chr(i), end=" ")

print()

for i in range(1000, 1200):
    print(chr(i), end=" ")

print()

print(hex(ord('h')))
bb = b'\x68'
print(type(bb))
print(bb.decode())
