# Reversing a sentense and swapping the cases, that is upper case to lower and lower to uppercase using python
sentence = "LANguage nEW is PYTHOn"
words = sentence.split(" ")
op_sentence = " ".join(reversed(words))
print(op_sentence.swapcase())
