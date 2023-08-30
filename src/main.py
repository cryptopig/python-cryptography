from cryptography.fernet import Fernet


# ______________________________________________________

# ENCRYPT FUNCTION

def encrypt(file_to_encrypt = []):
  key = Fernet.generate_key()
  
  
  with open("thekey.key", "wb") as thekey:
    thekey.write(key) # creates thekey.key file that stores the key
  
  with open("thekey.key", "rb") as thekey:
    key = thekey.read() # sets the key to encrypt files to the key in thekey.key file
  
  fernet = Fernet(key) # initializing the key object with its methods
  for f in file_to_encrypt:
    try:
      with open(f, "rb") as file:
        original = file.read()
    except FileNotFoundError:
      print("Please input a valid file name. ")
 
  
    encrypted = fernet.encrypt(original) # encrypts file using stored key
    
    with open(f, "wb") as encrypted_file:
      encrypted_file.write(encrypted)
    
    print(f"{f} has been encrypted.")

# ______________________________________________________


# DECRYPT FUNCTION

def decrypt(file_to_decrypt = []):
  
  with open("thekey.key", "rb") as thekey:
    key = thekey.read()
  
  fernet = Fernet(key) # key for decryption
  
  for i in file_to_decrypt: 
    try:
      with open(i, "rb") as file_enced:
        encrypted = file_enced.read()
    except FileNotFoundError: 
      print("Please input a valid file name.")
      exit()
  
    decrypted = fernet.decrypt(encrypted)
    
    with open(i, "wb") as file_decrypted:
      file_decrypted.write(decrypted)
    
    print(f"{i} has been decrypted.")

# ______________________________________________________

# CREATION FUNCTION

def create(file_to_create = [], content = []):
  for i in file_to_create:
    with open(i, "w") as create:
      for j in content:
        create.write(j)

# ______________________________________________________

# Running appropriate function


# User wants to encrypt

while True:
  encrypt_or_decrypt = input("\nWould you like to encrypt [e], decrypt [d], create a file [c], or quit [q]? ")
  
  if encrypt_or_decrypt == "e" or encrypt_or_decrypt == "encrypt":
    files_to_input = []
    n = int(input("How many files would you like to encrypt? "))
    for i in range(0, n):
      element = input(f"Filename {i}: ")
      files_to_input.append(element)
      
    encrypt(file_to_encrypt = files_to_input[:])
  
  
  # User inputs decrypt
  elif encrypt_or_decrypt == "d" or encrypt_or_decrypt == "decrypt":
    files_to_input = []
    n = int(input("How many files would you like to decrypt? "))
    for i in range(0, n):
      element = input(f"Filename {i}: ")
      files_to_input.append(element)
    decrypt(file_to_decrypt=files_to_input[:])
  
  
  # User wants to create files
  elif encrypt_or_decrypt == "c" or encrypt_or_decrypt == "create":
    n = int(input("How many files would you like to create? "))
    files_to_input = []
    contents = []
    for i in range(0, n):
      element = input(f"Filename {i}: ")
      files_to_input.append(element)
      content_input = input("What would you like to input? ")
      contents.append(content_input)
    create(file_to_create=files_to_input[:], content = contents[:])
      
  else:
    print("Exiting... ")
    exit()
