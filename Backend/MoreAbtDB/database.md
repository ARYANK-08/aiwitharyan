# Introduction to ORM's

Object-Relational Mapping (ORM) is a technique used to bridge the gap between object-oriented programming and relational databases. ORM allows developers to manipulate database data using an object-oriented paradigm rather than writing SQL queries. It simplifies database interaction by letting you work with classes and objects instead of tables and records.

### What is ORM?

In simple terms, ORM maps objects in your code to database tables. Instead of writing SQL to interact with the database, an ORM library helps automate that process by converting your code objects into relational database operations. 

Let's take an example:

- **Without ORM (SQL):**

    ```sql
    SELECT * FROM books WHERE author = 'Linus';
    ```

    You'd manually fetch rows from the database and populate them into objects in your code.

- **With ORM:**

    ```python
    book_list = Book.objects.filter(author="Linus")
    ```

    The ORM does the heavy lifting for you, automatically converting that command into the appropriate SQL query behind the scenes.

### Example with Django ORM

Let's say you have an `Employee` class and a corresponding `employee` table in the database.

#### Table Schema (SQL):

```sql
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

#### Model (Django ORM):

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
```

#### Query Example

- **SQL:**

    ```sql
    SELECT name FROM employee WHERE id = 1;
    ```

- **ORM (Django):**

    ```python
    employee = Employee.objects.get(id=1)
    print(employee.name)
    ```

This simple ORM query automatically handles the connection to the database, fetching the row and populating the `Employee` object.

### Pros of Using ORM

1. **Reduced Complexity**: ORM abstracts away SQL queries, allowing developers to work with objects instead of tables.
2. **Faster Development**: You write less boilerplate code for CRUD operations (Create, Read, Update, Delete).
3. **Consistency**: Models written in a single place ensure consistency across your application.
4. **Database Independence**: ORMs abstract the database engine, meaning you can switch between databases like MySQL, PostgreSQL, or SQLite without rewriting queries.
5. **Security**: ORM libraries often protect against SQL injection by using prepared statements.

### Cons of Using ORM

1. **Learning Curve**: ORM tools can be complex, and developers need to invest time to learn them.
2. **Performance**: For complex queries, hand-written SQL can be more performant.
3. **Overhead**: ORMs add an extra layer of abstraction, which may result in slower performance for large or highly-optimized queries.
4. **Hidden Complexity**: New developers might write inefficient queries unknowingly, resulting in poor database performance.

### Popular ORM Libraries

- **Java**: Hibernate
- **Python**: Django ORM, SQLAlchemy
- **PHP**: Doctrine, Propel
- **C#**: Entity Framework, NHibernate

### Real-World Use Case

Consider a large e-commerce platform where managing customers, products, orders, and inventory is essential. Without ORM, you'd need to manually write SQL for each interaction with the database. ORM simplifies this process by allowing the developer to create models representing customers, products, and orders. You can then easily perform operations like filtering orders, updating product details, or deleting a customer.

#### Example with Django:

- **Creating a Product**:

    ```python
    product = Product(name="Laptop", price=1000)
    product.save()
    ```

- **Querying for Products under $500**:

    ```python
    cheap_products = Product.objects.filter(price__lt=500)
    ```

These operations are handled seamlessly by the ORM, without the developer needing to write any SQL.

### Conclusion

ORM is a powerful tool that simplifies database interactions by converting code objects into database records and vice versa. While it can save time and reduce complexity for common queries, it’s essential to understand its limitations, especially for performance-critical applications. By learning and effectively using ORM libraries, developers can achieve clean, maintainable, and scalable code.

---

# ACID properties :


ACID properties play a crucial role in maintaining data integrity in databases, especially for applications where incorrect or inconsistent data can have serious consequences. Let’s dive into the concept using simple, real-world examples to make it more understandable.

### Real-World Example of ACID Principles

Imagine you’re managing an online shopping platform like **Amazon**. You allow users to place orders, update their shopping cart, and proceed to payment. Now think about what could go wrong during these processes. Without proper database management, users could get overcharged, undercharged, or even lose their order entirely!

To prevent such errors, databases like **MySQL** and **PostgreSQL** use **ACID** properties. These ensure the integrity and reliability of your transactions. But what are these properties, and how do they work in practice?

