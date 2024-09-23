# Database Management System (DBMS)

A **Database Management System (DBMS)** is software designed to manage and organize data in a structured way. It allows users to create, modify, and query databases, while also managing security and access controls. A DBMS provides an efficient environment for storing and retrieving data.

---

## Differences Between File System and DBMS

| **Aspect**            | **File System**                                            | **DBMS**                                                  |
|-----------------------|----------------------------------------------------------|----------------------------------------------------------|
| **Structure**         | Arranges files in a storage medium on a computer.       | Manages data in a structured database.                   |
| **Data Redundancy**   | Can contain redundant data.                              | Eliminates redundant data through normalization.          |
| **Backup and Recovery**| Lacks inbuilt backup and recovery mechanisms.            | Provides tools for backup and recovery of lost data.     |
| **Query Processing**   | Inefficient query processing.                            | Efficient query processing capabilities.                  |
| **Consistency**        | Less data consistency.                                   | Ensures more data consistency through normalization.      |
| **Security Constraints**| Offers less security.                                   | Implements advanced security mechanisms.                  |
| **User Access**        | Typically allows only one user at a time.              | Supports multiple users accessing data simultaneously.     |

### Example:
- **File System**: A simple text file to store customer details.
- **DBMS**: A relational database like MySQL managing a customer database with multiple tables.

---

## Differences Between Two-Tier and Three-Tier Database Architecture

| **Aspect**                 | **Two-Tier Architecture**                                | **Three-Tier Architecture**                              |
|----------------------------|---------------------------------------------------------|---------------------------------------------------------|
| **Type**                   | Client-Server Architecture.                             | Web-based application.                                   |
| **Application Logic**      | Logic is integrated either in the client or server.    | Logic is separated into a middle-tier (business logic). |
| **Layers**                 | Consists of Client Tier and Database (Data Tier).      | Comprises Client Layer, Business Layer, and Data Layer. |
| **Complexity**             | Easier to build and maintain.                           | More complex to build and maintain.                     |
| **Performance**            | Generally slower.                                       | Typically faster.                                       |
| **Security**               | Less secure; clients can communicate directly with the database. | More secure; clients do not directly access the database. |
| **Performance Impact**     | Performance may degrade with increased users.           | Better performance on the Internet, though may still experience issues with high loads. |

### Example:
- **Two-Tier**: A Contact Management System built with MS Access.
### Three-Tier Architecture

Almost all web applications operate on a three-tier architecture:

1. **Presentation Tier**: 
   - The web browser serves as the presentation tier. 
   - It interacts with the user to present and capture data/information.

2. **Application Tier**: 
   - This tier handles the dynamic aspects of the website. 
   - Development tools such as ASP, Java, PHP, Ruby on Rails, and Python (along with frameworks like Django) represent this second tier.

3. **Database Tier**: 
   - The database resides in the server-level infrastructure, forming the third tier. 
   - Technologies like Oracle, MySQL, and MS SQL, along with server-level operating systems, constitute this layer.

Almost all dynamic websites depend on this three-tier architecture.


![image](https://github.com/user-attachments/assets/e85b2319-ea19-41a0-819d-6775960a9935)

![image](https://github.com/user-attachments/assets/df8022dc-4e0c-4eee-9aae-815250a56d83)


## Schema :  logical representation of data 

## logical representation in rdbms -> tables eg : student -> table[rno.,name,marks], course->[course id, name, instructor] , in er models -> entitites

# DBMS 3-Tier Architecture

The 3-tier architecture in a Database Management System (DBMS) provides a logical framework for data organization and independence. It consists of three levels:

## 1. Physical Level
- **Description**: This level details how data is physically stored in secondary storage devices (like disks and tapes). 
- **Example**: Information about the location of database objects (e.g., tables, indexes) is stored here. Users are unaware of these locations.
  
## 2. Conceptual Level
- **Description**: Represents the logical structure of the database, showing how data is organized in tables.
- **Example**: 
  - **Tables**:
    - **STUDENT**: [Roll No, Age, Address, Name]
    - **COURSE**: [Course ID, Course Name, Instructor]
  - **Relationships**: Links between tables, such as a student enrolling in a course.

## 3. External Level
- **Description**: This level provides user-specific views of the data, tailored to different user needs.
- **Example**: 
  - **FACULTY View**: Course details of students.
  - **STUDENT View**: Academic records, accounts, courses, and hostel details.

---

## Data Independence

Data independence ensures that changes at one level do not impact other levels. There are two types:

### 1. Physical Data Independence
- **Definition**: Changes in the physical storage (e.g., relocating tables) do not affect the conceptual level or external views.
- **Example**: Moving the database to a new disk location will not alter how users interact with it.

### 2. Conceptual Data Independence
- **Definition**: Changes in the conceptual schema (like adding or deleting attributes) do not impact external views.
- **Example**: If a new column is added to the STUDENT table, it shouldn't change how students view their data, though this type of independence is harder to achieve.

---



