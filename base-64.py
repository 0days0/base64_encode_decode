import base64

print("Encode >> 1", "Decode >> 2", sep="\n")
a = input("Your Choice: ")

if a == "1":
    text = input("Encode Text: ")
    text_bytes = text.encode('ascii')
    b64_bytes = base64.b64encode(text_bytes)
    b64_text = b64_bytes.decode('ascii')
    print("Your encoded text:\n{}".format(b64_text))
elif a == "2":
    text = input("Decode Text: ")
    text_bytes = text.encode('ascii')
    b64_bytes = base64.b64decode(text_bytes)
    b64_text = b64_bytes.decode('ascii')
    print("Your decoded text:\n {}".format(b64_text))
else:
    print("Exiting the program...")    