# What is the Internet?

**Main link**: 

[What is the Internet?](https://roadmap.sh/guides/what-is-internet)

[The Internet](https://cs.fyi/guide/how-does-internet-work#introduction-to-the-internet)

[HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

The Internet is a global network of interconnected computers, allowing communication through standardized protocols. It is a network of networks, composed of various independently operated systems, and is designed to be decentralized, with no central control.

### Understanding Networks

Before diving into the Internet, it’s essential to understand what a network is. A network consists of a group of computers and devices connected to each other. For example, your home might have a network of computers, while your neighbor has a similar setup. Together, these networks form the Internet.

## How the Internet Works: An Overview

At a high level, the Internet connects devices and computer systems through a set of standardized protocols that define how information is exchanged. The core infrastructure consists of interconnected routers that direct traffic between devices.

### Data Transmission

When you send data over the Internet, it is broken into small units called packets. Each packet is sent from your device to a router, which forwards it to the next router in its path until it reaches its destination. This process relies on key protocols:

- **Internet Protocol (IP)**: Responsible for routing packets to their correct destinations.
- **Transmission Control Protocol (TCP)**: Ensures packets are transmitted reliably and in order.
![image](https://github.com/user-attachments/assets/00e398eb-7f45-4527-a565-672214635060)

In addition to IP and TCP, various protocols facilitate data exchange, such as:

- **Domain Name System (DNS)**: Translates domain names into IP addresses.
- **Hypertext Transfer Protocol (HTTP)**: Transfers data between web browsers and servers.
- **SSL/TLS**: Encrypts data for secure transmission.

## Basic Concepts and Terminology

To navigate the Internet effectively, familiarize yourself with these key terms:

- **Packet**: A small unit of data transmitted over the Internet.
- **Router**: A device that directs packets between different networks.
- **IP Address**: A unique identifier for each device on a network.
- **Domain Name**: A human-readable name for a website, like google.com.
- **DNS**: Translates domain names into IP addresses.
- **HTTP/HTTPS**: Protocols for transferring data, with HTTPS providing secure communication.
- **SSL/TLS**: Protocols for secure Internet communication.

Understanding these concepts is vital for developing Internet-based applications and services.

## The Role of Protocols

Protocols are rules and standards that enable communication across the Internet. Some key protocols include:

- **IP**: Routes packets to their correct destination.
- **TCP**: Ensures reliable data transmission.
- **UDP**: Used for faster but less reliable communication.
- **DNS**: Translates domain names into IP addresses.
- **HTTP/HTTPS**: Facilitate web communication.

Standardized protocols allow devices from different manufacturers to communicate seamlessly, making the Internet a unified platform.

## IP Addresses and Domain Names

IP addresses serve as unique identifiers for devices, guiding data to its intended recipient. They typically look like “192.168.1.1.” Domain names, such as “google.com,” are user-friendly identifiers translated into IP addresses by DNS.

### How DNS Works

When you enter a domain name in your browser, a DNS query is sent to a DNS server, which returns the corresponding IP address. This allows your computer to connect to the requested resource.

## HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) is the standard for transferring data between a client (like a web browser) and a server. When you access a website, your browser sends an HTTP request, and the server responds with the requested data.

HTTPS (HTTP Secure) encrypts the data exchanged between the client and server using SSL/TLS, adding a layer of security. A padlock icon in your browser indicates a secure connection.

## Building Applications with TCP/IP

TCP/IP forms the backbone of Internet-based applications. Key concepts include:

- **Ports**: Unique identifiers for applications running on devices.
- **Sockets**: Combinations of IP addresses and port numbers for communication endpoints.
- **Connections**: Established between two sockets for data transfer.

Understanding these concepts is essential for developing scalable and secure applications.

## Securing Internet Communication with SSL/TLS

SSL/TLS protocols secure data transmitted over the Internet. Key components include:

- **Certificates**: Establish trust between clients and servers.
- **Handshake**: Negotiates encryption parameters for secure connections.
- **Encryption**: Protects data during transmission.

Applications must utilize SSL/TLS for secure data exchange, ensuring the integrity and confidentiality of user information.

## Cybersecurity and Crime

Cybersecurity involves protective measures against criminal activity on networks. Understanding the security challenges facing DNS, such as spoofing, is crucial for safeguarding data.

### DNS Analogy

Think of DNS as a phonebook; it translates user-friendly domain names into IP addresses, similar to dialing a contact by name instead of remembering their phone number.

![image](https://github.com/user-attachments/assets/c098b375-832d-4451-8ef4-ce7d1b7c8ac1)


# Transmission Control Protocol

Under the application layer in the protocol stack is the TCP layer. When applications open a connection to another computer on the Internet, the messages they send (using a specific application layer protocol) get passed down the stack to the TCP layer. TCP is responsible for routing application protocols to the correct application on the destination computer. To accomplish this, port numbers are used. Ports can be thought of as separate channels on each computer. For example, you can surf the web while reading e-mail. This is because these two applications (the web browser and the mail client) used different port numbers. When a packet arrives at a computer and makes its way up the protocol stack, the TCP layer decides which application receives the packet based on a port number.

## How TCP Works

1. When the TCP layer receives the application layer protocol data from above, it segments it into manageable "chunks" and then adds a TCP header with specific TCP information to each "chunk". The information contained in the TCP header includes the port number of the application the data needs to be sent to.

2. When the TCP layer receives a packet from the IP layer below it, the TCP layer strips the TCP header data from the packet, does some data reconstruction if necessary, and then sends the data to the correct application using the port number taken from the TCP header.

This is how TCP routes the data moving through the protocol stack to the correct application.

## Characteristics of TCP

- TCP is **not** a textual protocol.
- TCP is a **connection-oriented**, reliable, byte stream service. 
  - **Connection-oriented** means that two applications using TCP must first establish a connection before exchanging data.
  - TCP is reliable because for each packet received, an acknowledgment is sent to the sender to confirm delivery.
  - TCP also includes a checksum in its header for error-checking the received data.

### TCP Header

The TCP header looks like this:

![image](https://github.com/user-attachments/assets/2fcb3105-c8e4-4f00-a4e7-ec90c39c14a7)


Notice that there is no place for an IP address in the TCP header. This is because TCP doesn't know anything about IP addresses. TCP's job is to get application-level data from application to application reliably. The task of getting data from computer to computer is the job of IP.

## Check It Out - Well Known Internet Port Numbers

Listed below are the port numbers for some of the more commonly used Internet services:

- **FTP**: 20/21
- **Telnet**: 23
- **SMTP**: 25
- **HTTP**: 80
- **Quake III Arena**: 27960

---

# Internet Protocol

Unlike TCP, IP is an unreliable, connectionless protocol. IP doesn't care whether a packet gets to its destination or not. Nor does IP know about connections and port numbers. IP's job is to send and route packets to other computers. IP packets are independent entities and may arrive out of order or not at all. It is TCP's job to make sure packets arrive and are in the correct order. 

About the only thing IP has in common with TCP is the way it receives data and adds its own IP header information to the TCP data. The IP header looks like this:

![image](https://github.com/user-attachments/assets/013cbc4f-1073-4584-ae14-959b923c1f27)

Above we see the IP addresses of the sending and receiving computers in the IP header. Below is what a packet looks like after passing through the application layer, TCP layer, and IP layer. The application layer data is segmented in the TCP layer, the TCP header is added, the packet continues to the IP layer, the IP header is added, and then the packet is transmitted across the Internet.

![image](https://github.com/user-attachments/assets/f9b54036-3f6a-493b-a299-ca12ae80f000)



---

# Browser Functionality

Browsers, much like operating systems, possess extensive capabilities that go beyond basic software. They provide features such as networking, timers, and data storage, allowing rich interactions with web applications.

## Components of a Browser

Browsers consist of several important components:

1. **Data Persistence**  
   - **Cookies**: Store small pieces of information between requests.
   - **Local Storage**: Provides more persistent storage for data, available across sessions.
   - **JavaScript**: Executes dynamic content and interacts with the data persistence layer.

2. **User Interface (UI)**  
   - The browser's UI is where users interact, navigate, and view content. Elements like the address bar, bookmarks, and page view area are all part of the UI.

3. **Browser Engine**  
   - Engines like **Blink** (in Chrome) or **WebKit** (in Safari) work under the hood to process web content and handle the rendering of web pages.
   - Changing the browser engine would impact how content is displayed across the internet, making compatibility critical.

---

## HTML Processing

HTML files go through several steps before being displayed:

1. **Raw Byte Reading**  
   The browser first reads the raw bytes of an HTML file from the disk.

2. **Character Encoding**  
   These bytes are then converted into characters based on encoding (e.g., UTF-8).

3. **Tokenization**  
   The character sequence is tokenized, breaking it into meaningful units like HTML tags (`<h1>`, `<p>`, etc.).

4. **Node List Generation**  
   The tokens are turned into a **node list** that the rendering engine (usually written in C++) understands.

**Example**:  
```html
<h1>Hello World</h1>
<p>This is a paragraph.</p>
```  
The browser converts this into a list of nodes for rendering.

---

## Document Object Model (DOM)

The **DOM** is a structured representation of the HTML document. After tokenization, the HTML is organized into a **hierarchical model** that represents relationships between elements like parents, siblings, and children.

**Example**:
- `<body>` is a parent of `<h1>` and `<p>`.
- `<h1>` and `<p>` are siblings.

---

## CSS Object Model (CSSOM)

Similar to the DOM, the **CSSOM** is created by tokenizing and structuring CSS data. This model defines how styles (like colors, fonts, and layouts) should be applied to elements on the page.

**Example**:
```css
h1 {
  color: blue;
}
```
The CSSOM ensures that the `<h1>` text is rendered in blue.

---

## Render Tree

The **Render Tree** is built by combining the DOM and CSSOM. It calculates the layout and visual styling of elements.

1. **DOM + CSSOM** = **Render Tree**  
   - Determines where elements should appear and how they should look on the page.

---

## JavaScript Execution

JavaScript execution happens when the browser encounters a `<script>` tag. Since JavaScript can manipulate the DOM and CSSOM, it can pause rendering.

- **Script Loading**:  
   By default, JavaScript execution blocks the loading of the DOM and CSSOM. However, using the `async` or `defer` keywords allows JavaScript to load asynchronously.

**Example**:  
```html
<script async src="app.js"></script>
```
This script will load asynchronously, allowing the rest of the page to load faster.

---

## Rendering

Once everything is processed, the browser's rendering engine (typically written in C++) takes the HTML, CSS, and JavaScript and turns it into **pixels** on the screen.

**Example**:  
The browser translates this code:
```html
<h1>Hello World</h1>
<p>This is a paragraph.</p>
```
into a visual representation on the screen with the defined styles.

![image](https://github.com/user-attachments/assets/9994f127-b1cc-4990-851d-7a538ec46a80)

---

