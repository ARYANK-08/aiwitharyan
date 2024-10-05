# Web security : the beauty of safe internet :D 

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




### HTTPS (Hypertext Transfer Protocol Secure)

HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP designed to secure data transmission between a client (e.g., browser) and a server. It uses encryption through SSL/TLS protocols to ensure data confidentiality, integrity, and authenticity. This prevents sensitive information, like login credentials or payment details, from being intercepted or tampered with by attackers. HTTPS is essential for securing web applications and has become a standard for most websites, especially those handling user data, as it helps protect against man-in-the-middle attacks and eavesdropping.

#### **What is HTTPS?**
HTTPS stands for Hypertext Transfer Protocol Secure. It’s the secure version of HTTP, which is the primary protocol used for transmitting data on the web. HTTPS encrypts data to enhance the security of data transfers, particularly when sensitive information, such as login credentials or financial information, is transmitted. Websites requiring user authentication should implement HTTPS to ensure secure communication.

Modern web browsers flag non-HTTPS sites as "not secure," making it essential for websites handling user data to adopt HTTPS for trust and safety.

#### **How does HTTPS work?**
HTTPS employs the Transport Layer Security (TLS) protocol (previously known as Secure Sockets Layer or SSL) for encryption. It operates using an asymmetric public key infrastructure, involving two keys:
- **Private Key:** Controlled by the website owner and kept secure on the web server, used for decrypting information.
- **Public Key:** Available to everyone and used for encrypting information sent to the server.

1. **Establishing a Secure Connection:** When a client connects to a server using HTTPS, the server provides its SSL certificate containing the public key. This initiates a process known as the SSL/TLS handshake, where both parties verify each other’s identity and agree on encryption methods.

2. **Encryption:** Once the handshake is completed, the client and server use symmetric encryption (using session keys) to secure the communication.

#### **Importance of HTTPS**
- **Data Protection:** Encrypts information, making it unreadable to anyone intercepting the data (e.g., on public Wi-Fi).
- **Integrity:** Ensures that the data sent and received has not been altered or tampered with.
- **Authentication:** Confirms that users are communicating with the genuine server and not an imposter.

