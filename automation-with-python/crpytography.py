# this a manual way of doing this in python

cipher = {chr(x):chr(x+1) for x in range (97,123)}
print("ans1  ")
print(cipher)
cipher['z'] = 'a'
print("ans2 ")
print(cipher)

parts = [cipher[letter] for letter in "gorgonzola"]
print("ans3 ")
print(parts)

print("ans4")
cipher1 = {chr(x):chr(x == range(50)) for x in range (97,123)}
print(cipher1)

decipher = {value:key for key,value in cipher.items()}

print("dec1")
print(decipher)

parts2 = [decipher[letter] for letter in parts ]

print("dec2")
print(parts2)

# the string function has a cipeher lib built into it, example below

caesar = str.maketrans("abcedfghijklmnopqrstuvwxyz","bcdefghjiklmnopqrstuvwxyza")

print("and5")

print(caesar)

decipher_caesar=str.translate("gorgonzola",caesar)

print("ans6")
print(decipher_caesar)

