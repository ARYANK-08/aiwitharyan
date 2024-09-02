# AWS - Everything You Need to Know

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

**Note**: Follow the principle of least privilege (minimal set of permissions required).

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
- A computer network is two or more client machines connected together to share resources.

![Networking Basics](https://github.com/user-attachments/assets/da67918f-9811-4310-b09e-c572e00d2e62)

- Each client machine has a unique IP.
  - Example: 192 = `11000000` 0 = `00000000` 2 = `0000010` 0 = `00000000`
  - **IPv4 (32 bits)**: `192.0.2.0`
  - **IPv6 (128 bits)**: `2600:1f18:22ba:8c00:ba86`

## CIDR (Classless Inter-Domain Routing)
Classless Inter-Domain Routing (CIDR) is a method of IP address allocation and IP routing that allows for more efficient use of IP addresses. CIDR is based on the idea that IP addresses can be allocated and routed based on their network prefix rather than their class, which was the traditional way of IP address allocation.

### Advantages of CIDR
- **Efficient use of IP addresses**: CIDR allows for more efficient use of IP addresses, which is important as the pool of available IPv4 addresses continues to shrink.
- **Flexibility**: CIDR allows for more flexible allocation of IP addresses, which can be important for organizations with complex network requirements.
- **Better routing**: CIDR allows for more efficient routing of IP traffic, which can lead to better network performance.
- **Reduced administrative overhead**: CIDR reduces administrative overhead by allowing for easier management of IP addresses and routing.

![CIDR Example](https://github.com/user-attachments/assets/8bdf19d3-416a-4f33-a788-d9cd25f1518f)
![CIDR Range](https://github.com/user-attachments/assets/26711456-6f37-4873-95d5-8473bc7df765)

**Example**: `192.0.2.0/24` -> The last number (24) tells you that the first 24 bits must be fixed, and the last 8 bits are flexible -> `2^8 = 256 IP addresses`.
- **Range**: `192.0.2.0` to `192.0.2.255`.
  - **Special Cases**:
    - Fixed: `192.0.2.0/24`
    - Flexible: `0.0.0.0/0`

## OSI Model
Explains how data travels over a network.

| Layer        | Number | Function                                           | Protocol                        |
|--------------|--------|----------------------------------------------------|---------------------------------|
| Application  | 7      | Means for an application to access the network     | HTTPS, FTP, LDAP, DHCP          |
| Presentation | 6      | Encryption, ensuring application layer reads data  | ASCII, ICA                      |
| Session      | 5      | Enables orderly exchange of data                   | NETBIOS, RPC                    |
| Transport    | 4      | Provides protocols to support host-to-host comm.   | TCP, UDP                        |
| Network      | 3      | Routing and packet forwarding (routers)            | IP                              |
| Data Link    | 2      | Reliable transfer of data across physical link     | ARP                             |
| Physical     | 1      | Transmit raw bit stream (hubs)                     | Ethernet, FDDI                  |

**Example**: A web browser sends a request to `www.google.com`. This action triggers the following:

- Application layer -> Presentation layer -> Session layer -> Transport layer (TCP/IP) -> Network layer (IP) -> Data link layer (MAC) -> Physical layer (Ethernet)
- The OSI model ensures the seamless transmission of data from one network to another.

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

- **Definition:**  
  An Internet Gateway allows communication between EC2 instances in your VPC and the internet.
  
- **Route Table Example:**
  - **Destination | Target**
    - 10.0.0.0/16 | Local
    - 0.0.0.0/0 | Internet Gateway ID

---

## NAT Gateway (Network Address Translation Gateway)

- **Definition:**  
  Allows instances in private subnets to connect to the internet or AWS services while preventing the internet from initiating a connection to them.

- **VPC Sharing:**  
  Share a subnet with other AWS accounts within the same organization, enabling services like EC2, RDS, Lambda, and Redshift.

- **VPC Peering:**  
  A VPC-to-VPC connection.

- **AWS Direct Connect:**  
  Connects a VPC to a remote network.

![NAT Gateway Diagram](https://github.com/user-attachments/assets/337dc9d0-b4a6-46ec-8a95-a86cd7bdd32e)

---

## Security Groups

- **Definition:**  
  Acts as a virtual firewall for your instances, controlling inbound and outbound traffic.
  
- **Characteristics:**
  - Operates at the instance level, not the subnet level.
  - Default Security Group: Denies all inbound traffic and allows all outbound traffic.
  
- **Example Rules:**
  - **Outbound Destination | Protocol | Port Range | Description**
    - 0.0.0.0/0 | All | All | IPv4 IP
    - ::/0 | All | All | IPv6 IP
  
  **Custom Rules:**
  - **Source | Protocol | Port | Description**
    - 0.0.0.0/0 | TCP | 80 | HTTP (IPv4)
    - ::/0 | TCP | 443 | HTTPS (IPv4)

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

---

## DNS Overview

- **DNS as a Phonebook:**  
  IP addresses of websites are stored as domain names, similar to how a phonebook stores names and numbers.

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

---

## AWS Services Summary:

| **Service**          | **Key Concepts**                  | **Characteristics**                                           |
|----------------------|-----------------------------------|---------------------------------------------------------------|
| **EC2**              | IaaS, Instance-based, Virtual Machines | Provision VMs that you can manage as you choose.              |
| **Lambda Function**  | Serverless computing, Function-based, Low cost | Write and deploy code that executes on a schedule or can be triggered by events. Use when possible. |
| **ECS/EKS/ECR/Fargate** | Container-based, Instance-based | Spin up and execute jobs more quickly.                        |
| **Elastic Beanstalk** | PaaS, Web applications            | Focus on building your application code, easily integrate with RDS, DNS. |

---
