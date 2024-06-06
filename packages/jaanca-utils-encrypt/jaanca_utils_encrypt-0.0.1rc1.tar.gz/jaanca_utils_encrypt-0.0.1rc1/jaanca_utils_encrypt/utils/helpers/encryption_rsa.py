import base64
import rsa

class EncryptionRSA():
    def create_keys(self,len_key_in_bits:int=2048,single_line:bool=False)->tuple[str,str]:
        '''Description
        Return RSA keys to be used in methods of this class

        :param lenKeyInBits:int: Generate Keysize (bits)
        nbits (single process): 128 -> 0.01 sec.
        nbits (single process): 256 -> 0.03 sec.
        nbits (single process): 384 -> 0.09 sec.
        nbits (single process): 512 -> 0.11 sec.
        nbits (single process): 1024 -> 0.79 sec.
        nbits (single process): 2048 -> 6.55 sec.
        nbits (single process): 3072 -> 23.4 sec.
        nbits (single process): 4096 -> 72.0 sec.

        
        :return tuple:str,str: plane text for public_key and private_key RSA standard
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
        encryptTextBase64=base64.b64encode(encryptTextRSA).decode()
        return encryptTextBase64

    def dencrypt_with_private_key_pkcs1(self,encryptTextBase64:str,private_key:str,single_line:bool=False)->str:
        '''Description
        :param encryptTextBase64:str    : string to decrypt in base 64
        :param private_key:str          : string of RSA PRIVATE KEY
        :return str                     : decrypted string in plaintext
        '''
        if single_line is True:
            private_key=private_key.replace('\\n', '\n')
        encryptTextRSA=base64.b64decode(str(encryptTextBase64).encode())
        plane_text = rsa.decrypt(encryptTextRSA, rsa.private_key.load_pkcs1(private_key)).decode()
        return plane_text
