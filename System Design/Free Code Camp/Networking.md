

### Networking Basics

When we discuss networking basics, we are essentially addressing how computers communicate with one another.

#### Key Concepts:

- **Communication Protocols**: Rules that dictate how data is transmitted and received over a network (e.g., TCP/IP, HTTP).

- **Network Types**: Different configurations of networks, including Local Area Networks (LANs), Wide Area Networks (WANs), and the Internet.

- **Data Transmission**: The process of sending and receiving data, which can occur via wired (Ethernet) or wireless (Wi-Fi) connections.

- **IP Addresses**: Unique identifiers assigned to each device on a network, enabling communication between devices.

- **Routers and Switches**: Devices that direct data traffic within and between networks, ensuring efficient data flow.

In summary, understanding networking basics is crucial for enabling effective communication between computers and ensuring seamless data exchange.



### The Role of IP Addresses in Networking

At the heart of computer communication is the **IP address**, a unique identifier for each device on a network.

#### Key Points:

- **IPv4 Addresses**: 
  - 32-bit addresses that allow for approximately 4 billion unique identifiers.
  
- **Transition to IPv6**: 
  - Utilizes 128-bit addresses, vastly increasing the number of available unique addresses to accommodate the growing number of devices.

- **Data Communication**: 
  - When two computers communicate, they send and receive **packets of data**.
  
- **Packet Structure**: 
  - Each packet contains an **IP header** that includes essential information, such as the sender's and receiver's IP addresses, ensuring that data reaches the correct destination.

In summary, IP addresses and packet structures are fundamental to enabling effective communication between devices on a network.




## Layers of Networking

Networking is often conceptualized in layers to simplify the design and implementation of network protocols. The most commonly referenced model is the **OSI (Open Systems Interconnection) model**, which has seven layers:

1. **Physical Layer**:
   - Deals with the physical connection between devices, including cables, switches, and other hardware. It defines how data is transmitted as electrical signals, light signals, or radio waves.

2. **Data Link Layer**:
   - Responsible for node-to-node data transfer and error detection. It includes protocols like Ethernet and Wi-Fi, managing how data packets are framed for transmission.

3. **Network Layer**:
   - Manages data routing and forwarding. This layer determines the best path for data to travel across networks. It includes protocols like IP (Internet Protocol).

4. **Transport Layer**:
   - Ensures reliable data transfer between devices. It provides error correction and flow control, using protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

5. **Session Layer**:
   - Manages sessions or connections between applications. It establishes, maintains, and terminates communication sessions.

6. **Presentation Layer**:
   - Transforms data into a format that the application layer can understand. It handles data encryption, compression, and translation.

7. **Application Layer**:
   - The top layer that interacts directly with end-user applications. It includes protocols like HTTP, FTP, and SMTP, enabling services like web browsing and email.

### Summary

These layers work together to facilitate communication over networks, allowing devices to connect and share information effectively. Understanding these layers is crucial for troubleshooting and designing network systems.


## Internet Protocol

### Data Communication in Networking

When two computers communicate over a network, they send and receive **packets of data**. Each packet includes an **IP header**, which contains essential information such as:

- **Sender's IP Address**
- **Receiver's IP Address**

This ensures that the data reaches the correct destination.

#### Governing Protocol: Internet Protocol (IP)

* also called Transfer Control Protocol ( TCP )

The process of sending and receiving these packets is governed by the **Internet Protocol (IP)**, a set of rules that defines:

- **Data Packet Structure**: How packets are formatted, including headers and payloads.
- **Routing**: How packets are directed through various networks to reach their destination.
- **Fragmentation and Reassembly**: How larger packets are split into smaller ones for transmission and reassembled at the destination.

### Other Key Layers

Besides the IP layer, communication also involves other layers of the networking model:

- **Transport Layer**: Ensures reliable data transmission and manages flow control using protocols like TCP and UDP.
- **Data Link Layer**: Handles node-to-node data transfer and error detection, ensuring reliable communication over a physical connection.
- **Application Layer**: Provides protocols for specific applications, enabling end-user services like web browsing and email.

In summary, the effective communication between computers relies on the structured use of protocols at various layers, with the Internet Protocol playing a crucial role in data transmission.




![[InternetProtocol.png]]




## Application Layer

### Application Layer in Networking

Besides the **IP layer**, we also have the **Application Layer**, which is crucial for application-specific data communication. 

#### Key Points:

- **Application Protocols**: 
  - This layer handles protocols like HTTP (for web browsing), FTP (for file transfer), and SMTP (for email). Each protocol defines how data is formatted and transmitted.

- **Data Formatting**: 
  - The data in packets is formatted according to the specific application protocol, ensuring that the receiving device can interpret it correctly. For example, HTTP packets contain structured data that web browsers understand.

### Understanding IP Addressing and Data Packets

Once we grasp the basics of **IP addressing** and **data packets**, we can appreciate how they work together in networking:

