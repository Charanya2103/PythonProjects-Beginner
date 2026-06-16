#Caesar Cipher(project)
char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n=input("Type 'e' for encryption, type 'd' for decryption:")
text=input("Type your message:")
shift=int(input("Type the shift number:"))
def encrypt(text,shift):
  res=""
  for i in range(len(text)):
    result=(i+shift)%26
    res+=char[result]
  return res
def decrypt(text,shift):
  res=""
  for i in range(len(text)):

    result=(-shift)%26
    if result<0:
      result+=26
    res+=char[result]
  return res
if n=="e":
  print(encrypt(text,shift))
else:
  print(decrypt(text,shift))
