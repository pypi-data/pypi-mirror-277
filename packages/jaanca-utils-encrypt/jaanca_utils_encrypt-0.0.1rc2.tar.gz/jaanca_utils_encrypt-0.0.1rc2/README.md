<p align="center">
    <em>jaanca public libraries</em>
</p>

<p align="center">
<a href="https://pypi.org/project/jaanca-utils-encrypt" target="_blank">
    <img src="https://img.shields.io/pypi/v/jaanca-utils-encrypt?color=blue&label=PyPI%20Package" alt="Package version">
</a>
<a href="(https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-%5B%3E%3D3.8%2C%3C%3D3.11%5D-blue" alt="Python">
</a>
</p>


---

#  A tool library created by jaanca

* **Python library**: A tool library created by jaanca that allows encrypting and decrypting in different ways.

[Source code](https://github.com/jaanca/python-libraries/tree/main/jaanca-utils-encrypt)
| [Package (PyPI)](https://pypi.org/project/jaanca-utils-encrypt/)
| [Samples](https://github.com/jaanca/python-libraries/tree/main/jaanca-utils-encrypt/samples)

---

# library installation
```console
pip install jaanca-utils-encrypt --upgrade
```

---
# Example of use

Public and private keys can be generated and saved in text with line separator single_line=False or in a single line with single_line=True.

```Python
from jaanca_chronometer import Chronometer
from jaanca_utils_encrypt import EncryptionRSA

chronometer=Chronometer()
single_line=False
encryption_rsa=EncryptionRSA()

chronometer.start()
encrypt_publicKey, decrypt_privateKey = encryption_rsa.create_keys(len_key_in_bits=2048,single_line=single_line)
chronometer.stop()
create_keys=chronometer.get_elapsed_time()

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
print(f"time elapsed for create_keys: {create_keys}")
print(f"time elapsed for encrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {encrypt_with_private_key_pkcs1}")
print(f"time elapsed for decrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {decrypt_with_private_key_pkcs1}")

# Output

# encrypted_text: tIN2dAOFJ+iwhPR2CRlkyPcKQpr5QmPwXGWTJvMVwrh2FTt67dYhbTnte69Tp76v5KlJSaFoXrcge8wNkxrUtR/9hur7RBdtAQrZG+fMsAKrSNYLedfiaYHxcSmgMvx+Bl81YXaSW+dNGkNVJCp92zhAjps0UkB1KVjsEjEH3eFtb+BxY2WikzCHswm47kmNl9yhSMDHsJo3n8zrEA7Ucrge6CtQ4pofswYFEk84lwyaIQWtPO2Tg7IamdO5DYu82zf3heAm+qqhEPNWT9Ua85YyABUF4DDmRRbFYUh2OxsoePZuFhLlg9PAag0M58Dr4I42AkS6Zur5geBptS/mxA==

# decrypted_text: Hello World

# time elapsed for create_keys: 00:00:02
# time elapsed for encrypt_with_private_key_pkcs1 HH:mm:ss: 00:00:00
# time elapsed for decrypt_with_private_key_pkcs1 HH:mm:ss: 00:00:00


```

---

# Semantic Versioning

jaanca-utils-encrypt < MAJOR >.< MINOR >.< PATCH >

* **MAJOR**: version when you make incompatible API changes
* **MINOR**: version when you add functionality in a backwards compatible manner
* **PATCH**: version when you make backwards compatible bug fixes

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## [0.0.1rcX] - 2024-06-05
### Added
- First tests using pypi.org in develop environment.

## [0.1.X] - 2024-06-05
### Added
- Completion of testing and launch into production.

