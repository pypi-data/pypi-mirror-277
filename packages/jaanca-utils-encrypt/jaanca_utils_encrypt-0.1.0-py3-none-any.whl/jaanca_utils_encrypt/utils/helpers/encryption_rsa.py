import base64
import rsa

class EncryptionRSA():
    '''Description
    
    ### Example
    ```Python
    from jaanca_chronometer import Chronometer
    from jaanca_utils_encrypt import EncryptionRSA

    chronometer=Chronometer()
    single_line=False
    encryption_rsa=EncryptionRSA()

    chronometer.start()
    encrypt_publicKey, decrypt_privateKey = encryption_rsa.create_keys_pkcs1(len_key_in_bits=2048,single_line=single_line)
    chronometer.stop()
    create_keys_pkcs1=chronometer.get_elapsed_time()

    chronometer.start()
    plane_text="Hello World"
    encrypted_text = encryption_rsa.encrypt_with_private_key_pkcs1(plane_text,encrypt_publicKey)
    chronometer.stop()
    encrypt_with_private_key_pkcs1=chronometer.get_elapsed_time()

    chronometer.start()
    decrypted_text = encryption_rsa.decrypt_with_private_key_pkcs1(encrypted_text,decrypt_privateKey)
    chronometer.stop()
    decrypt_with_private_key_pkcs1=chronometer.get_elapsed_time()

    print(f"encrypted_text: {encrypted_text}")
    print(f"decrypted_text: {decrypted_text}")
    print(f"time elapsed for create_keys_pkcs1: {create_keys_pkcs1}")
    print(f"time elapsed for encrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {encrypt_with_private_key_pkcs1}")
    print(f"time elapsed for decrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {decrypt_with_private_key_pkcs1}")
    ```
    '''
    def create_keys_pkcs1(self,len_key_in_bits:int=2048,single_line:bool=False)->tuple[str,str]:
        '''Description
        Return RSA keys to be used in methods of this class
        :param single_line:bool: Public and private keys can be generated and saved in text with line separator single_line=False or in a single line with single_line=True.
        :param len_key_in_bits:int: Generate Keysize (bits).

        nbits (single process): 128 -> 0.01 sec.
        nbits (single process): 256 -> 0.03 sec.
        nbits (single process): 384 -> 0.09 sec.
        nbits (single process): 512 -> 0.11 sec.
        nbits (single process): 1024 -> 0.79 sec.
        nbits (single process): 2048 -> 6.55 sec.
        nbits (single process): 3072 -> 23.4 sec.
        nbits (single process): 4096 -> 72.0 sec.
        
        :return tuple:str,str: plane text for public_key and private_key RSA standard

        ### Example

        ```Python
        from jaanca_chronometer import Chronometer
        from jaanca_utils_encrypt import EncryptionRSA

        chronometer=Chronometer()
        single_line=False
        encryption_rsa=EncryptionRSA()
        chronometer.start()
        encrypt_publicKey, decrypt_privateKey = encryption_rsa.create_keys_pkcs1(len_key_in_bits=2048,single_line=single_line)
        chronometer.stop()

        print(" encrypt_publicKey ")
        print(encrypt_publicKey)

        print(" decrypt_privateKey ")
        print(decrypt_privateKey)

        print(f"time elapsed {chronometer.get_format_time()}: {chronometer.get_elapsed_time()}")

        ```
        '''
        public_key, private_key = rsa.newkeys(len_key_in_bits)
        public_key = public_key.save_pkcs1().decode()
        private_key = private_key.save_pkcs1().decode()
        if single_line is True:
            public_key=public_key.replace('\n', '\\n')
            private_key=private_key.replace('\n', '\\n')
        return public_key, private_key

    def encrypt_with_private_key_pkcs1(self,plane_text:str,public_key:str,single_line:bool=False)->str:
        '''Description
        :param plane_text:str   : string to encrypt
        :param public_key:str   : string of RSA PUBLIC KEY
        :return str             : base 64 encrypted text
        '''
        if single_line is True:
            public_key=public_key.replace('\\n', '\n')
        encryptTextRSA = rsa.encrypt(str(plane_text).encode(),rsa.PublicKey.load_pkcs1(public_key))
        encrypt_text_base64=base64.b64encode(encryptTextRSA).decode()
        return encrypt_text_base64

    def decrypt_with_private_key_pkcs1(self,encrypt_text_base64:str,private_key:str,single_line:bool=False)->str:
        '''Description
        :param encrypt_text_base64:str  : string to decrypt in base 64
        :param private_key:str          : string of RSA PRIVATE KEY
        :return str                     : decrypted string in plaintext
        '''
        if single_line is True:
            private_key=private_key.replace('\\n', '\n')
        encryptTextRSA=base64.b64decode(str(encrypt_text_base64).encode())
        plane_text = rsa.decrypt(encryptTextRSA, rsa.PrivateKey.load_pkcs1(private_key)).decode()
        return plane_text