### What is a Transaction?

A transaction is like a set of tasks that must be completed together. For example, when a customer places an order on Amazon:
1. The quantity of the item in the cart is updated.
2. The order is added to the orders table.
3. The customer’s credit card is charged.

All these steps need to happen as one *unit* of work—either they all succeed, or none of them do.

Now, let’s break down the **ACID** properties using this example.

### 1. Atomicity: “All or Nothing”
In our Amazon scenario, the **Atomicity** rule ensures that *all* steps of the transaction happen completely or not at all. If there’s a failure in charging the credit card, the entire transaction will roll back. It’s like saying, “If I can’t do everything, I won’t do anything.” This prevents a user from updating the quantity without charging their card, avoiding potential issues where a customer gets items for free.

**Example:** Imagine you’re transferring money between two bank accounts. Atomicity ensures that both the debit and credit happen together. If the debit succeeds but the credit fails, the entire transaction is aborted, and it’s as if nothing happened.

### 2. Consistency: “No Missing Steps”
**Consistency** guarantees that after a transaction, the database moves from one valid state to another, maintaining all rules and constraints. In Amazon’s case, this means the order can’t be placed unless the customer’s balance is enough to cover the cost. If a rule is broken—like trying to charge a card with insufficient funds—the transaction is rolled back, ensuring the data remains consistent.

**Example:** Let’s say the system only allows users over 18 to make purchases. If someone under 18 tries to place an order, the system will reject the transaction, keeping the database consistent.

### 3. Isolation: “Transactions Don’t Interfere”
**Isolation** means that even if multiple transactions are happening at the same time, they won’t mess with each other’s data. Suppose two users are ordering the same product on Amazon. Even though these orders are happening simultaneously, each transaction is handled separately. This prevents issues like one user seeing uncommitted data from the other user’s transaction.

**Example:** Imagine you’re editing a Google Doc with a friend. You don’t want to see half-written words from your friend’s side while they’re still typing. Similarly, databases prevent partial changes from showing to other transactions.

- **Dirty Reads:** If one user updates their cart but hasn’t completed the transaction, another user should not be able to see that half-completed data.
  
- **Non-Repeatable Reads:** Let’s say one user is reading their cart’s total cost, but during that transaction, the price changes due to a discount. If the user checks the total cost again, the result will differ—this inconsistency is a non-repeatable read.

- **Phantom Reads:** If new products are added while a user is reviewing their cart, their next look at the cart might include those new products, causing inconsistency in reads.

### 4. Durability: “Saved for Good”
Once a transaction is complete and committed, **Durability** ensures the data is saved permanently, even if the system crashes. So, if Amazon confirms that the order is placed and the card is charged, this data will remain intact, regardless of server failures or power outages.

**Example:** Imagine you’re writing an email and hit “Send.” Even if your laptop crashes immediately afterward, the email will still be sent because the transaction (sending the email) has been completed and saved on the email server.

### Avoiding Transactional Errors with ACID

ACID helps prevent several common transactional errors, including:
- **Dirty Reads:** Uncommitted data being accessed by other transactions.
- **Non-Repeatable Reads:** Different results from two reads within the same transaction.
- **Phantom Reads:** New data added during an ongoing transaction, causing discrepancies.

ACID properties ensure that databases maintain accuracy and consistency during multiple operations and concurrent transactions.

### ACID vs. BASE in NoSQL Systems
While ACID is critical for **relational databases** like MySQL or PostgreSQL, **NoSQL** systems (like **MongoDB**) often follow a different standard called **BASE**:
- **Basic Availability:** The system is available most of the time, but might have delays.
- **Soft State:** Data may not be immediately consistent across the system.
- **Eventual Consistency:** Over time, the data will become consistent.

NoSQL systems, which prioritize **scalability** over perfect consistency, may not always follow ACID principles. They’re used for applications where availability is more important than strict data integrity, such as large-scale web apps.

---

In conclusion, **ACID** properties help ensure that your transactions either succeed completely or fail without causing any damage to your data. Whether you’re processing orders at Amazon or transferring money between bank accounts, ACID keeps your data safe and sound!

---

