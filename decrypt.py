import sys

from math import sqrt


def keygen(characters):
    '''
    This is your key generator. It takes a list of characters, in any random order, and 
    converts them into a key using the same logic as the Polybius Square (i.e. one letter gets two numbers
    according to the placement on the table (row and column)).
    
    Although it is based off the Polybius square, it is enhanced: it allows more than 25 characters,
    it allows any combination of characters, and it allows you to switch characters so that you get your own
    secret unique key. For instance, in the Polybius square the usual order is "A,B,C,D(...)". Here you can, if you want
    use something like "E,F,A,B,(...)"
    
    Feel free to try it out by either using the 'mykey1.txt', 'mykey2.txt' files
    provided, or by modifying the 'mykey1.txt' in any way you like.
    '''


    sub_tup=()
    tup=()
    if int(sqrt(len(characters)))**2 == (int(len(characters))):    
        tup_number = int(sqrt(len(characters)))
    else:
        tup_number = int(sqrt(len(characters)))+1
    n=len(characters)/tup_number
    for i in range(len(characters)):
        sub_tup = sub_tup + (characters[i],)
        if len(sub_tup)>=n:
            tup= tup + (sub_tup,)
            sub_tup=()
    if sub_tup != ():
        tup= tup + (sub_tup,)
    return tup


def get_character_final(code, used_key):
    ''' 
    This function takes an encoded character (composed by two numbers),
    takes the key used for encryption, and returns the decrypted character
    '''
    if code == 'XX':
        return '?'
    else:
        tuple(code)
        row=eval(code[0])
        col=eval(code[1])
        return used_key[row][col]
    
def decrypt(encrypted_message, used_key):
    '''
    This function generalizes the decryption of one character defined by the get_character_final
        function , and decrypts the whole message.
    
    '''
    row=0
    col=2
    decrypted_message=''   
    for i in range(int(len(encrypted_message)/2)):
        code = encrypted_message[row:col]
        decrypted_message = decrypted_message + get_character_final(code,used_key)
        row=row+2
        col=col+2
    return decrypted_message

def generate_decrypted_message():
    ''' 
    This is the final decrypt function with all functionalities.
    Given the encrypted message and the key used to encrypt it, the user gets the original message back.
    
    Example: User enters the .txt file of the encrypted message and the .txt file of the key used to encrypt
    
            User receives a generated .txt file called "decrypted_message" with the decrypted message
            '''
    try:
        filedirect=input("\n|\n|\n|Enter name of the .txt file you want to decrypt: ")+".txt"
        with open(file=filedirect, mode="r") as f:
            filedata=f.read()
        message=filedata
    except:
        print("""\n|\n|\nAN ERROR HAS OCCURRED. Please make sure you entered the correct file name,
and that the file is in the same directory you are running this script from.\n|\n|""")
        input("Press any key to exit.")
        sys.exit(-1)
    
    try:
        key_file_name=input("\n|\n|\n|Enter decryption key .txt file name: ")+".txt"
        with open(file = key_file_name, mode="r") as f:
            key1=f.read()
    except:
        print("""\n|\n|\nAN ERROR HAS OCCURRED. Please make sure you entered the correct file name,
and that the file is in the same directory you are running this script from.\n|\n|""")
        input("Press any key to exit.")
        sys.exit(-1)
        
    key1=list(key1)
    key1=keygen(key1)
    decrypt(message,key1)
    with open("decrypted_message.txt",mode="w") as f_out:
        f_out.write(decrypt(message, key1))
    print("\n|\n|\n File successfully decrypted. Check the directory to find the decrypted file.\n\n|")
    
generate_decrypted_message()

input("Press any key to exit.")
sys.exit(-1)
