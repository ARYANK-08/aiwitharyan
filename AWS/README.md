![image](https://github.com/user-attachments/assets/e2901636-eb40-4521-99cf-68296c1666a4)# AWS - Everything You Need to Know

## Table of Contents
1. [What is Cloud Computing?](#what-is-cloud-computing)
2. [Why Cloud Computing Came into Existence](#why-cloud-computing-came-into-existence)
3. [Cloud Service Models](#cloud-service-models)
   - [Infrastructure as a Service (IaaS)](#infrastructure-as-a-service-iaas)
   - [Platform as a Service (PaaS)](#platform-as-a-service-paas)
   - [Software as a Service (SaaS)](#software-as-a-service-saas)
4. [Six Advantages of Cloud Computing](#six-advantages-of-cloud-computing)
5. [What is a Web Service?](#what-is-a-web-service)
6. [AWS Pricing Model](#aws-pricing-model)
7. [Traditional Infrastructure vs. Cloud Computing](#traditional-infrastructure-vs-cloud-computing)

## What is Cloud Computing?
Cloud computing is the **on-demand** delivery of computing power, database storage, applications, and other IT resources via the internet with a pay-as-you-go pricing model. It enables you to shift from thinking of infrastructure as hardware to thinking of it as software.

### Cloud Service Models
- **IaaS** (Infrastructure as a Service)
- **PaaS** (Platform as a Service)
- **SaaS** (Software as a Service)

---

## Why Cloud Computing Came into Existence
Before cloud computing, organizations managed their own racks and servers on-premises. This approach had several challenges:

- **Underutilization of Resources**: Resources were often not fully utilized.
- **Scalability Issues**: Scaling instantly was challenging and required guessing future usage.
- **High Maintenance Costs**: Managing hardware and software infrastructure was a costly and time-consuming task.

Cloud computing was developed to address these issues, offering a more flexible, scalable, and cost-effective solution.

---

## Cloud Service Models

### Infrastructure as a Service (IaaS)
Provides access to networking features, computers (virtual or dedicated hardware), and data storage space. It offers the highest level of control over IT resources.

**Example**: Using Amazon EC2.

### Platform as a Service (PaaS)
Removes the need to manage the underlying infrastructure (usually hardware and operating systems). Focuses on the deployment and management of your applications.

**Example**: Using Elastic Beanstalk.

### Software as a Service (SaaS)
End-user applications are delivered over the internet.

**Example**: Slack, Gmail.

![Cloud Service Models](https://github.com/user-attachments/assets/18df9170-038b-4847-a328-91467049cb0f)

---

## Six Advantages of Cloud Computing

1. **Pay-as-you-go**: Pay only for the amount you consume, reducing hardware and maintenance costs.
2. **Eliminate Guessing Capacity**: Scale on demand, avoiding over-provisioning.
3. **Increased Speed**: Access resources quickly and efficiently.
4. **Stop Spending on Racks and Stacks**: No need to maintain data centers.
5. **Go Global in Minutes**: Deploy your application in multiple regions worldwide.
6. **Massive Economies of Scale**: The shared infrastructure model reduces costs for everyone.

---

## What is a Web Service?
A web service is any piece of software that is available over the internet and uses standardized formats like JSON or XML for request and response between applications.

- **EC2**: Complete control over AWS resources.
- **Lambda**: Run code without managing servers.
- **Elastic Beanstalk**: Deploy, manage, and scale web apps.
- **Lightsail**: Lightweight cloud platform for simple web apps.
- **Batch**: Process hundreds of thousands of batch workloads.
- **Outposts**: Extend AWS infrastructure to on-premises data centers.
- **Fargate**: Implement containers or microservices architecture.

![AWS Web Services](https://github.com/user-attachments/assets/834cf39a-24de-42d2-a921-868079532ad8)

---

## AWS Pricing Model

- **Compute**: Charged per second, varying by instance type.
- **Storage**: Typically charged per GB/hour.
- **Data Transfer**:
  - Outbound data is aggregated and charged per GB.
  - Inbound data transfer has no charge.

---

## Traditional Infrastructure vs. Cloud Computing

| Traditional Infrastructure | Cloud Computing |
|----------------------------|-----------------|
| Equipment | No upfront expense |
| Resources and administration | Pay for what you use |
| Contracts | Improve time to market |
| Costs | Scale up and down |


---


## VPC
An isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define.

## Total Cost Ownership (TCO)
A comparison between on-premises infrastructure vs. cloud infrastructure, including costs like server storage and IT labor.

## AWS Billing Dashboard
Includes AWS Budgets, cost and usage reports, cost explorer, forecast, and AWS pricing calculator.

## AWS Global Infrastructure
- **AWS regions** are geographical areas.
  - Data replication across regions is controlled by you.
  - Communication between regions uses AWS backbone infrastructure.

- A region typically consists of two or more availability zones.
- **Selecting a region**:
  - Data governance & legal requirements
  - Proximity to customers (latency)
  - Services available in the region
  - Costs (vary by region)

![AWS Regions](https://github.com/user-attachments/assets/88b4bba4-a04a-499e-a9e5-6919b1700570)

- Each region has multiple availability zones.
- Each availability zone is a fully isolated partition.
  - 69 availability zones
  - Availability zones consist of discrete data centers
  - Designed for fault tolerance and isolation
  - Interconnected with other availability zones by network
  - AWS recommends replicating data and resources across availability zones for resiliency

## Data Centers
- Designed for security
- Where data resides and data processing occurs
- Each data center has redundant power, networking, and connectivity, housed in a separate facility
- Each data center has 50k to 80k physical servers
- **Point of Presence**:
  - Route 53 to reduce latency
  - AWS CloudFront is a content delivery network to end users, reducing latency

## Elasticity and Scalability
- Dynamic adaptation of capacity
- Scalable infrastructure adapts to accommodate growth
- **Fault tolerance**: Operates even in failure
- **High availability**: Minimize downtime, ensure performance
- No human intervention and backup generators

Example: An EC2 Linux instance in the US East (Ohio) region costs $0.0416 per hour, while in Tokyo, it costs $0.0544 per hour.

## AWS Shared Responsibility Model
### Customer Responsibilities (In the Cloud)
- Customer data
- Platform, applications, IAM
- OS, network, firewall configuration, EC2 instance
- Client-side and server-side data encryption
- Network traffic protection
- Data integrity and authentication

### AWS Responsibilities (Of the Cloud)
- Software
- Compute, storage, database, networking
- Hardware infrastructure
- Regions, edge locations, availability zones

### AWS Services
- Compute
- Storage
- Database
- Networking

### Infrastructure
#### AWS Responsibilities
- Physical data centers security
- Intrusion detection: Network infrastructure
- Virtualization infrastructure: Instance isolation
- Hardware and software infrastructure: OS, auditing, etc.
  - Example: EC2 instances isolated from other customers

#### Customer Responsibilities
- EC2 instance OS
- Security group configuration
- OS host-based firewalls
- Network configurations
- Account management
- Passwords, role-based access

### IaaS (Infrastructure as a Service)
- Examples: EC2, VPC, Elastic Block Store
- More flexibility
- Configuration and networking

### PaaS (Platform as a Service)
- Examples: Elastic Beanstalk, RDS, Lambda Functions
- No need to manage infrastructure
- AWS handles OS, database, patching, firewall configuration
- Focus on code
- Disaster recovery

## AWS Identity & Access Management (IAM)
- **Example**: Think of it like a school database access where the principal has the highest authority access of all resources, and the least is given to students.
- Use IAM to manage access to AWS resources, e.g., EC2 instance/S3 bucket -> resources.
- A resource is an entity that you can work with.
  - Control who can terminate EC2 instances.
  - Who can access the resources.
  - Which resources can be accessed, and what can the user do to the resource?
  - How resources can be accessed?

- **IAM Components**:
  - **IAM User**
  - **IAM Group**: DBA, auditors, developers
  - **IAM Policy**: Document that defines which resources can be accessed and the level of access
  - **IAM Roles**: Grant permissions

![IAM Example](https://github.com/user-attachments/assets/9cce8ce3-e567-4d17-ad93-efabe210e6c5)

 
> [!NOTE]
> Follow the principle of least privilege (minimal set of permissions required).

**Example**: S3 bucket IAM policy example:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow Akua to list objects in the bucket",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::12345678901:user/Akua"
            },
            "Action": [
            "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
        }
    ]
}
```

**Example**: An application that runs on EC2 needs access to S3.

**Solution**:
- Define an IAM policy that grants access to S3.
- Attach the policy to a role.
- Allow EC2 instance to assume the role.

![IAM Solution](https://github.com/user-attachments/assets/1700e1e2-26e9-4d5b-8853-ef54c75d5789)

## Data Security in AWS
- Encryption encodes data with a secret key, making it unreadable.
  - AWS KMS can manage your secret keys.
  - AES-256 encryption algorithm.

- **Encryption of Data in Transit**:
  - Data moving across a network.
  - TLS (Transport Layer Security) -> SSL -> AES-256.
  - AWS Certificate Manager provides a new way to manage and renew TLS/SSL certificates.

- Secure HTTP(S) creates a secret tunnel.
- Use SSL/TLS for bidirectional exchange of data.

- **SSL/TLS**:
  - Secure network communications and establish the identity of websites over the internet.
  - Web traffic over HTTP is not secure.
  - HTTPS is protected from man-in-the-middle attacks and eavesdropping due to bidirectional communication and encryption by SSL.

## Networking Basics

- A computer network is formed when two or more client machines are connected to share resources. 
  - A network can be partitioned into subnets and requires a networking device such as a router or switch.

![Networking Basics](https://github.com/user-attachments/assets/da67918f-9811-4310-b09e-c572e00d2e62)
![image](https://github.com/user-attachments/assets/914bbdc9-853d-43cd-9a06-bb0c9e469385)

- Each client machine has a unique IP address.
  - **Example:**  
    - `192` = `11000000`, `0` = `00000000`, `2` = `00000010`, `0` = `00000000`
  - **IPv4 (32 bits):** `192.0.2.0`
  - **IPv6 (128 bits):** `2600:1f18:22ba:8c00:ba86`

![image](https://github.com/user-attachments/assets/58faaf29-17fc-436d-bdea-2a927d585294)
## CIDR (Classless Inter-Domain Routing)

Classless Inter-Domain Routing (CIDR) is a method of IP address allocation and routing that allows for more efficient use of IP addresses. CIDR is based on the idea that IP addresses can be allocated and routed based on their network prefix rather than their class, which was the traditional way of IP address allocation. A CIDR address is expressed as an IP address and is the first address of the network.

### Advantages of CIDR

- **Efficient use of IP addresses:** CIDR allows for more efficient use of IP addresses, which is essential as the pool of available IPv4 addresses continues to shrink.
- **Flexibility:** CIDR offers more flexible allocation of IP addresses, which is beneficial for organizations with complex network requirements.
- **Better routing:** CIDR enables more efficient routing of IP traffic, leading to improved network performance.
- **Reduced administrative overhead:** CIDR simplifies the management of IP addresses and routing, reducing administrative overhead.

![CIDR Example](https://github.com/user-attachments/assets/8bdf19d3-416a-4f33-a788-d9cd25f1518f)
![CIDR Range](https://github.com/user-attachments/assets/26711456-6f37-4873-95d5-8473bc7df765)

**Example:** `192.0.2.0/24`  
The last number (24) indicates that the first 24 bits must be fixed, and the last 8 bits are flexible, giving `2^8 = 256 IP addresses`.  
- **Range:** `192.0.2.0` to `192.0.2.255`.
- **Special Cases:**
  - Fixed: `192.0.2.0/24`
  - Flexible: `0.0.0.0/0`

## OSI Model

The OSI Model explains how data travels over a network.

| Layer        | Number | Function                                           | Protocol                        |
|--------------|--------|----------------------------------------------------|---------------------------------|
| Application  | 7      | Provides means for applications to access the network | HTTPS, FTP, LDAP, DHCP          |
| Presentation | 6      | Handles encryption and ensures that the application layer reads data correctly | ASCII, ICA                      |
| Session      | 5      | Manages orderly data exchange                      | NETBIOS, RPC                    |
| Transport    | 4      | Supports host-to-host communication                | TCP, UDP                        |
| Network      | 3      | Manages routing and packet forwarding (routers)    | IP                              |
| Data Link    | 2      | Ensures reliable data transfer across the physical link | ARP                             |
| Physical     | 1      | Transmits the raw bit stream (hubs)                | Ethernet, FDDI                  |

**Example:** When a web browser sends a request to `www.google.com`, the following sequence occurs:

- Application layer -> Presentation layer -> Session layer -> Transport layer (TCP/IP) -> Network layer (IP) -> Data link layer (MAC) -> Physical layer (Ethernet).

The OSI model ensures seamless data transmission from one network to another.

---

# VPC (Virtual Private Cloud)

- **Definition:**  
  A VPC enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.

- **Control Over Networking Resources:**  
  VPC provides control over your virtual networking resources, including:
  - Selection of IP address ranges (IPv4, IPv6)
  - Creation of subnets
  - Configuration of network gateways and route tables

- **Customization:**  
  You can customize the network configuration for your VPC and use multiple layers of security.

- **Example Use Case:**  
  - Create a public subnet for web servers to access the public internet.
  - Use RDS in a private subnet to restrict public internet access.

- **Security:**  
  VPC allows the use of security groups and network access control lists (Network ACLs) to help control access to EC2 instances in each subnet.

- **Key Points:**
  - VPCs are logically isolated and dedicated to your account.
  - Subnets are ranges of IP addresses within a VPC.
  - A VPC belongs to a single AWS region and contains subnets that belong to a single availability zone.
  - Subnets can be public or private.
![image](https://github.com/user-attachments/assets/6747863c-bd12-4a41-9ec2-8f6597a14a58)

## Subnets

- **Definition:**  
  A range of IP addresses in a VPC. Public subnets have direct access to the internet, while private subnets do not.

- **Reserved IP Addresses Example:**  
  - A VPC with an IPv4 CIDR of 10.0.0.0/16 has 65,536 total IP addresses.
  - If divided into 4 equal-sized subnets, only 251 IP addresses are available per subnet as 5 are reserved.
  
  Example:
  - **CIDR (10.0.0.0/24) | Reserved for:**
    - 10.0.0.0 | Network address
    - 10.0.0.1 | Internal communication
    - 10.0.0.2 | DNS
    - 10.0.0.3 | Future use
    - 10.0.0.255 | Network broadcast address

- **Elastic IP Address:**  
  Allocate and remap Elastic IPs at any time.

- **Route Tables:**  
  Control traffic for a subnet.

![VPC Diagram](https://github.com/user-attachments/assets/ee6e132b-c8f8-49c3-90e8-ba78a78b1863)
![Route Table Example](https://github.com/user-attachments/assets/e4bf979f-d03a-45ba-bf20-8c68bbf0b86a)

---

## Internet Gateway
![image](https://github.com/user-attachments/assets/7f5998a4-3064-4550-977d-2fddbe73a81e)

- **Definition:**  
  An Internet Gateway allows communication between EC2 instances in your VPC and the internet.
  
- **Route Table Example:**
  - **Destination | Target**
    - 10.0.0.0/16 | Local
    - 0.0.0.0/0 | Internet Gateway ID

---

## NAT Gateway (Network Address Translation Gateway)
![image](https://github.com/user-attachments/assets/1b9586a3-124e-4486-b36e-002808957e71)

- **Definition:**  
  Allows instances in private subnets to connect to the internet or AWS services while preventing the internet from initiating a connection to them.

- **VPC Sharing:**  
  Share a subnet with other AWS accounts within the same organization, enabling services like EC2, RDS, Lambda, and Redshift.
![image](https://github.com/user-attachments/assets/535d270d-c1e9-413c-820d-affd195fd9c8)

- **VPC Peering:**  
  A VPC-to-VPC connection.
![image](https://github.com/user-attachments/assets/e44ec2a4-8cb0-4d50-9c4f-e6f0e807f83c)

- **AWS Direct Connect:**  
  Connects a VPC to a remote network.
![image](https://github.com/user-attachments/assets/14f87c4e-0cc7-4d12-9fa6-3c31ed5b8049)


![NAT Gateway Diagram](https://github.com/user-attachments/assets/337dc9d0-b4a6-46ec-8a95-a86cd7bdd32e)
![image](https://github.com/user-attachments/assets/46422f0d-369e-4683-8dba-3319bd114412)

---

## Security Groups

- **Definition:**  
  Acts as a virtual firewall for your instances, controlling inbound and outbound traffic.
  
- **Characteristics:**
  - Operates at the instance level, not the subnet level.
  - Default Security Group: Denies all inbound traffic and allows all outbound traffic.
 
![image](https://github.com/user-attachments/assets/23532658-4487-4c2a-8ca3-0a064fa5db07)
  

| **Type**         | **Source/Destination** | **Protocol** | **Port Range** | **Description**      |
|------------------|------------------------|--------------|----------------|----------------------|
| **Outbound**     | 0.0.0.0/0              | All          | All            | IPv4 IP              |
| **Outbound**     | ::/0                   | All          | All            | IPv6 IP              |
| **Custom Rules** | 0.0.0.0/0              | TCP          | 80             | HTTP (IPv4)          |
| **Custom Rules** | ::/0                   | TCP          | 443            | HTTPS (IPv4)         |

![image](https://github.com/user-attachments/assets/78e13ef9-e026-4670-aa1c-ba99574b66fb)


- **Example:**  
  Incoming web traffic is distributed among a group of web servers located in different Availability Zones to ensure no single server is overwhelmed.


---


### SGs vs. ACLs (Security Groups vs. Network Access Control Lists)

- **Scope:** Instance level | Subnet level
- **Rules:** Allow rules only | Allow and deny rules
- **State:** Stateful (return traffic allowed) | Stateless
- **Order of Rules:** All rules are evaluated before a decision is made to allow traffic.

---

# Example VPC Design for an AI Anime Website

1. **Create a VPC** with CIDR: 10.0.0.0/24.
2. **Public Subnet:** 10.0.0.0/25 - For the web server.
3. **Private Subnet:** 10.0.0.128/25 - For the database server.
4. **Attach an Internet Gateway.**
5. **Routing:**
   - Public subnet -> Internet Gateway.
   - Private subnet -> NAT Gateway.
6. **Security Groups:**
   - Allow HTTP & HTTPS traffic.
7. **Deploy EC2 Instances:**
   - Web server in the public subnet.
   - Database server in the private subnet.
8. **Use Multiple Availability Zones & Elastic Load Balancing.**
9. **Firewall Protection:**
   - NACLS and Security Groups to secure the VPC.

---

# Route 53

- **Definition:**  
  A highly available and scalable domain name system (DNS) service.

- **Functionality:**  
  Route end users to internet applications by translating names like `www.nicevibes.co` into numeric IP addresses like 192.0.2.1 that computers use to connect with each other.
  
- **Supports:**  
  - IPv4 and IPv6

![Route 53 Diagram](https://github.com/user-attachments/assets/8fd789cb-1a50-4cc2-9b25-b0944f5d20a3)
![image](https://github.com/user-attachments/assets/4616c315-e236-4c45-9613-75e1887edd63)

---

## DNS Overview

- **DNS as a Phonebook:**  
  IP addresses of websites are stored as domain names, similar to how a phonebook stores names and numbers.

> [!NOTE]
> **Interview Question:** Explain what happens when you hit a URL.

## Routing Policies

- **Simple Routing:**  
  Round-robin for single server environments or small portions of traffic to a server.
  
- **Weighted Round Robin:**  
  Assign weights to resource record sets to specify frequency. Example: A/B testing with 90% traffic to the main website and 10% to a test website.
  
- **Latency Routing:**  
  Improve global application performance by routing based on latency.
  
- **Geolocation Routing:**  
  Route traffic based on user location.
  
- **Geoproximity Routing:**  
  Route traffic based on your resources.
  
- **Failover Routing:**  
  Failover to a backup site if your primary site becomes unreachable.

### DNS Failover Example:

- **High Availability:**
  1. Create two DNS records (CNAME) with failover routing.
  2. Primary routing policy: Load balancer for web application.
  3. Secondary policy: S3 static website.
  4. Health checks ensure the primary site works correctly. If it fails, the web application stack fails over to the static backup site.
![image](https://github.com/user-attachments/assets/cd0d4043-4280-4114-a368-e67cb2b9529b)

---

# Amazon CloudFront

### Content Delivery and Network Latency

- **Challenge of Network Communication:**  
  Network performance can be impacted by latency, especially depending on the geographical location of the user.

### Amazon CloudFront

- **Overview:**  
  Amazon CloudFront is a fast, global, and secure Content Delivery Network (CDN) service.

- **Features:**
  - **Global Network:**  
    Utilizes a global network of edge locations and regional edge caches.
  - **Self-Service Model:**  
    Allows users to manage and deploy CDN services easily.
  - **Pay-as-You-Go Pricing:**  
    Flexible pricing model based on usage.

### Infrastructure

- **How it Works:**
  - When a customer makes a request, CloudFront responds with the IP address of the edge location closest to the customer.
  - CloudFront obtains the requested data and caches it at the edge location to serve it quickly in subsequent requests.

### Edge Locations

- **Definition:**  
  Edge locations are data centers that CloudFront uses to deliver popular content quickly to users.

- **Regional Edge Cache:**
  - Acts as an intermediary between the origin server and global edge locations.
  - Stores content that isn't popular enough to remain at the edge location but may still be requested.
  - When data becomes stale, it is removed from the edge location's cache.

<details>
  <summary>Which AWS networking service enables a company to create a virtual network within AWS?</summary>

  **Answer:** Amazon VPC (Virtual Private Cloud)  
  A VPC allows you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
</details>


---

# EC2 Instance (Elastic Compute Cloud)

### Background Context
Running servers on-premise can be:
- **Expensive**: Purchase, data centers, maintenance, staff.
- **Hardware Management**: Managing peak workloads; server capacity sits idle.

### EC2 Provides:
- **Virtual Machines** to host the same applications as on-premise servers.
- **Example Uses**: Application server, web server, game server, database server.
- **Full Control** over the guest operating system (Linux/Windows).
- **Control Traffic** to and from instances using security groups.

### Key EC2 Components:
1. **AMI**: Linux/Windows (template)
2. **Instance Type**: The type of instance you want to launch.
3. **Network Settings**: Configure VPC, subnets, and public IP settings.
4. **IAM Role**: Attach a role to allow the instance to interact with AWS services.
5. **User Data**: Script that runs on the first start to customize the instance.
6. **Storage Options**: Configure the root volume and additional volumes.
7. **Tags**: Labels to categorize and organize resources.
8. **Security Groups**: Firewall rules that control traffic to the instance.
9. **Key Pair**: Used for secure access to your instances.

---

### 1. Amazon Machine Image (AMI)
- **Definition**: A template used to create an EC2 instance.
- **Content**: Windows or Linux OS, often with pre-installed software.

#### AMI Choices:
- **Quick Start**: Linux and Windows AMIs provided by AWS.
- **My AMIs**: Any AMIs that you created.
- **AWS Marketplace**: Pre-configured templates from third parties.
- **Community AMIs**: AMIs shared by others; use at your own risk.

![AMI Image](https://github.com/user-attachments/assets/a8a25673-63b0-4527-8c1f-0eaa6ac78cf8)

![AMI Selection](https://github.com/user-attachments/assets/debcc63a-cc8a-4bb0-8793-f095ee5559ff)

#### AMI Flowchart:
1. **Launch Instance** (Unmodified Instance)
2. **Connect to Instance** and run a script (e.g., install Python)
3. **Capture** as a new AMI
4. **Copy New AMI** to any other regions

---

### 2. Instance Type
- **Memory (RAM)**
- **Processing Power**
- **Disk Storage and Space**
- **Network Performance**

#### Instance Types Table:
| Instance Types       | Name      | vCPU | GB  |
|----------------------|-----------|------|-----|
| General Purpose      | t3.nano   | 2    | 0.5 |
| Compute Optimized    | t3.micro  | 2    | 1   |
| Memory Optimized     | t3.small  | 2    | 2   |
| Storage Optimized    | t3.medium | 2    | 4   |
| Accelerated Computing | t3.large  | 2    | 8   |
|                      | t3.xlarge | 4    | 16  |
|                      | t3.2xlarge | 8   | 32  |

![Instance Type Image](https://github.com/user-attachments/assets/e9ed8551-17cb-4de6-a54b-1d729cecb7df)
![Instance Type Graph](https://github.com/user-attachments/assets/7cf24746-33c9-4e04-a880-2514e29a62c3)
![Instance Type Comparison](https://github.com/user-attachments/assets/0992d991-d950-4a32-b531-fc095652176d)

---

### 3. Specify the Instance Deployment under VPC
- **Deployment Location**: Identify the VPC and optionally the subnet.
- **Public IP Assignment**: To make it internet-accessible.

![VPC Image](https://github.com/user-attachments/assets/47660088-f5b7-41a6-bd84-63dfb783d170)

---

### 4. Attach IAM Role (Optional)
- **Purpose**: Allows the EC2 instance to interact with other AWS services.
- **IAM Role**: An AWS Identity and Access Management role attached to an EC2 instance within an instance profile.

#### Example: 
Grant a role to S3, allowing an application on the instance to access an S3 bucket.

---

### 5. User Data Script (Optional)
- **Customization**: Customize the runtime environment of your instance.
- **Execution**: Script executes the first time the instance starts.
- **Strategic Use**: Reduce the number of custom AMIs you need to build and maintain.

---

### 6. Specify Storage
- **Root Volume**: Where the guest OS is installed.
- **Additional Volumes**: Optionally attach more storage volumes.

#### Volume Configuration:
- **Size of the Disk**: In GB.
- **Volume Type**: Different types of SSDs and HDDs.
- **Retention**: If the volume will be deleted when the instance is terminated.
- **Encryption**: Should encryption be used?

#### Amazon EC2 Storage Options:
- **Amazon Elastic Block Store (Amazon EBS)**: Durable, block-level storage volumes.
- **Amazon Elastic File System (Amazon EFS)**: Mount a file system.
- **Amazon S3**: Connect to Simple Storage Service.

![Storage Options Image](https://github.com/user-attachments/assets/05a79351-8bf4-460b-aa04-49f27d4eafbd)

#### Instance Characteristics:
- **Instance 1**: Amazon EBS root volume type for the OS.
  - OS volume survives after stopping and starting.
  - Data in ephemeral volume 1 is lost.
- **Instance 2**: Instance Store root volume type for the OS.
  - All data stored in ephemeral volume 2 is lost, including the OS.

---

### 7. Add Tags
- **Tagging**: Assign labels (key-value pairs) to AWS resources.
- **Benefits**: Filtering, automation, cost allocation, and access control.

---

### 8. Security Group Settings
- **Firewall Rules**: Control traffic to the instance outside the guest OS.
- **Rule Creation**: Specify source, port number, protocol, and allowed source.

---

### 9. Identify the Key Pair
- **Key Pair**: Consists of a public key (stored by AWS) and a private key file (stored by you).
- **Windows AMIs**: Use the private key to obtain the administrator password.
- **Linux AMIs**: Use the private key to SSH into your instance securely.

![EC2 Instance Image](https://github.com/user-attachments/assets/32d8cfc6-5f57-4357-8a05-277b12c4acd8)

---

### Another Option: Launch an EC2 Instance with the AWS CLI
- **AWS CLI Command Example**:
  ```bash
  aws ec2 run-instances --image0id ami-1a2b3c4d --count 1 --instance-type c3.large \
  --key-name MyKeyPair --security-groups MySecurityGroup --region us-east-1
  ```

#### This command assumes that the key pair and security group already exist.

---

### Amazon EC2 Instance Lifecycle
![Lifecycle Image](https://github.com/user-attachments/assets/c18319be-258c-41e0-8df4-4e7695d814f9)

#### Elastic IP Address Consideration
- **Rebooting**: Will not change IP addresses or DNS hostnames.
- **Stopping and Starting**: Public IPv4 address and external DNS hostname will change, private IPv4 address and internal DNS hostname do not.
- **Persistent Public IP**: Associate an Elastic IP address.

---

### EC2 Instance Metadata
- **Data Retrieval**: View instance data while connected.
  - **Browser**: `http://169.254.169.254/latest/meta-data/`
  - **Terminal**: `curl http://169.254.169.254/latest/meta-data/`

#### Example Retrievable Values:
- Public IP address, private IP address, public hostname, instance ID, security groups, Region, Availability Zone.

---

### Amazon CloudWatch for Monitoring
- **Monitoring EC2 Instances**: Provides near-real-time metrics, charts, and historical data (15 months).
- **Basic Monitoring**: Default, no additional cost, metric data sent every 5 minutes.
- **Detailed Monitoring**: Fixed monthly rate, metric data delivered every 1 minute.

---

# Amazon EC2 Cost Optimization

## Amazon EC2 Pricing Models

### On-Demand Instances
- **Pay**: By the hour
- **Commitment**: No long-term commitments
- **Eligibility**: Eligible for the AWS Free Tier

### Dedicated Hosts
- **Definition**: A physical server with EC2 instance capacity fully dedicated to your use

### Dedicated Instances
- **Definition**: Instances that run in a VPC on hardware dedicated to a single customer

### Reserved Instances
- **Payment Options**: Full, partial, or no upfront payment for instances you reserve
- **Discount**: Discount on hourly charge for that instance
- **Term**: 1-year or 3-year term

### Scheduled Reserved Instances
- **Definition**: Purchase a capacity reservation that is always available on a recurring schedule you specify
- **Term**: 1-year term

### Spot Instances
- **Pricing**: Instances run as long as they are available and your bid is above the Spot Instance price
- **Interruption**: Can be interrupted by AWS with a 2-minute notification; options include terminated, stopped, or hibernated
- **Cost**: Prices can be significantly less expensive compared to On-Demand Instances
- **Best For**: Good choice when you have flexibility in when your applications can run

### Benefits

|                   | On-Demand Instances         | Spot Instances                  | Reserved Instances               | Dedicated Hosts                  |
|-------------------|------------------------------|---------------------------------|---------------------------------|----------------------------------|
| **Cost & Flexibility** | Low cost and flexibility     | Large scale, dynamic workload   | Predictability ensures compute capacity is available when needed | Save money on licensing costs <br> Help meet compliance and regulatory requirements |

### Use Cases
![image](https://github.com/user-attachments/assets/3c90fee2-90d2-4f26-8673-1d3677003540)

## The 4 Pillars of Cost Optimization
![4pillars](https://github.com/user-attachments/assets/fca16bb3-59c4-4774-bc8a-46c995424fc1)

### Pillar 1: Right Size
- **Provision Instances**: Match the instances to your actual needs in terms of CPU, memory, storage, and network throughput.
- **Instance Types**: Select the appropriate instance types for your use case.
- **Monitoring**: Use Amazon CloudWatch metrics to assess instance utilization and identify idle instances.
- **Optimization**: Downsize instances as needed.
- **Best Practice**: Right-size instances before considering Reserved Instances.

### Pillar 2: Increase Elasticity
- **Stop or Hibernate**: For Amazon EBS-backed instances that are not actively in use, such as non-production development or test instances.
- **Automatic Scaling**: Use scaling policies to adjust capacity based on usage.
- **Elasticity Types**:
  - Automated scaling
  - Time-based scaling

### Pillar 3: Optimal Pricing Model
- **Pricing Models**: Choose the right pricing model based on your usage patterns.
- **Optimization**:
  - **On-Demand and Spot Instances**: For variable workloads.
  - **Reserved Instances**: For predictable workloads.
  - **Serverless Solutions**: Consider AWS Lambda for certain use cases.

### Pillar 4: Optimize Storage Choices
- **Cost Reduction**: Reduce costs while maintaining storage performance and availability.
- **EBS Volume Management**:
  - Resize EBS volumes as needed.
  - Change EBS volume types if appropriate.
  - Evaluate if performance requirements can be met with less expensive storage.
- **Examples**: Amazon EBS Throughput Optimized HDD (st1) storage is typically cheaper than General Purpose SSD (gp2).
- **Cleanup**: Delete unnecessary EBS snapshots.
- **Data Storage**: Determine the most suitable storage destination.
  - Consider Amazon S3 storage options with lifecycle policies to reduce costs.

### Measure, Monitor, and Improve
- **Ongoing Process**: Cost optimization should be continuous.
- **Recommendations**:
  - Define and enforce cost allocation tagging.
  - Define metrics, set targets, and review regularly.
  - Encourage cost-effective architecture designs.
  - Assign responsibility for optimization to an individual or team.

---

# Container Services

## Container Basics
- **Definition**: Containers are a method of operating system virtualization.
- **Benefits**:
  - **Repeatable**: Consistent environments across different stages (development, test, production).
  - **Self-Contained**: Environments encapsulate everything needed to run the software.
  - **Efficiency**: Faster to launch, stop, or terminate compared to virtual machines.

> [!NOTE]
> Containers are smaller than virtual machines (VMs) and do not have a complete operating system. Instead, they use a virtualized OS and run as resource-isolated processes.

Feel free to adjust or expand as needed!

## What is Docker?
- **Definition**: Docker is a software platform that facilitates building, testing, and deploying applications quickly.
- **Containers**: Run on Docker and are created from images (templates).
  - **Components**: Containers include all the dependencies required for the application to run.

### Containers vs VMs
- **Containers**:
  - Share the host OS kernel.
  - More lightweight and faster to start.
- **Virtual Machines (VMs)**:
  - Include a full OS along with the application.
  - Generally more resource-intensive.

![Containers vs VMs](https://github.com/user-attachments/assets/3aeaf742-3fa8-4141-a914-e4b10f6ec35c)


# Amazon Elastic Container Service (Amazon ECS)

A highly scalable, fast, container management service.

## Key Benefits
- Orchestrates the running of Docker containers
- Maintains and scales the fleet of nodes that run your containers
- Removes the complexity of standing up the infrastructure
- Integrated with features that are familiar to Amazon EC2 service users:
  - Elastic Load Balancing
  - Amazon EC2 security groups
  - Amazon EBS volumes
  - IAM roles

Amazon ECS orchestrates containers.
![image](https://github.com/user-attachments/assets/3d9da6a0-a6f7-40a8-93af-59ac53f7bedb)

## Amazon ECS Cluster Options

Do you want to manage the Amazon ECS cluster that runs the containers?

- **Yes:** Create an Amazon ECS cluster backed by Amazon EC2
  - Provides more granular control over infrastructure
- **No:** Create an Amazon ECS cluster backed by AWS Fargate
  - Easier to maintain, focus on your app
![image](https://github.com/user-attachments/assets/ef8623ea-dc45-4fcf-bdbc-22895369c204)

## What is Kubernetes?

**Comment:** Kubernetes is open-source software for container orchestration. It deploys and manages containerized apps at scale. The same toolset can be used on-premises and in the cloud.

- **Complements Docker:**
  - Docker enables you to run multiple containers on a single OS host.
  - Kubernetes orchestrates multiple Docker hosts (nodes).
- **Automates:**
  - Container provisioning
  - Networking
  - Load distribution
  - Scaling

### Amazon Elastic Kubernetes Service (Amazon EKS)

- **EKS:** Enables you to run Kubernetes on AWS
- Certified Kubernetes conformant
- Supports Linux and Windows containers
- Compatible with Kubernetes community tools and add-ons
- Use Amazon EKS to:
  - Manage clusters of Amazon EC2 instances
  - Run containers that are orchestrated by Kubernetes on those instances

## Amazon Elastic Container Registry (Amazon ECR)

Amazon ECR is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.

### Supports:
- Team collaboration
- Access control
- Third-party integration
- Possible to use with Amazon EKS

# Section 7: Introduction to AWS Lambda

AWS Lambda: Run code without servers. AWS Lambda is a serverless compute service.
![image](https://github.com/user-attachments/assets/8de1e600-4a8d-4a02-87a4-3bd3b2ab350e)

## Benefits of Lambda
- Supports multiple programming languages
- Completely automated administration
- Built-in fault tolerance
- Supports orchestration of multiple functions
- Pay-per-use pricing

## AWS Lambda Event Sources
![image](https://github.com/user-attachments/assets/c09952ee-0dcb-495c-8353-d697f6bf4b61)

### AWS Lambda Function Configuration
- Create lambda function: Give a name
- Runtime environment:
  - Python
  - Node.js
- Execution role to grant IAM permission to the function to interact with other services
- Configure the function:
  - Adding a trigger
  - Add function code
  - Specify the memory in megabytes (up to 3008 MB)
  - Specify environment variables
![image](https://github.com/user-attachments/assets/4c92930e-fcf2-4a2e-8cc1-d28897f03d95)

### Examples:
- **Schedule-based Lambda Function:** Start and stop EC2 instances

  ![image](https://github.com/user-attachments/assets/2334a666-a0a0-46ac-bf16-11a233bdf0ce)

- **Event-based Lambda Function:** Create thumbnail images
![image](https://github.com/user-attachments/assets/cabe217f-2dc6-45e2-9e8a-b5845492e79b)

### AWS Lambda Limits
- **Soft limits per Region:**
  - Concurrent executions = 1,000
  - Function and layer storage = 75 GB
- **Hard limits for individual function:**
  - Max function memory allocation = 3,008 MB
  - Function timeout = 15 min
  - Deployment package size = 250 MB unzipped, including layers

# Section 8: Introduction to AWS Elastic Beanstalk

AWS Elastic Beanstalk: An easy way to get a web app up and running. A managed service that automatically handles:
- Infrastructure provisioning and configuration
- Deployment
- Load balancing
- Automatic scaling
- Health monitoring
- Analysis and debugging
- Logging

No additional charge for Elastic Beanstalk. Pay only for the underlying resources that are used.

## AWS Elastic Beanstalk Deployments
- Supports web apps written for common platforms:
  - Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker
- You upload your code
- Elastic Beanstalk automatically handles the deployment
- Deploys on servers such as Apache, NGINX, Passenger, Puma, and Microsoft Internet Information Services (IIS)

## Benefits of Elastic Beanstalk
![image](https://github.com/user-attachments/assets/b4d926c1-5b3a-4a20-91f4-9d3d8d328870)

# Wrap-up

**Which AWS service helps developers quickly deploy resources which can make use of different programming languages, such as .NET and Java?**

<details>
  <summary>Select your answer</summary>
  
  - AWS CloudFormation
  - AWS SQS
  - AWS Elastic Beanstalk
  - Amazon Elastic Compute Cloud (Amazon EC2)

**Answer:** AWS Elastic Beanstalk

**Keywords:**
- Developers quickly deploy resources
- Different programming languages
</details>

# Module 7: Storage

## Section 1: Amazon Elastic Block Store (Amazon EBS)

### Storage
- Provides persistent block storage volumes with Amazon EC2 instances
- Called non-volatile storage
- Replicated within AZ
- AWS Storage options: block storage vs object storage
- What if you want to change one character in a 1-GB file?
![image](https://github.com/user-attachments/assets/79448924-44e1-4df8-96f0-23d2fc3b1e45)

### Amazon EBS
> [!NOTE] Amazon EBS enables you to create individual storage volumes and attach them to an Amazon EC2 instance
- Amazon EBS offers block-level storage
- Volumes are automatically replicated within its AZ
- Can be backed up automatically to Amazon S3 through snapshots

#### Uses include:
- Boot volumes and storage for Amazon Elastic Compute Cloud (Amazon EC2) instance
- Data storage with a file system
- Database hosts
- Enterprise app

### Amazon EBS Volume Types
![image](https://github.com/user-attachments/assets/ff93adf9-63ac-42df-a9f8-b35ccca2456f)

#### Snapshots
- Point-in-time snapshots
- Recreate a new volume at any time

#### Encryption
- Encrypted Amazon EBS volumes
- No additional cost

#### Elasticity
- Increase capacity
- Change to different types

#### Volumes, IOPS and Pricing
- **Volumes**: Amazon EBS volumes persist independently from the instance
  - All volume types are charged by the amount that is provisioned per month
- **IOPS**:
  - General Purpose SSD: Charged by the amount that you provision in GB per month until storage is released
  - Magnetic: Charged by the number of requests to the volume
  - Provisioned IOPS SSD: Charged by the amount that you provision in IOPS (multiplied by the percentage of days that you provision for the month)
- **Snapshots**: Added cost of Amazon EBS snapshots to Amazon S3 is per GB-month of data stored
- **Data Transfer**:
  - Inbound data transfer is free
  - Outbound data transfer across Regions incurs charges

## Section 2: Amazon Simple Storage Service (Amazon S3)

### Storage
> [!NOTE] Amazon S3 is object-level storage
- If you want to change part of a file, you must do the change and re-upload the entire file

### Amazon S3 Overview
- Data stored as objects in buckets
- Virtually unlimited storage
- Single object is limited to 5 TB
- Designed for 11 9s of durability
- Granular access to bucket and objects
- Data private by default
- Can set up notification:
  - When object is added
  - When object is deleted

### Amazon S3 Storage Classes
- **Amazon S3 Standard**: High availability, high durability, performance, frequently accessed data
- **Amazon S3 Intelligent-Tiering**: Optimize cost by moving data to the most cost-effective access tier, long-lived data with unpredictable access pattern
- **Amazon S3 Standard-Infrequent Access (Amazon S3 Standard-IA)**: Data accessed less frequently, long-term storage
- **Amazon S3 One Zone-Infrequent Access (Amazon S3 One Zone-IA)**: Data accessed less frequently, stores data in a single availability zone
- **Amazon S3 Glacier**: Secure, durable, low cost, data archiving, three retrieval options (minutes to hours)
- **Amazon S3 Glacier Deep Archive**: Lowest cost, long-term retention, retrieved once or twice a year

### Amazon S3 Bucket URLs (Two Styles)
- **Bucket Path-Style URL Endpoint**: `https://s3.ap-northeast-1.amazonaws.com/bucket-name`
- **Bucket Virtual-Hosted-Style URL Endpoint**: `https://bucket-name.s3-ap-northeast-1.amazonaws.com`

- Data is redundantly stored in the Region
- Designed for seamless scaling
  ![image](https://github.com/user-attachments/assets/69d6a6ec-1bca-4caf-a560-e0b2a86c0a34)

- Amazon S3:
  - Automatically manage the storage
  - Scales to handle high volume of requests
  - Billed for what you use
- Access the data anywhere:
  - AWS CLI
  - AWS Management Console
  - SDK
-> [!WARNING]  
> Bucket names must be globally unique and DNS compliant: all lowercase, only letters, numbers, and dashes

### Amazon S3 Common Scenarios
- Backup and storage
- Application hosting
- Media hosting
- Software
![image](https://github.com/user-attachments/assets/2640339a-5a87-4dac-8142-19596f419102)

### Amazon S3 Pricing
- Pay for what you use:
  - GBs per month
  - Transfer OUT to other Regions
  - PUT, COPY, POST, LIST, and GET requests
- You do not pay for:
  - Transfers IN to Amazon S3
  - Transfers OUT from Amazon S3 to Amazon CloudFront or Amazon EC2 in the same region

### Amazon S3: Storage Pricing
- **To estimate Amazon S3 costs**:
  - Types of storage classes
  - Standard storage is for:
    - 11 9s of durability
    - 4 9s of availability
  - S3 Standard-Infrequent Access (S-IA) is for:
    - 11 9s of durability
    - 3 9s of availability
  - Amount of storage
  - The number and size of objects
  - Requests:
    - Number of requests (GET, PUT, COPY)
    - Type of requests
    - Different rates for GET requests
  - Data transfer:
    - Pricing based on the amount of data transferred out of Amazon S3 Region
    - Data transfer in is free, but incur charges for data transferred out

## Section 3: Amazon Elastic File System (Amazon EFS)

### Storage
> [!Note] Implements storage for EC2 instances

### Features
- File storage in the AWS Cloud
- Works well for big data and analytics, media processing workflows, content management, web serving, and home directories
- Petabyte-scale, low-latency file system
- Shared storage
- Elastic capacity:
  - Gigabytes to petabytes of data
- Supports Network File System (NFS) versions 4.0 and 4.1 (NFSv4)
- Compatible with all Linux-based AMIs for Amazon EC2
- Pay for what you use

### Amazon EFS Architecture
- Create your Amazon EC2 resources and launch your instance
- Create your Amazon EFS file system
- Create your mount targets in the appropriate subnets
- Connect your Amazon EC2 instances to the mount targets
- Verify the resources and protection of your AWS account
![image](https://github.com/user-attachments/assets/e0aca94d-58f6-4b34-9c81-dd749ed5e8b7)

### Amazon EFS Resources
- **Mount Target**:
  - Subnet ID
  - Security groups
  - One or more per file system
  - Create in a VPC subnet
  - One per AZ
  - Must be in the same VPC
- **Tags**:
  - Key-value pairs

## Section 4: Amazon S3 Glacier

### Storage
> [!Note] Secure, durable, and extremely low-cost data archiving

### Archive
- Any object such as photo, video, file, or document stored in Amazon S3 Glacier
- Base unit of storage: unique ID
- **Vault**:
  - Container for storing archive
  - Specifies vault name
  - Permissions access policy
  - Vault lock policy

### Amazon S3 Glacier Review
- Designed to provide 11 9s of durability for objects
- Supports encryption of data in transit/at rest through Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
- Vault lock: enforces compliance through a policy
- Extremely low-cost for long-term archiving
- Three options: expedited, standard, or bulk
  - Retrieval times from a few minutes to hours
![image](https://github.com/user-attachments/assets/76aac8f3-6e41-4886-93bd-1785c45382b2)

### Amazon S3 Glacier Use Cases
- Media asset archiving
- Healthcare info archiving
- Regulatory and compliance archiving
- Scientific data archiving
- Digital preservation
- Magnetic tape replacement

### Using Amazon S3 Glacier
- RESTful web services
- Java or .NET SDKs
- Amazon S3 with lifecycle policies

### Lifecycle Policies
- Amazon S3 lifecycle policies enable you to delete or move objects based on age
![image](https://github.com/user-attachments/assets/88f0cbca-1e96-4ce8-b152-af908eb1c7a4)

## AWS Storage Classes
![image](https://github.com/user-attachments/assets/0001eeb0-29bf-457f-9e46-a4ad23d0f46d)

## Storage Comparison
![image](https://github.com/user-attachments/assets/dd99223e-39f4-40ed-9e81-56f427ba7ad5)

### Server-side Encryption
![image](https://github.com/user-attachments/assets/437b366b-f58c-4168-9cea-6998f0a1a97d)

#### Server-side Encryption (SSE)
- **SSE-S3**:
  - Each object has a unique key
  - AES 256
- **SSE-C**:
  - Own encryption keys
  - AWS Key Management Service
  - Scaled for the cloud
  - Customer master keys
  - IAM Console or API
  - Access keys
  - How keys can be used

### Security with Amazon S3 Glacier
- Control access with IAM
- Amazon S3 Glacier encrypts your data with AES-256
- Amazon S3 Glacier manages your keys for you

## Wrap-up

A company wants to store data that is not frequently accessed. What is the best and cost-effective solution that should be considered?

<details>
  <summary>Select your answer</summary>
  
  - Amazon S3 Storage Gateway
  - Amazon S3 Glacier
  - Amazon EBS
  - Amazon S3

**Answer:** Amazon S3 Glacier

**Keywords:**
- Not frequently accessed
- Cost-effective solution
</details>