![image](https://github.com/user-attachments/assets/e131da2e-7d51-43a5-8f47-ef22272bd169)


#### **What happens if a website doesn’t have HTTPS?**
Without HTTPS, data is transmitted in plain text, making it vulnerable to interception and manipulation. Potential risks include:
- **Data Interception:** Attackers can easily read and capture sensitive information.
- **Content Injection:** ISPs or malicious third parties can inject unwanted advertisements or malicious content into webpages.
- **Reduced Trust:** Browsers mark non-HTTPS sites as "not secure," leading to decreased user trust.

#### **What port does HTTPS use?**
HTTPS operates over **port 443**, while HTTP uses **port 80**. This distinction helps in routing traffic correctly and securing connections.

#### **Difference between HTTPS and HTTP**
- **Encryption:** HTTPS uses SSL/TLS to encrypt data, while HTTP transmits data in plain text.
- **Security:** HTTPS provides a secure communication channel; HTTP does not.

#### **Understanding the TLS Handshake**
A TLS handshake is the process that establishes a secure connection. Here’s how it works:
1. **Client Hello:** The client sends a message to the server indicating supported TLS versions and cipher suites.
2. **Server Hello:** The server responds with its SSL certificate and selected cipher suite.
3. **Authentication:** The client verifies the server's SSL certificate with a trusted Certificate Authority (CA).
4. **Session Keys Creation:** Both parties generate session keys for symmetric encryption.

#### **TLS vs. SSL**
SSL was the original protocol for securing communications, but it has been largely replaced by TLS due to security vulnerabilities. The terms SSL and TLS are often used interchangeably, but the latest standard is TLS.

#### **Benefits of HTTPS**
- **Enhanced Security:** Protects user data during transmission.
- **Improved SEO:** Search engines favor HTTPS websites, enhancing visibility.
- **Trust and Credibility:** Websites with HTTPS are viewed as more trustworthy by users.

In summary, implementing HTTPS is essential for any website, especially those handling sensitive user information, to ensure security, privacy, and trustworthiness.

```python
import socket, threading

ENCODING = "utf8"

class Client(threading.Thread):
    def run(self):
        # initialize necessary variables
        spacing = ""
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        # open connection
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        requestData = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]

        for datum in requestData:
            # send request to server
            print(spacing, "put:", datum)
            connection.sendto(datum.encode(ENCODING), clientAddress)

            # get response from server
            responseData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", responseData.decode(ENCODING))

        # close connection
        connection.close()
        print(spacing, "close")

class Server(threading.Thread):
    def run(self):
        # initialize necessary variables
        count = 0
        spacing = "\t\t\t"
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        # open connection
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection.bind(serverAddress)

        print(spacing, "open")

        while 1:
            # get request from client
            requestData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", requestData.decode(ENCODING))

            # process request
            count += 1

            if requestData.decode(ENCODING) == ".":
                responseData = "done"
            else:
                responseData = "ok [" + str(count) + "]"

            # send response to client
            print(spacing, "put:", responseData)
            connection.sendto(responseData.encode(ENCODING), clientAddress)

            # close connection
            if requestData.decode(ENCODING) == ".":
                break

        connection.close()
        print(spacing, "close")

class Attacker(threading.Thread):
    def run(self):
        # initialize necessary variables
        spacing = "            "
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        # open connection
        clientConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientConnection.bind(clientAddress)

        # initialize necessary variables
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        # open connection
        serverConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        while 1:
            # get request from client
            clientRequestData, clientAddress = clientConnection.recvfrom(1024)
            print(spacing, "get:", clientRequestData.decode(ENCODING))

            # modify request (if desired)
            serverRequestData = clientRequestData.decode(ENCODING)

            if clientRequestData.decode(ENCODING) == "quick":
                serverRequestData = "big"
            if clientRequestData.decode(ENCODING) == "fox":
                serverRequestData = "bear"
            if clientRequestData.decode(ENCODING) == "jumps":
                serverRequestData = "runs"
            if clientRequestData.decode(ENCODING) == "lazy":
                serverRequestData = "hyper"
            if clientRequestData.decode(ENCODING) == "dog":
                serverRequestData = "rabbit"

            # send request to server
            print(spacing, "put:", serverRequestData)
            serverConnection.sendto(serverRequestData.encode(ENCODING), serverAddress)

            # get response from server
            serverResponseData, serverAddress = serverConnection.recvfrom(1024)
            print(spacing, "get:", serverResponseData.decode(ENCODING))

            # modify response (if desired)
            clientResponseData = serverResponseData.decode(ENCODING)

            # send response to client
            print(spacing, "put:", clientResponseData)
            clientConnection.sendto(clientResponseData.encode(ENCODING), clientAddress)

            if serverResponseData.decode(ENCODING) == "done":
                break

        # close connection
        serverConnection.close()
        clientConnection.close()
        print(spacing, "close")

print("  Client     Attacker     Server")
print("----------  ----------  ----------")

# create all threads
server = Server()
attacker = Attacker()
client = Client()

# start all threads
server.start()
attacker.start()
client.start()

# join all threads
server.join()
attacker.join()
client.join()

```
## UDP Client-Server with MITM Attack Simulation

### Code Explanation

### Overview
The code implements a simple UDP client-server architecture along with an attacker thread simulating a man-in-the-middle attack. The client sends data to the server, while the attacker intercepts and modifies the data before it reaches the server.

### Key Components

1. **Imports**:
   - `socket`: Provides access to the BSD socket interface.
   - `threading`: Enables concurrent execution by creating threads.

2. **Encoding**:
   - `ENCODING = "utf8"`: Specifies the encoding for string manipulation.

3. **Client Class**:
   - Inherits from `threading.Thread` to run in a separate thread.
   - Connects to a server at `127.0.0.1:12345` and sends a list of strings.
   - Receives responses from the server and prints them.

4. **Server Class**:
   - Also inherits from `threading.Thread`.
   - Listens for incoming messages on `127.0.0.1:12346`.
   - Processes incoming messages and sends responses.
   - Stops when it receives a "." from the client.

5. **Attacker Class**:
   - Simulates a MITM attack by intercepting messages between the client and server.
   - Modifies specific messages (e.g., replacing "quick" with "big") before forwarding them to the server.
   - Sends modified responses back to the client.

6. **Main Execution**:
   - Instantiates and starts all three threads: `Server`, `Attacker`, and `Client`.
   - Uses `join()` to ensure the main thread waits for the others to finish.

### Important Concepts

- **UDP Sockets**: 
  - The code uses `SOCK_DGRAM` which allows for connectionless communication. UDP is faster but does not guarantee delivery.

- **Multithreading**:
  - Each class runs in its own thread, allowing simultaneous operations (client sending requests, server processing, and attacker intercepting).

- **Man-in-the-Middle Attack**:
  - The attacker intercepts and alters messages between the client and server. This demonstrates vulnerabilities in communication protocols where data can be manipulated.

### MITM Attack Example
- The attacker listens for the client's message:
  - If it sees "quick", it changes it to "big".
  - Other substitutions include changing "fox" to "bear", "jumps" to "runs", etc.
  
### Security Implications
- This example highlights the importance of securing communication channels (e.g., using encryption) to prevent unauthorized data interception and manipulation.


## CORS (Cross-Origin Resource Sharing):

Cross-Origin Resource Sharing (CORS) is a security mechanism implemented by web browsers to control access to resources (like APIs or fonts) on a web page from a different domain than the one serving the web page. It extends and adds flexibility to the Same-Origin Policy, allowing servers to specify who can access their resources. CORS works through a system of HTTP headers, where browsers send a preflight request to the server hosting the cross-origin resource, and the server responds with headers indicating whether the actual request is allowed. This mechanism helps prevent unauthorized access to sensitive data while enabling legitimate cross-origin requests. CORS is crucial for modern web applications that often integrate services and resources from multiple domains, balancing security needs with the functionality requirements of complex, distributed web systems.

**CORS** allows web applications from one domain (origin) to access resources on another domain. By default, browsers restrict cross-origin requests for security, but CORS opens controlled access via headers.

#### Real-Life Example
Imagine you're working on a project at **domain-a.com**. Now, you need some data hosted on **domain-b.com**. Normally, your browser blocks this due to security reasons. But if **domain-b.com** allows it by setting CORS headers, you can access the data safely.

![image](https://github.com/user-attachments/assets/cee23754-2497-4f24-a480-75a3ba82385e)


![image](https://github.com/user-attachments/assets/ffa1590f-d316-4d5c-99aa-0d8f7ec4bcc9)

#### Key Concepts:
1. **Same-Origin Policy**: Browsers block requests from one origin (domain, protocol, port) to another by default.
2. **CORS Headers**: Servers explicitly declare which origins can access their resources using headers like:
   - `Access-Control-Allow-Origin`: Defines which domains are allowed to access the server.
3. **Preflight Requests**: For certain types of requests (e.g., `POST`), the browser asks the server via an **OPTIONS** request if it’s okay to proceed before the actual request.

#### Common CORS Scenario
```javascript
fetch("https://api.otherdomain.com/data")
  .then(response => response.json())
  .then(data => console.log(data));
```
Here, JavaScript code from `domain-a.com` fetches data from `domain-b.com`. If `domain-b.com` allows `domain-a.com` through its CORS policy, the browser will permit the data exchange.

#### Preflight Request Example
For requests like `POST` or requests with custom headers, the browser first sends a preflight **OPTIONS** request to check if the server allows the cross-origin request.

---

### Example of a CORS Header:

```http
Access-Control-Allow-Origin: https://domain-a.com
```
This header tells the browser to allow requests from `domain-a.com`.

---

#### Why CORS?
CORS protects against malicious attacks where a script on one website tries to access sensitive information from another. It’s crucial for web security, ensuring that data sharing across domains happens under controlled, safe conditions.

### Content Security Policy (CSP)

**Content Security Policy (CSP)** is like a set of rules that tell your website what content it can trust and what it should block to avoid attacks like **Cross-Site Scripting (XSS)** and **clickjacking**.

#### Real-Life Example: 
Imagine your website is like a VIP event. **CSP** is the security team. They have a guest list (trusted content sources), and anyone not on the list (like malicious scripts) is turned away.

- You specify in your site’s settings, “Only load images from `images.example.com` or scripts from `scripts.example.com`.” If a hacker tries to inject a script from a shady source, **CSP** blocks it from running.

#### How to Implement CSP:
- **HTTP Header**: You add a special header like this:
```http
Content-Security-Policy: script-src 'self' https://scripts.example.com
```
This tells the browser, "Only load JavaScript from my domain (`'self'`) or from the trusted domain."

- **Meta Tag**: You can also add this in your HTML:
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' https://images.example.com;">
```

#### Why CSP Matters:
- **Stops malicious code**: By restricting content sources, you prevent hackers from injecting harmful scripts.
- **Reporting**: CSP can also alert you when someone tries to break the rules so you can investigate.

---

### Server Security

**Server Security** is all about making sure your server (the machine that runs your website/app) stays safe from attackers. Think of it as installing locks, alarms, and cameras in your virtual house.

#### Real-Life Example:
Let’s say you run an **online store**. Your server stores customer data and processes payments. You wouldn’t leave the doors open for anyone to access, right? Server security helps lock those doors.

#### Key Practices:

1. **Patch Management**: Regularly update your software (like installing phone updates). Outdated software is like leaving your house with a broken lock.
   
2. **Access Control**: Only let authorized people in! For example, only specific employees should be able to access the payment system. Use strong passwords and multi-factor authentication (MFA).

3. **Firewalls**: Think of a firewall like a bouncer at the door. It only lets in visitors with the right credentials and blocks suspicious activity.

4. **Encryption**: Protect sensitive info (like passwords and credit card details) by encrypting it. Encryption is like turning your data into secret code that only authorized people can read.

5. **Backup**: Regularly backup your data so that even if something goes wrong (like a server crash), you can restore it. Imagine keeping a spare copy of all your important documents somewhere safe.

6. **Monitoring**: Use tools to constantly check your server’s activity. If someone tries to break in, you’ll get an alert.

#### Real-World Tip:
- For an e-commerce website, make sure payment and customer data is encrypted. Use SSL/TLS certificates so that communication between the server and users is secure (look for "https" in the URL).

#### Best Practices:
- **Disable root access** for your server’s main account (like locking away the master keys).
- Use **firewalls and tools like fail2ban** to block repeated hacking attempts.
- Keep **backups in multiple places** (e.g., local, cloud, and off-site) so you're prepared for any disaster.

---

Both **CSP** and **Server Security** are crucial for keeping your site and users safe from attacks. **CSP** protects your front-end from malicious scripts, while **server security** protects the backend from unauthorized access.
