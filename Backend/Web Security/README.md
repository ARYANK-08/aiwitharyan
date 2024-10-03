# MD5 and Cryptographic Hash Functions

### What is MD5?

MD5 (Message-Digest Algorithm 5) is a cryptographic hash function that converts a message of any length into a fixed-length hash value of **16 bytes** (128 bits). It is primarily used to verify data integrity, as any changes in the original message will result in a completely different hash output.

### Example:

```python
import hashlib

value = hashlib.md5("hello world".encode("utf-8")).hexdigest()
print(value)  # Output: 5eb63bbbe01eeed093cb22bb8f5acdc3
```

In this example, the string `"hello world"` is converted into a hash, which is a **32-character hexadecimal number**.

---

### Working of the MD5 Algorithm

MD5 follows several steps to generate a hash:

#### 1. Append Padding Bits
MD5 starts by adding padding bits to the original message, ensuring that the length of the message is 64 bits less than a multiple of 512 bits.

For instance, a message of 1000 bits would be padded with 472 bits, bringing the total to 1472 bits. This is because **1472 is 64 bits less than 1536 (512 * 3)**.

```text
Length = 512 * i - 64, where i = 1, 2, 3...
```

#### 2. Append Length Bits
Next, MD5 appends **64 bits** that represent the original message length, making the final length a multiple of 512 bits.

#### 3. Initialize MD Buffer
MD5 uses four buffers, each of **32 bits**:

- A = `0x67425301`
- B = `0xEDFCBA45`
- C = `0x98CBADFE`
- D = `0x13DCE476`

These buffers are initialized and will hold intermediate and final values.

#### 4. Process Each 512-bit Block
MD5 processes the message in 512-bit blocks. This process involves **64 operations** divided into four rounds. Each round uses different logical operations (`AND`, `OR`, `XOR`, `NOT`) and functions **F, G, H,** and **I**.

The steps include:
- **Modulo addition** of 32-bit constants.
- **Left shifts** of intermediate results.
- Reassigning values between buffers A, B, C, and D.

After processing all blocks, the final **message digest** is stored in buffers A, B, C, and D.

---

### Example: Hashing a Custom Message

```python
import hashlib

inputstring = "This is a message sent by a computer user."
output = hashlib.md5(inputstring.encode())
print("Hash of the input string:")
print(output.hexdigest())
```

**Output:**

```text
Hash of the input string:
922547e866c89b8f677312df0ccec8ee
```

---

### Applications of MD5

MD5 is widely used for:

1. **Data Integrity**: Comparing hashes of files or messages to check if they've been tampered with.
2. **Secure Password Storage**: Storing user passwords as hashes rather than plaintext.
3. **Version Control**: Verifying the integrity of different file versions.

However, due to its vulnerabilities, MD5 is no longer recommended for highly secure applications like **digital signatures**. It has been replaced by more secure algorithms such as **SHA-256**.

---

## What is SHA-1?

SHA-1 (Secure Hash Algorithm 1) is another cryptographic hash function developed by the **NSA**. It produces a hash value of **160 bits** (or a **40-digit hexadecimal number**). Like MD5, it ensures data integrity and is widely used in **digital signatures**, **data protection**, and **password storage**.

Hashing is similar to encryption, the only difference between hashing and encryption is that hashing is one-way, meaning once the data is hashed, the resulting hash digest cannot be cracked, unless a brute force attack is used. See the image below for the working of SHA algorithm. SHA works in such a way even if a single character of the message changed, then it will generate a different hash. For example, hashing of two similar, but different messages i.e., Heaven and heaven is different. However, there is only a difference of a capital and small letter.
The determinism of SHAs is one of reasons every SSL certificate on the Internet is required to have been hashed with a SHA-2 function.

What is SHA used for?
As previously mentioned, Secure Hashing Algorithms are required in all digital signatures and certificates relating to SSL/TLS connections, but there are more uses to SHAs as well. Applications such as SSH, S-MIME (Secure / Multipurpose Internet Mail Extensions), and IPSec utilize SHAs as well.  SHAs are also used to hash passwords so that the server only needs to remember hashes rather than passwords.

In this way, if an attacker steals the database containing all the hashes, they would not have direct access to all of the plaintext passwords, they would also need to find a way to crack the hashes to be able to use the passwords. SHAs can also work as indicators of a file’s integrity. If a file has been changed in transit, the resulting hash digest created from the hash function will not match the hash digest originally created and sent by the file’s owner.

In blockchain technology, particularly in cryptocurrencies like Bitcoin, SHA-256 plays a crucial role. It is integral to the mining process, where it helps solve complex mathematical puzzles to validate and add new transactions to the blockchain. 

---

### MD5 vs. SHA-1

| **MD5**                       | **SHA-1**                      |
|-------------------------------|--------------------------------|
| 128-bit message digest         | 160-bit message digest         |
| Faster than SHA-1              | Slower than MD5                |
| Less secure, vulnerable to attacks | More secure but still vulnerable |
| Used for basic checksums and password storage | Used in digital signatures and certificates |
| Introduced in 1992             | Introduced in 1995             |

---

### Real-World Applications of SHA-1

1. **Digital Signatures**: Used in verifying the authenticity of documents.
2. **SSL/TLS Certificates**: Ensures secure communication between web browsers and servers.
3. **Password Hashing**: Passwords are stored as SHA-1 hashes instead of plaintext.
4. **File Integrity**: Verifies if files have been modified in transit.

---

### Example: Real-World Impact of SHA Algorithms

SHA algorithms are crucial in technologies like **blockchain**. For example, **SHA-256** is integral to the mining process in cryptocurrencies like Bitcoin. It helps in solving complex mathematical puzzles to validate transactions and add them to the blockchain.

---

## What is Scrypt?

**Scrypt** is a cryptographic key derivation function designed to make brute-force attacks difficult by being computationally and memory-intensive. It's widely used in **password hashing** and **cryptocurrency mining** (like **Litecoin**).

Unlike MD5 or SHA-1, which focus on fast computations, Scrypt adds complexity by using a large amount of memory along with CPU-intensive operations. This makes it costly and challenging for attackers to run large-scale, parallel brute-force attacks using **GPUs** or **ASICs**.

---

### Example: Where Scrypt is Used

1. **Password Hashing**: Commonly used in web applications to store passwords securely.
2. **Cryptocurrency Mining**: Scrypt is used in mining altcoins like **Litecoin** as it requires more memory to solve puzzles compared to Bitcoin's SHA-256.

---

### Summary

- **MD5**: Fast, but offers weak security. Good for basic checksums and non-critical data.
- **SHA-1**: Better than MD5, widely used but has vulnerabilities. Replaced by **SHA-2** in modern security systems.
- **Scrypt**: Highly secure due to its computational and memory demands. Perfect for password hashing and cryptocurrency mining.
