# JSON Web Token (JWT) Explained

JSON Web Token (JWT) is an **open standard** (RFC 7519) that defines a compact, self-contained way to **transmit information securely** between two parties as a JSON object. This token can be verified and trusted because it is **digitally signed**. JWTs can be signed using a **secret key** (HMAC algorithm) or a **public/private key pair** (RSA or ECDSA). While JWTs can also be encrypted for additional secrecy, we’ll focus on **signed tokens**, which ensure that the data in the token hasn't been tampered with.

---

## 📦 **Why Use JWT?**

### **1. Authorization**

JWTs are most commonly used for **authorization**. After a user logs in, a JWT is issued and sent with every subsequent request, granting access to certain resources based on the user’s permissions.

For example:
- **Real-world scenario:** After logging into Netflix, every request to stream a movie or TV show includes your JWT, allowing access to only the shows you've subscribed to.

### **2. Information Exchange**

JWTs securely transmit information between parties, ensuring the sender is authenticated. The data within the JWT cannot be tampered with because of its signature.

For example:
- **Real-world scenario:** A bank might use JWTs to transfer encrypted data between servers, ensuring the integrity of transactions and preventing any tampering along the way.

---

## 🛠️ **JWT Structure**

JWTs consist of three parts, separated by dots (`.`):
```
header.payload.signature
```

### **1. Header**
Contains the token type (JWT) and the algorithm used for signing (e.g., HS256).
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### **2. Payload**
Contains **claims**, which are statements about the user (or other entities). There are three types of claims:

- **Registered claims**: Predefined claims like `iss` (issuer), `exp` (expiration), and `sub` (subject).
- **Public claims**: Custom claims, often used for sharing data, which should be collision-resistant (registered in the [IANA JWT Registry](https://www.iana.org/assignments/jwt/)).
- **Private claims**: Custom claims shared between parties.

Example payload:
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

### **3. Signature**
The signature ensures the token has not been tampered with. It is created by encoding the **header**, **payload**, and a **secret key** or **private key** (in the case of asymmetric signing).

For example, using the HMAC SHA256 algorithm:
```
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

---

## 🔄 **How JWT Works:**

1. **User Authentication**: After successfully logging in, a JWT is returned.
2. **Token Use**: Every time the user accesses a protected resource (like a server or API), the JWT is sent in the **Authorization header** of the request:
   ```
   Authorization: Bearer <token>
   ```

### **Real-World Example:**
- **YouTube API**: When developers access YouTube's data using their API, they authenticate with a JWT. The token ensures they have valid permissions to retrieve information like playlists or videos.

---

## 🛡️ **Why JWT over Other Tokens?**

- **Compact**: Since JWT uses **JSON**, it is smaller and faster to transmit than XML-based tokens like **SAML**.
- **Versatile**: Works across various programming languages.
- **Secure**: Unlike **Simple Web Tokens (SWT)**, which only use symmetric keys, JWT supports **asymmetric keys** (public/private key pairs) for added security.

## 📈 **Conclusion**

JWTs provide a secure, compact, and easy-to-use method for **authorization** and **information exchange** across platforms. They are widely used today for their **scalability** and **security** benefits in handling sensitive data in modern web applications.



![image](https://github.com/user-attachments/assets/559f48cc-dca6-41b0-bf7b-c203332a5419)

![image](https://github.com/user-attachments/assets/b5a4bfb7-22db-4228-8966-dd2d813c3f6d)

# Simplified Explanation of JWT (JSON Web Token)

Imagine there are two different servers: **Bank** and **Retirement**. Both are separate systems, but you, as a user, want to log in and access both of them without entering your credentials every time.

---

## The Problem: Manual Login Every Time

When you log in to your **Bank** server, you can browse your account information. But if you switch to the **Retirement** server, you're asked to log in again. This can be frustrating, especially if both services belong to the same company and you expect seamless access across platforms.

### Example:
- **Scenario**: You log into **your bank** to check your balance. Later, you visit the **retirement server** to check your retirement plan, but you're asked to log in again, even though both servers are part of the same financial company.

---

## The JWT Solution: Seamless Login Across Services

**JWT (JSON Web Token)** solves this problem by storing the login information **on the browser side**. Once you log in to one server (e.g., **Bank**), a JWT is created and stored in your browser. When you visit the other server (e.g., **Retirement**), the JWT is automatically sent, and the **Retirement** server recognizes you and lets you access your account **without asking you to log in again**.

### How It Works:

1. **Login to Bank Server**:
   - You enter your credentials (username, password).
   - The **Bank server** creates a **JWT** and sends it to your browser.
   
2. **JWT Stored in Browser**:
   - Your browser stores the **JWT** securely.
   
3. **Switch to Retirement Server**:
   - When you switch to the **Retirement server**, your browser sends the **JWT** along with the request.
   - The **Retirement server** checks the **JWT** and sees that you're already authenticated.
   - You **don't need to log in again**; the server grants you access.

### Real-World Example:
- **Google Accounts**: When you log into **Gmail**, you can also access **Google Drive** or **YouTube** without logging in again. That’s because a JWT (or similar token) is being used behind the scenes, allowing all these services to recognize you.

---

## Why JWT is Useful Here:
- **No Multiple Logins**: You log in once, and JWT lets you access multiple services seamlessly.
- **Stored in Browser**: The token is stored safely in the browser, allowing it to be reused when switching between services.
- **Fast and Efficient**: Since JWT is small and compact, it can easily be transmitted with each request without slowing things down.

---

In simple terms, JWT acts like a **magic ticket** that you get when you log in once, and it lets you access multiple services without the hassle of logging in again each time!

![image](https://github.com/user-attachments/assets/58330c54-b26f-428c-913c-be5ab0d1349e)