# CAP Theorem :

The **CAP theorem** (also known as Brewer’s theorem) is a fundamental concept in distributed systems. It states that in any distributed system, you can only guarantee **two out of three** properties at a given time: **Consistency (C)**, **Availability (A)**, and **Partition Tolerance (P)**. You cannot achieve all three simultaneously.

Here's what each property means:

1. **Consistency (C)**: Every read receives the most recent write. In simpler terms, all nodes in a distributed system have the same data. After an update, if you query any node, you should get the same updated value.

2. **Availability (A)**: Every request gets a response, even if some of the nodes in the system are unavailable. The system should be able to fulfill requests as long as it hasn’t crashed.

3. **Partition Tolerance (P)**: The system continues to operate even if there is a network partition, meaning the communication between nodes is broken.

Let’s break this down with a **real-world example**:

### Example Scenario: Bank Account Withdrawal

- **Servers**: You have two servers (S1 and S2) in a distributed banking system.
- **Client (C)**: A user (client) wants to withdraw money from their bank account.
- **Balance**: The initial balance on both servers is ₹100.

Now, let’s see how CAP theorem applies when the client withdraws ₹10:

---

### **Consistency**

When the client requests to withdraw ₹10, the following happens:

1. **Client (C)** withdraws ₹10 from the balance of ₹100 on **Server S1**.
2. **Server S1** updates the balance to ₹90 and **synchronizes** this change with **Server S2**, which also updates its balance to ₹90.
   
In a **consistent** system, if the client reads the balance from **Server S2**, it will show the same updated balance of ₹90.

However, if the system is **inconsistent**, Server S2 may still show ₹100 after the withdrawal. This violates **consistency** because both servers should have the same balance.

---

### **Availability**

Now, assume **Server S1** handles the withdrawal, but **Server S2** is temporarily down or unreachable. In a system that prioritizes **availability**, the client will still be able to withdraw money from **Server S1**, and the system will respond without waiting for **Server S2** to update. However, this may lead to inconsistency because **Server S2** won’t reflect the withdrawal immediately.

The system prioritizes **availability** over **consistency**.

---

### **Partition Tolerance**

Now imagine there's a **network partition**: the connection between **Server S1** and **Server S2** is broken. In this state, the two servers cannot communicate with each other, but both still accept requests.

In a partitioned system, you can choose to either:
- **Prioritize consistency**: Block all updates until the servers can communicate again.
- **Prioritize availability**: Continue processing transactions on **S1** or **S2**, knowing that the system might become inconsistent.

For example, if the client withdraws ₹10 during this partition and only **S1** processes the withdrawal, **S2** might still show ₹100 until the partition is resolved.

---

### **The Trade-off: CAP in Action**

In distributed systems, you must **choose two** properties at the cost of the third:

- **Consistency + Partition Tolerance (CP)**: The system will maintain consistency across all nodes even if a network partition occurs, but **availability** will be sacrificed. The system may block updates or reads until all nodes can communicate.
  - **Example**: A financial system that blocks transactions during a partition to ensure that no incorrect data is processed.

- **Availability + Partition Tolerance (AP)**: The system will remain available even in the case of a partition, but the data across nodes may be **inconsistent**.
  - **Example**: Social media platforms like Instagram or Twitter prioritize availability, where temporary inconsistencies (like delayed comments or likes) are acceptable as long as the system stays up.

- **Consistency + Availability (CA)**: The system will always return the most recent data, but it won’t handle network partitions well.
  - **Example**: A centralized database system (not distributed) can ensure that all requests are consistent and available but cannot tolerate network failures.

---

### Summary of the CAP Theorem

- **Consistency**: All nodes see the same data at the same time.
- **Availability**: The system responds to all requests, even if some data is outdated.
- **Partition Tolerance**: The system continues to function even if nodes can't communicate with each other.

You **cannot** have all three at the same time in a distributed system. You need to choose between **CA**, **CP**, or **AP**, depending on the needs of your application.



![image](https://github.com/user-attachments/assets/22b27f62-d2e4-4ec0-af66-6b4b129e9229)

![image](https://github.com/user-attachments/assets/72cdefde-dfbf-423b-81d2-748621d62ccb)

---
