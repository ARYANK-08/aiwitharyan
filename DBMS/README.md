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


| ![Image 1](https://github.com/user-attachments/assets/e85b2319-ea19-41a0-819d-6775960a9935) | ![Image 2](https://github.com/user-attachments/assets/df8022dc-4e0c-4eee-9aae-815250a56d83) |
|:---:|:---:|

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
# Integrity Constraints

Integrity constraints are rules defined in a database to maintain the accuracy, consistency, and reliability of data. They ensure that the data stored in the database adheres to predefined rules or conditions.

## Types of Integrity Constraints

| **Constraint Type**             | **Description**                                                                                | **Example**                          |
|----------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------|
| **1. Domain Constraints**        | Ensure that data values fall within a specified range or set.                                 | Age > 20, Mobile phone length = 10  |
| **2. Entity Integrity Constraints** | Ensure that each row in a table has a unique primary key that cannot be null.                | Roll Number as Primary Key (PK)     |
| **3. Referential Integrity**     | Ensure that foreign keys reference valid primary keys in related tables.                       | Foreign key references in student/course tables. |
| **4. Key Constraints**           | Ensure uniqueness of values in specified columns.                                             | Unique email addresses in a user table. |

### Key Concepts

- **Key**: An attribute used to uniquely identify rows in a table. For example, adding an Aadhaar number as a unique identifier.

#### Types of Keys

| **Key Type**        | **Description**                                                                                          | **Example**                             |
|---------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------|
| **1. Candidate Key**| A set of attributes that can uniquely identify a row. The primary key is chosen from this set.          | Aadhaar Number, Voter ID, Phone Number |
| **2. Primary Key**  | An attribute that is unique and not null.                                                                | Roll Number (e.g., 101)                |
| **3. Foreign Key**  | An attribute that references the primary key in the same or another table, maintaining referential integrity. | `rno` in the Course table referencing `rno` in the Student table. |


#### Student Table
| **rno (PK)** | **Name**  | **Address**     |
|--------------|-----------|------------------|
| 1            | Aryan     | Mumbai           |
| 2            | Myron     | Bandra           |
| 3            | Sharvin   | Chandigarh       |

#### Course Table
| **Course ID** | **Course Name** | **rno (FK)** |
|----------------|-----------------|---------------|
| C1             | DBMS            | 1             |
| C2             | OS              | 2             |

## Integrity in Action

### Insertion
Inserting a record into the base table (Student table) with `rno = 3` (Sharvin, Chandigarh) is valid since there is no existing foreign key constraint violation.

### Deletion
If we attempt to delete a student from the base table, such as `rno = 1` (Aryan), it may cause a violation if there are references to that `rno` in the Course table. 

### Solutions to Deletion Violations
1. **ON DELETE CASCADE**: Automatically deletes related records in the Course table when a record in the Student table is deleted.
2. **ON DELETE SET NULL**: Sets the foreign key value in the Course table to NULL when the corresponding record in the Student table is deleted.

- **Update with ON UPDATE CASCADE**: If the roll number changes from `9486` to `9701`, the referencing tables are automatically updated.
- **Insertion Violation**: Trying to enroll a student who does not exist in the Student table will result in a violation.
- **Deletion**: Deleting a record from the Student table where a roll number is enrolled in a course will not violate constraints if the foreign key references are handled appropriately.

---

# Super Key

A **Super Key** is a combination of attributes that can uniquely identify two tuples (rows) in a table. For example:
- **Candidate Key (CK)**: Roll Number
- **Super Key (SK)**: 
  - Roll Number + Name
  - Roll Number + Age

A super key is essentially a superset of any candidate key.

---

# ER Model

The **Entity-Relationship (ER) Model** is used for the logical representation of data in a conceptual manner. It helps in understanding system requirements easily, much like an architectural model of a building.

## Symbols Used in the ER Model

The ER Model consists of various symbols that represent different components:

- **Rectangles**: Represent **Entities**.
- **Ellipses**: Represent **Attributes**.
- **Diamonds**: Represent **Relationships** among Entities.
- **Lines**: Connect attributes to entities and show relationships.
- **Double Ellipses**: Represent **Multi-Valued Attributes**.
- **Double Rectangles**: Represent **Weak Entities**.
- **Dotted Ellipses**: Represent **Derived Attributes**.

### Example Images

| ![ER Model Example 1](https://github.com/user-attachments/assets/528a9e95-c7e8-40b3-8657-b4959c373763) | ![ER Model Example 2](https://github.com/user-attachments/assets/b7cda717-1804-4670-85da-06c9b8a3bbfe) |
|:---:|:---:|



---

# Types of Attributes

1. **Single vs. Multi-Valued Attributes**:
   - **Single Attribute**: Roll Number (e.g., `123`)
   - **Multi-Valued Attribute**: Mobile Number (e.g., `9876543210, 8765432109`)

2. **Simple vs. Composite Attributes**:
   - **Simple Attribute**: Age (cannot be broken down further)
   - **Composite Attribute**: Name (can be divided into First Name, Middle Name, Last Name) or Address (can be composed of Street, City, State, Country)

3. **Stored vs. Derived Attributes**:
   - **Stored Attribute**: Date of Birth (DOB) 
   - **Derived Attribute**: Age (calculated from DOB: Current Year - Year of Birth)

4. **Key vs. Non-Key Attributes**:
   - **Key Attribute**: Uniquely identifies each row (e.g., Roll Number, underlined in representation)
   - **Non-Key Attribute**: Does not uniquely identify rows.

5. **Required vs. Optional Attributes**:
   - **Required**: Must have a value.
   - **Optional**: Can have a null value.

---

# Degree of Relationships

1. **One-to-One (1-1)**:
   - Example: An employee works in one department.
   - **Employee Table**:
     | **eid (PK)** | **ename** | **age** |
     |---------------|-----------|---------|
     | e1            | Aryan     | 20      |
     | e2            | Myron     | 21      |
     | e3            | John      | 22      |

   - **Department Table**:
     | **did (PK)** | **dname** | **dlocation** |
     |---------------|-----------|---------------|
     | d1            | IT        | Bangalore     |
     | d2            | HR        | Delhi         |

   - **Works Table**:
     | **eid (FK)** | **did (FK)** |
     |---------------|---------------|
     | e1            | d1            |
     | e2            | d2            |

   ![One-to-One Example](https://github.com/user-attachments/assets/6dcee10f-546b-457e-995d-e4c7d0b7025e)

2. **One-to-Many (1-M)**:
   - Example: A customer can place many orders.
   - **Customer Table**:
     | **id (PK)** | **name** | **city**    |
     |--------------|----------|-------------|
     | c1           | A        | Delhi       |
     | c2           | B        | Mumbai      |

   - **Orders Table**:
     | **ono (PK)** | **item_name** | **cost** |
     |---------------|----------------|----------|
     | o1            | Bucket         | 100      |
     | o2            | Shoes          | 200      |
     | o3            | iPhone         | 300      |
     | o4            | Tablet         | 400      |

   - **Gives Table**:
     | **id (FK)** | **ono (FK)** | **date**  |
     |--------------|---------------|-----------|
     | c1           | o1            | 2023-01-01|
     | c1           | o2            | 2023-01-02|
     | c2           | o3            | 2023-01-03|
     | c2           | o4            | 2023-01-04|

   ![One-to-Many Example](https://github.com/user-attachments/assets/2dffe2b2-e9bb-4ae1-abaf-460c3b3ca0a6)

3. **Many-to-Many (M-N)**:
   - Example: Many students can enroll in many courses.
   - **Student Table**:
     | **rollno** | **name** | **age** |
     |-------------|----------|---------|
     | 1           | Aryan    | 20      |
     | 2           | Myron    | 21      |

   - **Course Table**:
     | **cid** | **name**  | **credit** |
     |---------|-----------|------------|
     | C1      | DBMS      | 3          |
     | C2      | OS        | 4          |

   - This relationship cannot be reduced as each student can enroll in multiple courses and vice versa.
   ![image](https://github.com/user-attachments/assets/244bd0c3-0ccb-4d2b-bcc7-549b01dcff76)

---

# Normalization

**Normalization** is the process of minimizing redundancy in a relation or set of relations. Redundancy can lead to insertion, deletion, and update anomalies. By organizing data efficiently, normalization helps maintain data integrity.

Normalization is achieved through various **Normal Forms** designed to eliminate or reduce redundancy in database tables.

---

## First Normal Form (1NF)

A relation is in **First Normal Form (1NF)** if:
1. All attributes contain only **single-valued** attributes.
2. The **attribute domain** does not change.
3. Every attribute/column has a **unique name**.
4. The order of data storage does not affect the relation.

### Example 1: Student Table

#### Table 1: Original Relation (Not in 1NF)

| **Roll No** | **Name** | **STUD_PHONE**       |
|-------------|----------|-----------------------|
| 1           | A        | 1234567890, 0987654321|
| 2           | B        | 2345678901            |
| 3           | C        | 3456789012, 1234567890|

In Table 1, the **STUD_PHONE** column contains multi-valued attributes, violating 1NF.

![image](https://github.com/user-attachments/assets/0ee758a5-c3a1-4405-aa4b-d824d7754a90)


#### Table 2: Decomposed Relation (In 1NF)

| **Roll No** | **Name** | **STUD_PHONE** |
|-------------|----------|------------------|
| 1           | A        | 1234567890       |
| 1           | A        | 0987654321       |
| 2           | B        | 2345678901       |
| 3           | C        | 3456789012       |
| 3           | C        | 1234567890       |

In Table 2, the relation is in 1NF because each attribute contains only single-valued attributes.

---

### Example 2: Courses Table

#### Table 3: Original Relation (Not in 1NF)

| **ID** | **Name** | **Courses**     |
|--------|----------|------------------|
| 1      | A        | c1, c2           |
| 2      | E        | c3               |
| 3      | M        | c2, c3           |

In Table 3, the **Courses** column is a multi-valued attribute, thus not in 1NF.

#### Table 4: Decomposed Relation (In 1NF)

| **ID** | **Name** | **Course** |
|--------|----------|------------|
| 1      | A        | c1         |
| 1      | A        | c2         |
| 2      | E        | c3         |
| 3      | M        | c2         |
| 3      | M        | c3         |

In Table 4, the relation is now in 1NF as each course is listed in a separate row, ensuring all attributes are single-valued.

![image](https://github.com/user-attachments/assets/867ff9ec-e0a5-4ae5-bae8-c149d1197e2c)

---
# Functional Dependency in Database Systems

## Definition
Functional dependency occurs when one attribute uniquely determines another attribute within a relation. It's expressed as \( A \→ B \), meaning attribute A functionally determines attribute B.

## Importance
Functional dependencies are crucial for understanding relationships among database entities and play a vital role in advanced concepts of Relational Database Systems.

---

## Examples of Functional Dependencies

### Example Table

| roll_no | name | dept_name | dept_building |
|---------|------|-----------|---------------|
| 42      | abc  | CO        | A4            |
| 43      | pqr  | IT        | A3            |
| 44      | xyz  | CO        | A4            |
| 45      | xyz  | IT        | A3            |
| 46      | mno  | EC        | B2            |
| 47      | jkl  | ME        | B2            |

### Valid Functional Dependencies

| Dependency                                          | Description                                                           |
|-----------------------------------------------------|-----------------------------------------------------------------------|
| roll_no → {name, dept_name, dept_building}         | roll_no determines name, dept_name, and dept_building.              |
| roll_no → dept_name                                 | roll_no can determine dept_name (subset).                            |
| dept_name → dept_building                           | Each dept_name corresponds to a unique dept_building.                |

### Invalid Functional Dependencies

| Dependency                                          | Reason                                                               |
|-----------------------------------------------------|----------------------------------------------------------------------|
| name → dept_name                                    | Same name can belong to different departments.                       |
| dept_building → dept_name                           | Multiple departments can share the same building.                    |

---

## Armstrong’s Axioms for Functional Dependencies

1. **Reflexivity**: If \( Y \) is a subset of \( X \), then \( X \→ Y \) holds.
   - Example: \( \{roll_no, name\} \→ name \)
  
2. **Augmentation**: If \( X \→ Y \) is valid, then \( XZ \→ YZ \) is also valid.
   - Example: \( \{roll_no, name\} \→ dept_building \) implies \( \{roll_no, name, dept_name\} \→ \{dept_building, dept_name\} \)

3. **Transitivity**: If \( X \→ Y \) and \( Y \→ Z \), then \( X \→ Z \).
   - Example: \( roll_no \→ dept_name \) and \( dept_name \→ dept_building \) imply \( roll_no \→ dept_building \)

---

## Types of Functional Dependencies

| Type                                         | Description                                                                                              | Example                                                 |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| **Trivial Functional Dependency**            | Dependent is a subset of the determinant.                                                              | \( \{roll_no, name\} \ → name \)               |
| **Non-Trivial Functional Dependency**        | Dependent is not a subset of the determinant.                                                           | \( roll_no \→ name \)                          |
| **Multivalued Functional Dependency**        | No functional dependency between dependents.                                                            | \( roll_no \→ \{name, age\} \)                 |
| **Transitive Functional Dependency**         | Indirect dependency via another attribute.                                                               | \( enrol_no \→ dept \) and \( dept \→ building_no \) imply \( enrol_no \→ building_no \) |
| **Fully Functional Dependency**               | A set of attributes uniquely determines another attribute.                                               | \( \{X\} \→ Y \)                               |
| **Partial Functional Dependency**             | A non-key attribute depends on part of a composite key.                                                | \( X \→ Z \) where \( X \) is part of a composite key. |

---

## Advantages of Functional Dependencies

| Advantage                        | Description                                                             |
|----------------------------------|-------------------------------------------------------------------------|
| **Data Normalization**           | Helps organize data to minimize redundancy and enhance integrity.       |
| **Query Optimization**           | Aids in determining table connectivity and necessary attributes for queries. |
| **Consistency of Data**          | Maintains data consistency by preventing redundancy and inconsistencies.  |
| **Data Quality Improvement**      | Ensures data accuracy and completeness, reducing errors in analysis.     |


![image](https://github.com/user-attachments/assets/4d1968ff-aced-4b9a-a5d8-7d2bfd7bf1b5)

---

# Second Normal Form (2NF)
![image](https://github.com/user-attachments/assets/2e12e680-56c0-4002-932a-928152d7791d)

## Definition
The **Second Normal Form (2NF)** is a database normalization level that addresses the concept of fully functional dependency. A relation is in 2NF if:
- It is already in **First Normal Form (1NF)**.
- It does not contain any **partial dependency**.

### Key Concepts
- **Composite Key**: A primary key that consists of two or more attributes.
- **Non-prime Attribute**: An attribute that is not part of any candidate key.
- **Partial Dependency**: A non-prime attribute that depends on a proper subset of a candidate key.

---

## Conditions for 2NF
To be in 2NF:
- It is already in **First Normal Form (1NF)**.
- Every non-prime attribute must be fully functionally dependent on candidate key
- There should be no partial dependencies.

### Example 1: Table Normalization

**Original Table**

| STUD_NO | COURSE_NO | COURSE_FEE |
|---------|-----------|------------|
| 1       | C1        | 1000       |
| 2       | C2        | 1500       |
| 1       | C4        | 2000       |
| 4       | C3        | 1000       |
| 4       | C1        | 1000       |
| 2       | C5        | 2000       |

- **Candidate Key**: {STUD_NO, COURSE_NO}
- **Partial Dependency**: COURSE_FEE is dependent on COURSE_NO (which is a proper subset of the candidate key).

**Normalized Tables**

1. **Table 1: STUDENT_COURSE**

| STUD_NO | COURSE_NO |
|---------|-----------|
| 1       | C1        |
| 2       | C2        |
| 1       | C4        |
| 4       | C3        |
| 4       | C1        |
| 2       | C5        |

2. **Table 2: COURSE_FEE**

| COURSE_NO | COURSE_FEE |
|-----------|------------|
| C1        | 1000       |
| C2        | 1500       |
| C3        | 1000       |
| C4        | 2000       |
| C5        | 2000       |

- This normalization reduces redundancy, ensuring COURSE_FEE is only stored once per course.

---

### Example 2: Relation R(A, B, C, D)

**Functional Dependencies**

- \( AB \→ C \) (A and B together determine C)
- \( BC \→ D \) (B and C together determine D)

**Candidate Key**: {AB}

- **Check for Partial Dependencies**: 
  - C depends on the whole key (AB).
  - D depends on the whole key (BC).
  
Since there are no partial dependencies, this relation is already in **3NF**.

---

## Summary of Partial Dependency
- **Definition**: Occurs when a non-prime attribute is dependent only on part of a composite key.
- **Issue**: Leads to data redundancy and anomalies in updates.

To eliminate partial dependencies, relations should be normalized to 2NF, ensuring all non-prime attributes are fully determined by the entire key.


>![Note]
>LHS should be proper subset of ck and rhs shhould be a non prime attribute : partial dependency


![image](https://github.com/user-attachments/assets/5d89d759-ba5c-4faa-b8b1-1883ff470185)

---

# Third Normal Form (3NF)

## Definition
A relation is in **Third Normal Form (3NF)** if:
1. It is in **Second Normal Form (2NF)**.
2. There are no **transitive dependencies**.

### Key Concepts
- **Transitive Dependency**: Occurs when a non-prime attribute is determined by another non-prime attribute. In simpler terms, if you have a non-prime attribute \( B \) that determines another non-prime attribute \( C \), then you have a transitive dependency \( A \&rarr; B \&rarr; C \).

---

## Example: Understanding Transitive Dependency

### Table Structure

| roll_no | state | city    |
|---------|-------|---------|
| 1       | CA    | Los Angeles |
| 2       | NY    | New York    |
| 3       | CA    | San Francisco |
| 4       | TX    | Houston     |

### Functional Dependencies

- **Functional Dependency**: 
  - \( roll\_no &rarr; state \)
  - \( state &rarr; city \)

### Explanation
- **Primary Key (PK)**: `roll_no`
- **Non-Prime Attributes (NPA)**: `state`, `city`

In this example:
- The primary key `roll_no` determines `state`.
- However, `state` also determines `city`. This creates a transitive dependency because `roll_no` indirectly determines `city` through `state`.

---

## Issues with Transitive Dependency
Transitive dependencies can lead to:
- Data redundancy
- Update anomalies (inconsistencies in data when updates are made)

### Diagram Representation

![Transitive Dependency Diagram](https://github.com/user-attachments/assets/9db88e12-7283-49f5-90c0-098efd2bb456)

---

## Conversion to 3NF

To convert a relation to 3NF, we eliminate transitive dependencies by creating separate tables.

### Normalized Tables

1. **Table 1: Roll Number and State**

| roll_no | state |
|---------|-------|
| 1       | CA    |
| 2       | NY    |
| 3       | CA    |
| 4       | TX    |

2. **Table 2: State and City**

| state | city         |
|-------|--------------|
| CA    | Los Angeles  |
| NY    | New York     |
| CA    | San Francisco |
| TX    | Houston      |

### Functional Dependencies After Normalization
- For **Table 1**: \( roll\_no &rarr; state \)
- For **Table 2**: \( state &rarr; city \)

By structuring the data this way, we eliminate the transitive dependency and maintain a clear and efficient database schema.


>![NOTE]
>The left-hand side (LHS) of all functional dependencies must be a **candidate key** (CK) or a **super key** (SK), and the right-hand side (RHS) must be a prime attribute (part of any candidate key).

---
# Boyce-Codd Normal Form (BCNF)

## Definition
BCNF is a normalization form that ensures a relation is free from redundancy caused by functional dependencies. It is stricter than the Third Normal Form (3NF).

## Rules for BCNF
1. **Must be in 3NF**: The relation must already be in Third Normal Form.
2. **Superkey Requirement**: For every functional dependency \( X \rightarrow Y \), \( X \) must be a superkey.

### Note
To test for BCNF, identify all determinants and ensure they are candidate keys.

---

## Hierarchy of Normal Forms
- **1NF**: Requires atomic values in tuples.
- **2NF**: Builds on 1NF by removing partial dependencies.
- **3NF**: Further restricts by removing transitive dependencies.
- **BCNF**: Every determinant must be a superkey.

*All relations in BCNF are also in 3NF, but not all 3NF relations are in BCNF.*

---

## Example
### Given Relation
| Stu_ID | Stu_Branch                           | Stu_Course          | Branch_Number | Stu_Course_No |
|--------|--------------------------------------|---------------------|---------------|----------------|
| 101    | Computer Science & Engineering       | DBMS                | B_001         | 201            |
| 101    | Computer Science & Engineering       | Computer Networks    | B_001         | 202            |
| 102    | Electronics & Communication Engineering | VLSI Technology     | B_003         | 401            |
| 102    | Electronics & Communication Engineering | Mobile Communication | B_003         | 402            |

### Functional Dependencies
Stu_ID −> Stu_Branch
Stu_Course −> {Branch_Number, Stu_Course_No}

### Candidate Keys
- {Stu_ID, Stu_Course}

### Why This Table is Not in BCNF
The table is not in BCNF because:
- Neither **Stu_ID** nor **Stu_Course** is a superkey for the functional dependency \( \text{Stu_Course} \rightarrow \{ \text{Branch_Number}, \text{Stu_Course_No} \} \).

---

## How to Achieve BCNF
To satisfy BCNF, decompose the relation into multiple tables:

1. **Stu_Branch Table**
   | Stu_ID | Stu_Branch                           |
   |--------|--------------------------------------|
   | 101    | Computer Science & Engineering       |
   | 102    | Electronics & Communication Engineering |

   - **Candidate Key**: Stu_ID

2. **Stu_Course Table**
   | Stu_Course          | Branch_Number | Stu_Course_No |
   |---------------------|---------------|----------------|
   | DBMS                | B_001         | 201            |
   | Computer Networks    | B_001         | 202            |
   | VLSI Technology     | B_003         | 401            |
   | Mobile Communication | B_003         | 402            |

   - **Candidate Key**: Stu_Course

3. **Stu_ID to Stu_Course_No Table**
   | Stu_ID | Stu_Course_No |
   |--------|----------------|
   | 101    | 201            |
   | 101    | 202            |
   | 102    | 401            |
   | 102    | 402            |

   - **Candidate Key**: {Stu_ID, Stu_Course_No}

---

After decomposition, the relations satisfy BCNF conditions, as all determinants are superkeys.


# Difference Between Lossless and Lossy Join Decomposition

## Key Concepts
- **Decomposition**: Breaking a relation into smaller sub-relations to reduce redundancy and anomalies.

## Types of Decomposition
1. **Lossless Join Decomposition**
   - **Definition**: Decomposed relations can be rejoined without losing any information.
   - **Advantages**:
     - Maintains data integrity.
     - Ensures consistency across the database.
     - Facilitates higher normal forms (e.g., 3NF, BCNF).
   - **Disadvantages**:
     - Increased storage usage.
     - Complex queries for rejoining tables.

2. **Lossy Join Decomposition**
   - **Definition**: Some information is lost when relations are decomposed.
   - **Advantages**:
     - Simpler structure with smaller sub-tables.
     - Reduced redundancy may be acceptable in some cases.
   - **Disadvantages**:
     - Permanent loss of data.
     - Leads to inconsistencies in the database.
     - Harder to manage data consistency.

## Key Differences
| Feature                       | Lossless Join                          | Lossy Join                           |
|-------------------------------|----------------------------------------|--------------------------------------|
| **Reconstruction**            | Original relation can be perfectly reconstructed. | Some data is permanently lost.     |
| **Join Result**               | R1 ⨝ R2 ⨝ R3 .... ⨝ Rn = R   | R ⊂ R1 ⨝ R2 ⨝ R3 .... ⨝ Rn |
| **Attribute Relation**        | Common attribute is a superkey.       | Common attribute is not a superkey. |
| **Information Loss**          | No loss of information.                | Information loss leads to inconsistencies. |

## Conclusion
- **Lossless Join Decomposition** is preferred for data integrity and accuracy.
- **Lossy Join Decomposition** may be acceptable for reducing redundancy when some data loss is tolerable.


Here’s an improved version of the content with more detailed examples and easy-to-understand explanations using Markdown:

# Joins in SQL

A **Join** allows you to combine rows from two or more tables based on a related column between them.

- **Basic Join Concept**: Join = (Cross Product + Condition).
- **Key Requirement**: To perform a join, you need a common column between two tables.

## Types of Joins

1. **Natural Join**
2. **Self Join**
3. **Equijoin**
4. **Conditional**
5. **Outer Join**
     - Left
     - Right
     - Full
   
![image](https://github.com/user-attachments/assets/48a21120-7f0a-4f1b-b476-03063cfe8669)

---

## 1. Natural Join

### Definition:
A **Natural Join** automatically joins two tables based on columns with the same name and data type in both tables.

### Example:
We want to find the names of employees (`ename`) who are working in a specific department (`dept`). The two tables, `emp` and `dept`, share a common column `eno` (employee number).

```sql
-- Using explicit condition
SELECT ename 
FROM emp, dept 
WHERE emp.eno = dept.eno;

-- Using NATURAL JOIN (automatically uses the common column 'eno')
SELECT ename 
FROM emp 
NATURAL JOIN dept;
```

### Diagram:

![Natural Join Example](https://github.com/user-attachments/assets/c8474f66-de30-4dab-a0e6-e135958abe5c)

---

## 2. Self Join

### Definition:
A **Self Join** is when a table is joined with itself. This is useful when you want to compare rows within the same table.

### Example:
Find the student IDs (`sid`) of students who are enrolled in at least two different courses. Here, we compare the `study` table with itself, ensuring that the course IDs (`cid`) are different.

```sql
-- Self join with alias to compare rows in the same table
SELECT t1.sid 
FROM study AS t1, study AS t2
WHERE t1.sid = t2.sid 
AND t1.cid != t2.cid;
```

### Diagram:

![Self Join Example](https://github.com/user-attachments/assets/8e747b85-36e1-406a-8d29-71df000c1d67)

---

## 3. Equijoin

### Definition:
An **Equijoin** uses the equality (`=`) operator to match rows between tables. It joins tables based on a condition that compares columns with equal values.

### Example:
Find the employee names (`ename`) of employees who work in a department with the same location (`location`) as their address (`address`). Here, we are joining the `emp` and `dept` tables using the `location` and `address` fields.

```sql
-- Equijoin using equality condition
SELECT ename 
FROM emp, dept
WHERE emp.location = dept.address;
```

### Diagram:

![Equijoin Example](https://github.com/user-attachments/assets/29e3af65-e5e5-4e7c-b038-9f590402a519)

---

## Key Takeaways

- **Natural Join**: Automatically joins using common columns.
- **Self Join**: Joins a table with itself to compare rows within it.
- **Equijoin**: Joins based on equality between columns of two tables.


---

## 1. Inner Join
An **Inner Join** returns rows where there is a match in both tables. If there are no matches, no rows are returned.

### SQL Query:
```sql
SELECT StudentCourse.COURSE_ID, Student.NAME, Student.AGE 
FROM Student
INNER JOIN StudentCourse
ON Student.ROLL_NO = StudentCourse.ROLL_NO;
```

![image](https://github.com/user-attachments/assets/edb94326-b42b-4784-9bb0-d98d2ed56869)


### Explanation:
- We select course IDs from the `StudentCourse` table and the names and ages from the `Student` table.
- The rows are matched based on `ROLL_NO`.

### Output:
| COURSE_ID | NAME  | AGE |
|-----------|-------|-----|
| CS101     | Aryan | 20  |
| CS102     | Sara  | 21  |
| CS103     | John  | 22  |

---

## 2. Left Outer Join
A **Left Outer Join** returns all rows from the left table and the matched rows from the right table. If there is no match, NULL values are returned from the right table.

### SQL Query:
```sql
SELECT emp_no, e_name, d_name, loc  
FROM emp 
LEFT OUTER JOIN dept 
ON emp.dept_no = dept.dept_no;
```

![image](https://github.com/user-attachments/assets/13607218-c979-4c8d-a3eb-cbd05c9e26c0)

### Explanation:
- This query fetches employee details (`emp_no`, `e_name`) and department details (`d_name`, `loc`).
- All employees are shown, even if they don't belong to a department.

### Output:
| emp_no | e_name | d_name    | loc        |
|--------|--------|-----------|------------|
| 1001   | Aryan  | Sales     | Mumbai     |
| 1002   | Sara   | NULL      | NULL       |
| 1003   | John   | Marketing | Bangalore  |

> **NOTE:** Employees like `Sara` don't belong to any department, so department columns return `NULL`.

### Another Example:
```sql
SELECT Student.NAME, StudentCourse.COURSE_ID 
FROM Student
LEFT JOIN StudentCourse 
ON StudentCourse.ROLL_NO = Student.ROLL_NO;
```

---

## 3. Right Outer Join
A **Right Outer Join** returns all rows from the right table, and the matched rows from the left table. If there is no match, NULL values are returned from the left table.

### SQL Query:
```sql
SELECT emp_no, e_name, d_name, loc 
FROM emp 
RIGHT OUTER JOIN dept 
ON emp.dept_no = dept.dept_no;
```

![image](https://github.com/user-attachments/assets/8c67677f-bddf-4f10-a18c-24f0dd92ed20)


### Explanation:
- This query fetches department details and any employees that belong to them.
- All departments are shown, even if they don't have any employees.

### Output:
| emp_no | e_name | d_name    | loc        |
|--------|--------|-----------|------------|
| 1001   | Aryan  | Sales     | Mumbai     |
| NULL   | NULL   | Marketing | Bangalore  |

> **NOTE:** The `Marketing` department has no employees, so employee columns return `NULL`.

### Another Example:
```sql
SELECT Student.NAME, StudentCourse.COURSE_ID 
FROM Student
RIGHT JOIN StudentCourse 
ON StudentCourse.ROLL_NO = Student.ROLL_NO;
```

---

## 4. Full Outer Join
A **Full Outer Join** returns all rows when there is a match in either left or right table. If there is no match, NULL values are returned for non-matching rows in either table.

> **IMPORTANT**: 
> LEFT OUTER JOIN + RIGHT OUTER JOIN = FULL OUTER JOIN

--- 

### Visual Explanation of Joins

- **Inner Join**: Shows only matching rows.
- **Left Outer Join**: Shows all rows from the left, and matching from the right.
- **Right Outer Join**: Shows all rows from the right, and matching from the left.
- **Full Outer Join**: Combines left and right joins.

![image](https://github.com/user-attachments/assets/0267f36e-e028-4951-940d-00f584fe6958)

--- 

# SQL: Structured Query Language

**SQL** (Structured Query Language) is a standard language for managing and manipulating relational databases. It's a **declarative language**, meaning you specify *what* you want to do, and the SQL engine handles *how* it's done.

---

## Types of SQL Commands

SQL commands are categorized into different types based on their functionality. Here's a breakdown:

| **Category**                | **Description**                                                |
|-----------------------------|----------------------------------------------------------------|
| **Data Definition Language** (DDL) | Defines the structure of the database (schema) and the tables.  |
| **Data Manipulation Language** (DML) | Manipulates data stored in the database.                   |
| **Data Control Language** (DCL) | Controls access to the data within the database.              |
| **Transaction Control Language** (TCL) | Manages transactions within the database.                  |
| **Constraints**              | Ensures data integrity by defining rules for the data.         |

---

### 1. **Data Definition Language (DDL)**
DDL commands are used to define and manage database schema objects, like tables, views, and indexes.

| **Command** | **Description**                                           |
|-------------|-----------------------------------------------------------|
| `CREATE`    | Creates a new table, view, or database.                   |
| `ALTER`     | Modifies the structure of an existing table.              |
| `DROP`      | Deletes an existing table or database.                    |
| `TRUNCATE`  | Removes all rows from a table without logging individual row deletions. |
| `RENAME`    | Renames an existing object like a table or column.        |

**Example:**

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT
);

ALTER TABLE Students ADD Email VARCHAR(100);

DROP TABLE Students;
```

---

### 2. **Data Manipulation Language (DML)**
DML commands are used to modify data within tables.

| **Command**  | **Description**                                           |
|--------------|-----------------------------------------------------------|
| `SELECT`     | Retrieves data from one or more tables.                   |
| `INSERT`     | Inserts new data into a table.                            |
| `UPDATE`     | Modifies existing data in a table.                        |
| `DELETE`     | Removes data from a table.                                |

**Example:**

```sql
INSERT INTO Students (StudentID, Name, Age) 
VALUES (1, 'Aryan', 20);

SELECT * FROM Students;

UPDATE Students 
SET Age = 21 
WHERE StudentID = 1;

DELETE FROM Students 
WHERE StudentID = 1;
```

---

### 3. **Data Control Language (DCL)**
DCL commands are used to control access to data stored in a database.

| **Command** | **Description**                               |
|-------------|-----------------------------------------------|
| `GRANT`     | Gives users permission to perform operations. |
| `REVOKE`    | Removes previously granted permissions.       |

**Example:**

```sql
GRANT SELECT, INSERT ON Students TO 'admin';

REVOKE INSERT ON Students FROM 'admin';
```

---

### 4. **Transaction Control Language (TCL)**
TCL commands are used to manage transactions within a database, ensuring data consistency.

| **Command**   | **Description**                                     |
|---------------|-----------------------------------------------------|
| `COMMIT`      | Saves all changes made during the current transaction. |
| `ROLLBACK`    | Undoes all changes made during the current transaction. |
| `SAVEPOINT`   | Sets a savepoint within a transaction to roll back to. |

**Example:**

```sql
BEGIN TRANSACTION;

UPDATE Students SET Age = 22 WHERE StudentID = 1;

SAVEPOINT AgeUpdate;

ROLLBACK TO AgeUpdate;

COMMIT;
```

---

### 5. **Constraints**
Constraints enforce rules to maintain data integrity within a database. These rules are applied when creating or altering tables.

| **Constraint**   | **Description**                                         |
|------------------|---------------------------------------------------------|
| `PRIMARY KEY`    | Uniquely identifies each record in a table.             |
| `FOREIGN KEY`    | Links records between two tables, enforcing referential integrity. |
| `CHECK`          | Ensures that all values in a column satisfy a specific condition. |
| `UNIQUE`         | Ensures all values in a column are distinct.            |
| `NOT NULL`       | Ensures that a column cannot have NULL values.          |
| `DEFAULT`        | Provides a default value for a column if none is specified. |

**Example:**

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT CHECK (Quantity > 0),
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    OrderDate DATE DEFAULT GETDATE(),
    UNIQUE (ProductID)
);
```

---

## Key Takeaways:

1. **DDL**: Defines and manages tables and schema.
2. **DML**: Manipulates data within tables (insert, update, delete).
3. **DCL**: Grants or revokes user access to data.
4. **TCL**: Manages database transactions for data consistency.
5. **Constraints**: Enforce rules to maintain valid and consistent data.

SQL makes it easy to define, manipulate, and control access to data while ensuring the integrity of information through constraints.

---

# SQL `CREATE TABLE` Command

The **`CREATE TABLE`** command is used to create a new table in SQL with specified columns and constraints.

---

## Key Points:
- Defines table structure (columns and data types).
- Constraints like `PRIMARY KEY`, `NOT NULL`, `CHECK`, etc., can be added.
- Use `CREATE TABLE IF NOT EXISTS` to avoid errors when the table already exists.

---

## Example: Create `Customer` Table with Constraints

```sql
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    LastName VARCHAR(50),
    Country VARCHAR(50),
    Age INT CHECK (Age BETWEEN 0 AND 99),
    Phone INT(10)
);
```

---

## Insert Data:

```sql
INSERT INTO Customer (CustomerID, CustomerName, LastName, Country, Age, Phone)
VALUES 
    (1, 'Shubham', 'Thakur', 'India', 23, 'xxxxxxxxxx'),
    (2, 'Aman', 'Chopra', 'Australia', 21, 'xxxxxxxxxx');
```

---

## Create Table from Another Table:

```sql
CREATE TABLE SubTable AS
SELECT CustomerID, CustomerName
FROM Customer;
```

---

# SQL `ALTER` Command

The **`ALTER`** command in SQL is used to modify an existing table. It can be used to:
- Add or remove columns.
- Modify data types or their lengths.
- Add or remove constraints.
- Rename columns or tables.

---

## Syntax:

```sql
ALTER TABLE table_name
-- ADD, DROP, MODIFY, RENAME commands
```

---

## 1. Add a Column

```sql
ALTER TABLE Employee
ADD Email VARCHAR(100);
```
Adds a new column `Email` to the `Employee` table.

---

## 2. Remove a Column

```sql
ALTER TABLE Employee
DROP COLUMN Email;
```
Removes the `Email` column from the `Employee` table.

---

## 3. Modify Data Type of a Column

```sql
ALTER TABLE Employee
MODIFY Salary DECIMAL(12, 2);
```
Changes the data type and length of the `Salary` column.

---

## 4. Modify Data Type Length

```sql
ALTER TABLE Customer
MODIFY Phone VARCHAR(15);
```
Modifies the length of the `Phone` column to allow more digits.

---

## 5. Add a Constraint

```sql
ALTER TABLE Employee
ADD CONSTRAINT chk_salary CHECK (Salary >= 0);
```
Adds a `CHECK` constraint to ensure `Salary` is not negative.

---

## 6. Remove a Constraint

```sql
ALTER TABLE Employee
DROP CONSTRAINT chk_salary;
```
Removes the `CHECK` constraint from the `Salary` column.

---

## 7. Rename a Column

```sql
ALTER TABLE Employee
RENAME COLUMN FirstName TO First_Name;
```
Renames the column `FirstName` to `First_Name`.

---

## 8. Rename a Table

```sql
ALTER TABLE Employee
RENAME TO Staff;
```
Changes the table name from `Employee` to `Staff`.

---


## `ALTER` vs `UPDATE` in SQL

| **ALTER**                                    | **UPDATE**                               |
|----------------------------------------------|------------------------------------------|
| **DDL (Data Definition Language)**           | **DML (Data Manipulation Language)**     |
| Used to change the **table structure**.      | Used to **modify data** within a table.  |
| Works on the schema/structure of the table.  | Works on the data stored in the table.   |
| Example: Add a column `email`                | Example: Update salary                  |
| Example: Remove a column `name`              | Example: Update `name`                  |
| Example: Modify data type from `INT` to `VARCHAR(50)` | Works on rows or specific columns |
| Example: Rename column or table              | Applies changes to records in the table |

---

### Examples for `ALTER`

1. **Add a column `email`:**

    ```sql
    ALTER TABLE emp
    ADD email VARCHAR(100);
    ```

2. **Remove a column `name`:**

    ```sql
    ALTER TABLE emp
    DROP COLUMN name;
    ```

3. **Modify data type from `INT` to `VARCHAR(50)`:**

    ```sql
    ALTER TABLE emp
    MODIFY id VARCHAR(50);
    ```

4. **Rename a column or table:**

    ```sql
    ALTER TABLE emp
    RENAME COLUMN name TO full_name;
    
    ALTER TABLE emp
    RENAME TO employees;
    ```

---

### Examples for `UPDATE`

1. **Update salary by doubling it:**

    ```sql
    UPDATE emp
    SET salary = salary * 2
    WHERE id = 1;
    ```

2. **Update `name` of an employee:**

    ```sql
    UPDATE emp
    SET name = 'Aryan Kumar'
    WHERE id = 1;
    ```


- **`ALTER`**: Used for modifying the structure of a table (DDL).
- **`UPDATE`**: Used for modifying the data within the table (DML).

---

## `DELETE` vs `DROP` vs `TRUNCATE` in SQL

| **DELETE**                                   | **DROP**                                 | **TRUNCATE**                             |
|----------------------------------------------|------------------------------------------|------------------------------------------|
| **DML (Data Manipulation Language)**         | **DDL (Data Definition Language)**       | **DDL (Data Definition Language)**       |
| Used to delete specific **rows/tuples** from a table using a `WHERE` clause. | Deletes the **entire table**, including its structure (schema). | Deletes all rows from a table, keeping the structure. |
| Preserves the table structure.               | Completely removes table structure and data. | Table structure is preserved.           |
| Slower, as it deletes one row at a time.     | Irreversible and faster for removing an entire table. | Faster than `DELETE`, but irreversible. |
| Can use `WHERE` clause to delete specific rows. | Example: `DROP TABLE Student;`          | Deletes all rows in one go without `WHERE`. |
| **Example:**                                 | **Example:**                             | **Example:**                             |
| ```sql                                       | ```sql                                   | ```sql                                   |
| DELETE FROM student WHERE id = 1;            | DROP TABLE student;                      | TRUNCATE TABLE student;                  |
| ```                                          | ```                                      | ```                                      |
| Supports rollback (transactional).           | Irreversible; cannot roll back.          | No rollback possible. No logging.        |
| Slower than `TRUNCATE` due to logging of each row. | Completely wipes out the table.         | Removes all rows instantly, no individual row logging. |

### Key Differences

- **DELETE**: Removes specific rows from the table using `WHERE`. It logs each row and is slower. You can roll back changes using transactions.
  
- **DROP**: Completely removes the table, including its structure, making it irrecoverable.

- **TRUNCATE**: Deletes all rows instantly but preserves the structure. Faster than `DELETE` but cannot be rolled back.

---

## Constraints in SQL

Constraints are conditions or restrictions applied to data before it's inserted into the database, ensuring data integrity and validity.

### Common Constraints:

1. **UNIQUE**  
   - Ensures all values in a column are **distinct** and no duplicate values are allowed.
   - **Example**: Ensuring each mobile number is unique.
   ```sql
   CREATE TABLE Users (
       UserID INT UNIQUE,
       MobileNumber VARCHAR(15) UNIQUE
   );
   ```

2. **NOT NULL**  
   - Ensures that a column cannot have a **NULL** (empty) value.
   - **Example**: Email ID must be filled out in a form (mandatory).
   ```sql
   CREATE TABLE Users (
       UserID INT,
       Email VARCHAR(100) NOT NULL
   );
   ```

3. **PRIMARY KEY**  
   - A combination of **UNIQUE** and **NOT NULL** constraints. Uniquely identifies each row in a table.
   - **Example**: `UserID` is unique and non-null.
   ```sql
   CREATE TABLE Users (
       UserID INT PRIMARY KEY,
       Email VARCHAR(100)
   );
   ```

4. **CHECK**  
   - Ensures that all values in a column meet a specific condition.
   - **Example**: Age must be greater than 18.
   ```sql
   CREATE TABLE Users (
       UserID INT,
       Age INT CHECK (Age >= 18)
   );
   ```

5. **FOREIGN KEY**  
   - Ensures referential integrity by linking columns to another table's **PRIMARY KEY**.
   - **Example**: `DepartmentID` in `Employee` table refers to the `DepartmentID` in `Departments` table.
   ```sql
   CREATE TABLE Employee (
       EmployeeID INT PRIMARY KEY,
       DepartmentID INT,
       FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
   );
   ```
6. **DEFAULT**

The `DEFAULT` constraint provides a **default value** for a column when no value is specified. If a user doesn't insert a value into that column, the database automatically assigns the default value.

#### Example: Setting a Default Salary

If no salary is provided for an employee, the `DEFAULT` constraint ensures the salary is automatically set to 10,000.

```sql
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT DEFAULT 10000
);
```

In this case, if you insert a new employee without specifying the salary, it will be set to 10,000 by default.

#### Insert Example:
```sql
INSERT INTO Employee (EmployeeID, FirstName, LastName)
VALUES (1, 'Aryan', 'Kyatham');
```

#### Result:
The inserted employee will have a salary of **10,000**, as defined by the `DEFAULT` constraint:
| EmployeeID | FirstName | LastName | Salary |
|------------|-----------|----------|--------|
| 1          | Aryan     | Kyatham  | 10000  |

This way, the `DEFAULT` constraint ensures that missing values are handled with predefined values!  

### Real-World Example:

When creating a Gmail account:
- The **UNIQUE** constraint ensures the email ID `kyathamaryan@gmail.com` isn't already taken.
- The **NOT NULL** constraint makes it mandatory to fill out fields like email and mobile number.

These constraints help maintain clean, valid, and organized data in your database!


---


| **e_id** | **ename** | **dept** | **salary** |
|----------|-----------|----------|------------|
| 1        | Ram       | HR       | 10,000     |
| 2        | Amrit     | MRKT     | 20,000     |
| 3        | Ravi      | HR       | 30,000     |
| 4        | Nitin     | MRKT     | 40,000     |
| 5        | Varun     | IT       | 50,000     |

## SQL Queries

### 1. Display Maximum Salary from `emp` Table
To find the maximum salary from the `emp` table, use the following query:

```sql
SELECT MAX(salary) FROM emp;
```

### 2. Display Employee Name with Maximum Salary
To get the name of the employee earning the maximum salary:

```sql
SELECT ename FROM emp
WHERE salary = (SELECT MAX(salary) FROM emp);
```

### 3. Display Second Highest Salary from `emp` Table
To find the second highest salary:

```sql
SELECT MAX(salary) FROM emp 
WHERE salary != (SELECT MAX(salary) FROM emp);
```

### 4. Display Employee Name with Second Highest Salary
To get the name of the employee earning the second highest salary:

```sql
SELECT ename FROM emp
WHERE salary = (SELECT MAX(salary) FROM emp 
                WHERE salary != (SELECT MAX(salary) FROM emp));
```

> **Note:**  
> Using `=` in conditions such as `2 = 2` is straightforward, but when checking multiple values, use the `IN` keyword for better clarity and efficiency.  
> For example, instead of checking multiple values with `=`:

```sql
SELECT * FROM emp WHERE dept IN ('HR', 'MRKT');
```

### 5. Display Department Names with Number of Employees
To get a count of employees working in each department:

```sql
SELECT dept, COUNT(dept) 
FROM emp 
GROUP BY dept;
```

#### Output:
| **dept** | **count** |
|----------|-----------|
| HR       | 2         |
| MRKT     | 2         |
| IT       | 1         |

### Important Notes on `GROUP BY`
- When using `GROUP BY`, you can only select columns that are either grouped or aggregated. For example:

```sql
SELECT dept FROM emp GROUP BY dept;
```
- In this case, only the `dept` column is allowed without any other attributes.


---

### 6. Display all Departments where the Number of Employees is Less than 2

This query finds departments with fewer than 2 employees.

```sql
SELECT dept
FROM emp
GROUP BY dept
HAVING COUNT(dept) < 2;
```

#### Explanation:
- `GROUP BY dept`: Groups employees by their department.
- `HAVING COUNT(dept) < 2`: Only includes departments where the number of employees is less than 2.

#### Expected Output:
| dept  |
|-------|
| Sales |
| IT    |

---

### 6.1. Display the Names of Employees in Departments with Fewer than 2 Employees

This query returns the names of employees who work in departments where the number of employees is less than 2.

```sql
SELECT ename 
FROM emp 
WHERE dept IN (
    SELECT dept
    FROM emp
    GROUP BY dept
    HAVING COUNT(dept) < 2
);
```

#### Explanation:
- The inner query selects departments with fewer than 2 employees.
- The outer query finds the names (`ename`) of employees in those departments.

#### Expected Output:
| ename  |
|--------|
| John   |
| Alice  |

---

### 7. Display the Employee with the Highest Salary per Department

This query shows the names of employees who are earning the highest salary in each department.

```sql
SELECT ename 
FROM emp 
WHERE salary IN (
    SELECT MAX(salary) 
    FROM emp
    GROUP BY dept
);
```

#### Explanation:
- The inner query finds the maximum salary in each department.
- The outer query finds the employees whose salary matches the maximum for their department.

#### Expected Output:
| ename  |
|--------|
| Ravi   |
| Nitin  |
| Varun  |

---

### IN / NOT IN Example

This query finds the details of employees whose address is either 'Delhi', 'Chandigarh', or 'Pune'.

```sql
SELECT * 
FROM emp 
WHERE address IN ('DELHI', 'CHANDIGARH', 'PUNE');
```

#### Explanation:
- `IN` is used to check whether a value exists within a given set of values.

#### Expected Output:
| eid | ename  | address     |
|-----|--------|-------------|
| 1   | Ravi   | Chandigarh  |
| 2   | Varun  | Delhi       |
| 3   | Nitin  | Pune        |

---

### Find Employees Who Are Working on a Project

This query retrieves the names of employees who are working on a project.

```sql
SELECT ename 
FROM emp 
WHERE eid IN (
    SELECT DISTINCT eid 
    FROM project
);
```

#### Explanation:
- The inner query selects the unique employee IDs (`eid`) from the `project` table.
- The outer query returns the names of those employees from the `emp` table.

#### Expected Output:
| ename  |
|--------|
| Ravi   |
| Ammy   |
| Nitin  |

---

### Nested Query Explanation

- **Nested Queries**: Queries inside another query.
- **Bottom-Up Execution**: The innermost query runs first, and its result is used by the outer query.

For example, in the query:

```sql
SELECT ename 
FROM emp 
WHERE eid IN (
    SELECT DISTINCT eid 
    FROM project
);
```

- The inner query (`SELECT DISTINCT eid FROM project`) runs first to get the employee IDs.
- The outer query (`SELECT ename FROM emp WHERE eid IN (...)`) uses these IDs to find the employee names.

---


### EXISTS and NOT EXISTS in SQL

- **EXISTS**: This operator is used in a **correlated** subquery to check if rows are returned by the inner query.
- **NOT EXISTS**: This is the opposite, checking if no rows are returned by the inner query.

These operators return **TRUE** or **FALSE** based on whether the subquery finds matching records.

#### Example: Find Employees Who Are Working on at Least One Project

```sql
SELECT * 
FROM emp 
WHERE EXISTS (
    SELECT eid 
    FROM project 
    WHERE emp.eid = project.eid
);
```

#### Explanation:
- **Correlated Query**: The subquery depends on the outer query because it uses `emp.eid`.
- The subquery checks for the existence of the employee (`emp.eid`) in the `project` table.
- If a matching `eid` is found, the outer query returns the employee's details.

#### Expected Output:

| eid | ename  | dept   | salary |
|-----|--------|--------|--------|
| 1   | Aryan  | Backend| 75000  |
| 3   | Nitin  | Android| 85000  |

---

### Aggregate Functions in SQL

SQL offers several aggregate functions to perform calculations on data sets. These include:

- **MAX**: Returns the highest value.
- **MIN**: Returns the lowest value.
- **COUNT**: Returns the number of rows (or non-null values in a column).
- **SUM**: Returns the total sum of a numeric column.
- **AVG**: Returns the average of a numeric column.

#### Example: Find Maximum Salary in the Employee Table

```sql
SELECT MAX(salary) FROM emp;
```

#### Expected Output:
| max(salary) |
|-------------|
| 75000       |

#### Other Examples:

- **MIN**: `SELECT MIN(salary) FROM emp;`
- **COUNT (All Rows)**: `SELECT COUNT(*) FROM emp;`
- **COUNT (Non-Null Salaries)**: `SELECT COUNT(salary) FROM emp;`
- **SUM**: `SELECT SUM(salary) FROM emp;`
- **AVG**: `SELECT AVG(salary) FROM emp;`

---

### Correlated Query in SQL

- A **correlated query** is a **subquery** that uses values from the outer query.
- It’s evaluated for each row processed by the outer query, making it a **top-down approach**.

#### Example: Find All Employee Details Who Work in a Department

```sql
SELECT * 
FROM emp 
WHERE EXISTS (
    SELECT * 
    FROM dept 
    WHERE dept.eid = emp.eid
);
```

#### Explanation:
- The subquery is correlated with the outer query using the condition `dept.eid = emp.eid`.
- For each employee in the outer query, the subquery checks whether a matching `eid` exists in the `dept` table.

#### Expected Output:

| eid | ename  | dept    | salary |
|-----|--------|---------|--------|
| 1   | Aryan  | Backend | 75000  |
| 2   | Sandy  | Testing | NULL   |

---

### Nested Queries vs Correlated Queries vs Joins

Let’s compare **nested queries**, **correlated queries**, and **joins** based on their execution patterns.

| Query Type         | Execution Pattern          | Description                              |
|--------------------|----------------------------|------------------------------------------|
| **Nested Query**    | **Bottom-Up**              | The inner query is executed first, and its result is used by the outer query. |
| **Correlated Query**| **Top-Down**               | The inner query is dependent on values from the outer query and is re-executed for each row of the outer query. |
| **Join**            | **Single Execution (Cross Product + Condition)** | Combines data from two or more tables based on a related column. Generally more efficient than correlated queries. |

#### Example: Nested Query

This query returns the details of all employees who work in any department.

```sql
SELECT * 
FROM emp 
WHERE eid IN (
    SELECT eid 
    FROM dept
);
```

- **Inner Query**: Selects all `eid` from the `dept` table.
- **Outer Query**: Fetches all employees (`emp`) whose `eid` matches the `eid` from the inner query.

#### Expected Output:

| eid | ename  | dept    | salary |
|-----|--------|---------|--------|
| 1   | Aryan  | Backend | 75000  |
| 2   | Sandy  | Testing | NULL   |

---

#### Example: Correlated Query

This query returns details of employees who work in a department, checking row by row.

```sql
SELECT * 
FROM emp 
WHERE EXISTS (
    SELECT 1 
    FROM dept 
    WHERE dept.eid = emp.eid
);
```

- **Inner Query**: Checks for the existence of `eid` in the `dept` table for each `eid` from the outer query.

#### Expected Output:

| eid | ename  | dept    | salary |
|-----|--------|---------|--------|
| 1   | Aryan  | Backend | 75000  |

---

#### Example: Join

This query returns employee details along with department information using a join.

```sql
SELECT emp.*, dept.name 
FROM emp 
JOIN dept 
ON emp.eid = dept.eid;
```

- **Join**: Combines data from `emp` and `dept` tables where `eid` matches.

#### Expected Output:

| eid | ename  | dept    | salary | dept_name  |
|-----|--------|---------|--------|------------|
| 1   | Aryan  | Backend | 75000  | IT         |

---

### Nested vs Correlated Query vs Join: Performance Comparison

- **Nested Queries**: Process the **inner query first** and then apply the outer query. Suitable for simple data extraction.
  
- **Correlated Queries**: Execute the **inner query for each row** in the outer query. This can be less efficient due to repeated executions, but useful for more complex filtering.

- **Joins**: Process both tables at the same time using a **cross-product and condition**. This is generally faster and more efficient than correlated queries, though it can consume more space.

For example, in a correlated query, for 5 employees and 3 departments, there would be **5 × 3** executions, while in a join, a temporary buffer holds the results, making the query more efficient overall.

---
### Finding the Nth Highest Salary Using SQL

To find the **Nth highest salary** in a table, you can use a correlated subquery that counts distinct salaries greater than the salary in each row. Here's a breakdown of how it works:

```sql
SELECT id, salary 
FROM emp e1
WHERE N - 1 = (
    SELECT COUNT(DISTINCT salary) 
    FROM emp e2 
    WHERE e2.salary > e1.salary
);
```

#### Explanation:
- `e1` is the outer query, representing each employee's salary.
- `e2` is the inner query, counting how many distinct salaries are **greater** than `e1.salary`.
- The condition `N - 1` ensures that we're selecting the row where exactly **N - 1** distinct salaries are greater than the current salary.

#### Example:

| id | salary |
|----|--------|
| 1  | 10000  |
| 2  | 20000  |
| 3  | 20000  |
| 4  | 30000  |
| 5  | 40000  |

To find the **2nd highest salary** (`N = 2`):

```sql
SELECT id, salary 
FROM emp e1
WHERE 2 - 1 = (
    SELECT COUNT(DISTINCT salary) 
    FROM emp e2 
    WHERE e2.salary > e1.salary
);
```

#### Output:

| id | salary |
|----|--------|
| 4  | 30000  |

---

### Alternative Approach to Finding the 2nd Highest Salary

You can also use this query to find the **2nd highest salary** by excluding the highest salary:

```sql
SELECT MAX(salary) 
FROM emp 
WHERE salary NOT IN (
    SELECT MAX(salary) 
    FROM emp
);
```

#### Explanation:
- The subquery finds the **maximum salary**.
- The outer query finds the **maximum salary** excluding the highest one from the subquery.

#### Example Output:

If the salaries are `10000, 20000, 30000, 40000`, the query will return `30000` as the 2nd highest salary.

---

### Query to Find Last Names with 'A' as the Second Character

To find employees whose last names have an 'A' as the **second character**, use the `LIKE` operator with the underscore (`_`) wildcard for a single character:

```sql
SELECT last_name 
FROM emp 
WHERE last_name LIKE '_A%';
```

#### Explanation:
- `_` represents **any single character**.
- `A` is the second character.
- `%` allows for any sequence of characters after the second character.

#### Example:

| last_name |
|-----------|
| Kalpana   |
| Daniel    |

This will return last names where 'A' is the second character.

---

### SQL Command to Remove a Table

To **remove a table** (or relation) from a SQL database, you can use the `DROP TABLE` command:

```sql
DROP TABLE <TABLE_NAME>;
```

#### Example:

```sql
DROP TABLE employees;
```

