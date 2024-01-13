''''''

'''
base64: <Description>
'''
import base64

message = "GeeksForGeeks is the best"
print("Normal message : ", message)
en_message = message.encode("ascii")
print("Encode message : ", en_message)

bs64_msg = base64.b64encode(en_message)
print("Base64 message : ", bs64_msg)

bs64_dec_msg = bs64_msg.decode("ascii")

print(f"Decoded string : {bs64_dec_msg}")