# String

text = "X-DSPAM-Confidence:    0.8475"
find=text.find("0")
find2=text[find: ]
print(float(find2))