- **IP Addressing**: 
  - Unique identifiers for devices on a network, essential for routing packets to the correct destination.

- **Data Packets**: 
  - Units of data that include headers (with IP addresses) and payloads (with application-specific data), enabling effective communication between devices.

In summary, the Application Layer is vital for ensuring that data is transmitted in a format that applications can utilize, complementing the foundational role of the IP layer in routing and addressing.




![[ApplicationLayer.png]]



## Transport Layer

### Transport Layer: TCP vs. UDP

In the **Transport Layer**, two key protocols, **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)**, serve different purposes in data communication.

#### TCP (Transmission Control Protocol)

- **Reliable Communication**:
  - Think of TCP as a meticulous delivery service that ensures packages arrive intact and in order.
  
- **Key Features**:
  - **TCP Header**: Each packet includes a TCP header containing essential information, such as:
    - **Port Numbers**: Identifying the sending and receiving applications.
    - **Control Flags**: Managing the connection and data flow.
  
  - **Sequence Numbers**: Used to keep track of the order of packets, ensuring they are reassembled correctly at the destination.
  
  - **Three-Way Handshake**: A process to establish a stable connection between two devices before data transmission begins.

- **Reliability**: 
  - Guarantees complete and correct delivery of data packets, making it ideal for applications where accuracy is critical (e.g., file transfers, web pages).

#### UDP (User Datagram Protocol)

- **Faster but Less Reliable**:
  - UDP operates without establishing a connection, making it quicker but less reliable than TCP.
  
- **Key Characteristics**:
  - **No Connection Establishment**: Data is sent immediately without handshaking.
  
  - **No Delivery Guarantee**: Does not ensure the order or delivery of packets, which can lead to data loss.

- **Use Cases**: 
  - Ideal for time-sensitive communications where speed is more important than reliability, such as video calls or live streaming, where some data loss is acceptable.

### Summary

The **Transport Layer** plays a crucial role in managing how data is sent and received. TCP ensures reliability and order, while UDP prioritizes speed, making each suitable for different applications. Understanding these protocols helps in designing systems that meet specific communication needs effectively.


![[TCPHeader.png]]




![[3WayHandshake.png]]


## DNS


### Domain Name System (DNS)

The **Domain Name System (DNS)** acts as the internet's phone book, translating human-friendly domain names into IP addresses.

#### How DNS Works

1. **DNS Query**:
   - When you enter a URL in your browser, it sends a DNS query to find the corresponding IP address. This enables the browser to connect to the server and retrieve the web page.

2. **Oversight by ICANN**:
   - The functioning of DNS is overseen by **ICANN (Internet Corporation for Assigned Names and Numbers)**, which coordinates the global IP address space and the domain name system.

3. **Domain Name Registrars**:
   - Accredited by ICANN, companies like **Namecheap** or **GoDaddy** sell domain names to the public.

#### Types of DNS Records

- **A Records**:
  - Map a domain name to its corresponding **IPv4 address**, ensuring requests reach the correct server.

- **AAAA Records**:
  - Map a domain name to an **IPv6 address**, accommodating the newer addressing system.

### Summary

DNS is essential for converting domain names into IP addresses, facilitating seamless web browsing. Its structure and management ensure that users can access websites easily and accurately.


## Networking Infrastructure

The networking infrastructure supports communication through a structured use of IP addresses, ports, and security measures.

#### IP Addresses

- **Public IP Addresses**:
  - Unique across the internet, allowing devices to communicate globally.

- **Private IP Addresses**:
  - Unique within a local network, facilitating communication among devices in that network.

- **Static vs. Dynamic IP Addresses**:
  - **Static IP Addresses**: Permanently assigned to a device, ensuring it retains the same address over time.
  - **Dynamic IP Addresses**: Change over time, commonly used for residential internet connections and devices on local area networks (LANs).

#### Communication in Local Networks

- Devices connected in a local network can communicate directly with each other, enhancing efficiency and speed.

#### Security Measures

- **Firewalls**:
  - Monitor and control incoming and outgoing network traffic, providing a security barrier between internal networks and external threats.

#### Ports and Services

Within a device, specific processes or services are identified by **ports**. When combined with an IP address, they create a unique identifier for a network service. Here are some common port assignments:

- **Port 80**: Used for HTTP (web traffic).
- **Port 443**: Used for HTTPS (secure web traffic).
- **Port 22**: Used for SSH (secure shell access).
- **Port 3306**: Used for MySQL (database management).
- **Port 21**: Used for FTP (File Transfer Protocol).
- **Port 25**: Used for SMTP (Simple Mail Transfer Protocol).
- **Port 53**: Used for DNS (Domain Name System).

### Summary

The networking infrastructure comprises various elements that facilitate secure and efficient communication, using IP addresses, ports, and firewalls to manage connectivity and protect data. Understanding common ports is essential for configuring services and securing networks effectively.






