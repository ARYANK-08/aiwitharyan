# What is Big Data?

- **Big Data** is defined as high volume, velocity, and variety of information assets that demand cost-effective, innovative forms of information processing for enhanced insights and decision-making.

![image](https://github.com/user-attachments/assets/6a5dc328-b713-4e46-b0b7-e9d6eb89a5c5)

  
- A collection of large datasets that cannot be processed using traditional computing methods.
- **Examples**: Google, eBay, LinkedIn, and Facebook were built around Big Data Analytics (BDA).
- **Three Pillars of BDA**:
  1. Social Networking
  2. Mobile Computing
  3. Cloud Computing

![image](https://github.com/user-attachments/assets/a29090f9-628c-4cd1-b885-f34c56865987)


### Sources of Big Data:
- **Social Networking Sites**: Activity, posts, messages, videos over platforms like WhatsApp, Facebook, etc.
- **IoT Devices**: Smartwatches, Smart TVs
- **Financial Market Data**
- **Web Server Logs**
- **Banking Transactions**
- **Traffic Flow Sensors**
- **Scans of Government Documents**
  
Big Data = Transactions + Interactions + Observations

---

# Characteristics of Big Data Analytics (5 V's)

### 1. Volume (Quantity)
- A vast amount of data is generated every second/minute.
- **Example**: A Boeing 737 generates 240TB of flight data for a single flight.
- **Example**: Twitter generates 12TB of tweets every day.
- Big data tools use distributed systems to store and analyze data across databases worldwide.

### 2. Velocity (Speed)
- The speed at which Big Data is generated is very fast and it moves around quickly.
- It needs to be processed rapidly.
- **Example**: Over 3.5 billion searches are made per day on Google.
- **Example**: E-promotions: Based on your current location, purchase history, and preferences, you receive real-time promotions for a nearby store.
- **Example**: If you like the PS5 and pass by a Sony store, you might get a real-time notification.
- **Healthcare Monitoring Example**: If a patient's blood pressure is high, immediate alerts are sent to medical professionals.

### 3. Variety (Sources/Formats of Data)
- Big Data comes in structured, semi-structured, and unstructured forms.
  - **Structured Data**: Transactional tables, legacy data.
  - **Text Data**: Unstructured web documents, log files.
  - **Graph Data**: Social networks, semantic web (PDF).
  - **Streaming Data**
  - **Public Data**: Online weather, finance data.
  - **3D Data**: Photos, audio files, video recordings.
  
A single application can generate or collect various types of data.

### 4. Veracity (Trustworthiness of Data)
- With many forms of Big Data, maintaining:
  - Quality
  - Reliability
  - Accuracy
  - Completeness becomes challenging.
  
**Example**: Twitter messages with abbreviations, typos, or hashtags may create data quality issues.

### 5. Value (The Most Important 'V')
- Data in itself is of no use unless it is converted into something valuable.
- **Value** refers to the ability to turn data into insights.
- The one 'V' that matters the most.
- Big Data delivers value in almost every area of society or business.
  - **Example**: Amazon and Netflix recommendations help companies better understand and serve customers.
  - **Example**: Uber uses Big Data to predict demand, dynamically price journeys, and send the closest driver to the customer.
  - **Example**: Law enforcement agencies use Big Data to prevent terrorist attacks and detect cybercrimes.
  - **Example**: Sports teams analyze athletes' performances using Big Data.

---

| **Traditional Data**        | **Big Data**                            |
|-----------------------------|-----------------------------------------|
| Volume: GB to TB             | Volume: Petabytes to Zettabytes         |
| Deals with structured data   | Structured, semi-structured, unstructured |
| Data generated per hour/day  | Data generated per second               |
| Normal system configuration  | Requires high system capability         |
| Data size is small           | Data size > traditional data            |
| Manageable volume            | Difficult to manage and manipulate      |
| Data generated within enterprises | Data generated outside the enterprise |
| Data integration is easy     | Data integration is very difficult      |


---

# Challenges in Big Data Analytics (BDA):

1. **Data Volume**:  
   Large data volumes require scalable storage solutions. Cloud storage platforms like **Amazon S3**, **Google Cloud Storage**, and **Microsoft Azure** offer scalable options. Data compression and deduplication can optimize storage use and reduce costs.
   
2. **Data Variety**:  
   Handling diverse data types (structured, semi-structured, and unstructured) is complex. Tools like **Apache Nifi** and **Talend**, along with schema-on-read approaches, help manage this diversity.
   
3. **Data Velocity**:  
   High-speed data generation necessitates real-time processing. Frameworks like **Apache Kafka** and **Apache Flink** enable real-time data processing, while edge computing reduces latency.
   
4. **Data Veracity**:  
   Ensuring data quality is critical. Data governance, including quality standards and audits, along with tools like **Trifacta** and **Talend Data Quality**, help maintain accuracy.
   
5. **Data Security and Privacy**:  
   Protecting sensitive information requires encryption, access controls, and compliance with privacy regulations (e.g., **GDPR**, **CCPA**). Implementing privacy-by-design principles and conducting regular security audits is essential.
   
6. **Data Integration**:  
   Integrating data from various sources, including legacy systems, is challenging. Platforms like **Apache Camel** and **MuleSoft**, coupled with a microservices architecture, simplify this process.
   
7. **Data Analytics**:  
   Analyzing large datasets can be overwhelming. Tools like **Apache Spark** and **Google BigQuery**, combined with data literacy initiatives, enhance analytical capabilities.
   
8. **Data Governance**:  
   Effective governance policies and standards are crucial. Tools like **Collibra** and **Informatica** support data consistency and compliance with regulatory requirements.

---

# What is Hadoop?

**Hadoop** is an open-source, Java-based programming framework that enables the processing and storage of extremely large datasets in a distributed computing environment. It's a part of the **Apache** ecosystem.

### Key Features:
- **Scalability**: It can scale up to thousands of machines.
- **Fault Tolerance**: It is designed to detect and handle failures at the application layer.
- **Economical**: Runs on commodity hardware, making it cost-effective.
- **Hardware Failure Management**: Provides highly available services across clusters.
- **Massive Data Storage**: Stores large datasets on clusters of commodity hardware.
- **Fast Processing**: Enables quick data processing for large datasets.

### Core Components of Hadoop:

1. **HDFS (Hadoop Distributed File System)**:  
   A distributed file system providing high-throughput access to application data. It supports parallel processing, fault tolerance, and high availability.
   
2. **YARN (Yet Another Resource Negotiator)**:  
   YARN manages job scheduling and cluster resources, ensuring efficient processing.

3. **MapReduce**:  
   A YARN-based system that enables the parallel processing of large datasets.

### Advantages of Hadoop:

1. **Scalability**: Servers can be added or removed from the cluster dynamically.
2. **Economical**: It's open-source and compatible across platforms (Java-based).
3. **Distributed System Support**: Users can quickly write and test distributed systems.
4. **Fault Tolerance & High Availability**: Automatically handles failures and ensures uptime.

---

# Core Components of Hadoop

### HDFS (Hadoop Distributed File System):
- **Distributed File System**: HDFS is designed to store massive amounts of data across multiple machines.
- **Fault Tolerance**: It provides redundancy by storing data across different machines to prevent loss in case of failure.
- **Parallel Processing**: HDFS enables parallel processing by making application data available across clusters.
- **Cluster Management**: The built-in NameNode and DataNode servers help manage the cluster and monitor its status.
- **Streaming Access**: Provides high-throughput streaming access to the data.
- **Scalability**: HDFS scales easily, accommodating large datasets by distributing data across inexpensive commodity hardware.
- **Security**: Offers file permission and authentication to ensure data security.

---

### NameNode (Master Server):
- **Cluster Information**: Manages cluster metadata, including communication with YARN and jar files.
- **Replication**: It is replicated to ensure high availability.
- **Commodity Hardware**: Runs on GNU/Linux OS and commodity hardware with NameNode software.
- **Namespace Management**: Manages the filesystem namespace and maintains "inode" information (metadata about files and directories).
- **Block Mapping**: Maps inodes to data blocks and their respective locations in the cluster.
- **Client Access**: Controls client access by managing authentication and authorization of file operations (like renaming, opening, and closing files).
- **Data Block Monitoring**: Monitors the health of data blocks, replicating any missing blocks to maintain data integrity.


Here's a more structured and easy-to-understand breakdown of using **aggregation** and **annotation** in Django QuerySets, with examples, SQL queries, and real-world scenarios.

---

## **Aggregation Over QuerySets (Min, Max, Sum, Count, Avg)**

**Aggregation** is used to compute values (like `sum`, `average`, `min`, `max`, etc.) over a set of rows in the database. The result is a **single value** for the entire queryset.

### **Example: Counting the Number of Restaurants**
```python
from django.db.models import Count

restaurants = Restaurant.objects.aggregate(total=Count('id'))
print(restaurants)
```
**Output:**
```python
{'total': 14}
```
**SQL Query:**
```sql
SELECT COUNT("core_restaurant"."id") AS "total" FROM "core_restaurant";
```

---

### **Example: Calculating the Average Rating of a Restaurant**
```python
from django.db.models import Avg

average_rating = Rating.objects.aggregate(avg_rating=Avg('rating'))
print(average_rating)
```
**Output:**
```python
{'avg_rating': 2.36}
```
**SQL Query:**
```sql
SELECT AVG("core_rating"."rating") AS "avg_rating" FROM "core_rating";
```

---

### **Real-World Scenario: Aggregating Sales Data**
Imagine a sales reporting tool that needs to display the **total sales**, **minimum income**, **maximum income**, and the **average income** of restaurants in the last month.

```python
from django.db.models import Sum, Min, Max, Avg
from django.utils import timezone

one_month_ago = timezone.now() - timezone.timedelta(days=30)
sales = Sale.objects.filter(date__gte=one_month_ago)

report = sales.aggregate(
    total_sales=Sum('income'),
    min_income=Min('income'),
    max_income=Max('income'),
    avg_income=Avg('income')
)

print(report)
```
**Output:**
```python
{'total_sales': 5743.40, 'min_income': Decimal('6.25'), 'max_income': Decimal('99.22'), 'avg_income': Decimal('57.43')}
```
**SQL Query:**
```sql
SELECT SUM("core_sale"."income") AS "total_sales", MIN("core_sale"."income") AS "min_income", 
MAX("core_sale"."income") AS "max_income", AVG("core_sale"."income") AS "avg_income" 
FROM "core_sale" WHERE "core_sale"."date" >= '2024-09-05';
```

---

## **Annotating Querysets**

**Annotations** allow you to add **calculated fields** to each row of the queryset. Instead of a single value for the entire queryset (like aggregation), each object in the queryset gets the annotated value.

### **Example: Adding the Length of a Restaurant’s Name**
```python
from django.db.models.functions import Length

restaurants = Restaurant.objects.annotate(len_name=Length('name'))
print(restaurants.values('name', 'len_name'))
```
**Output:**
```python
<QuerySet [{'name': 'Bombay Bustle', 'len_name': 13}, {'name': 'Chinese 2', 'len_name': 9}, ...]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", LENGTH("core_restaurant"."name") AS "len_name" 
FROM "core_restaurant";
```

---

### **Example: Annotating Total Sales for Each Restaurant**
```python
from django.db.models import Sum

restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income'))
for r in restaurants:
    print(r.name, r.total_sales)
```
**Output:**
```python
Bombay Bustle 3000.0
Chinese 2 2000.0
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", SUM("core_sale"."income") AS "total_sales" 
FROM "core_restaurant" LEFT OUTER JOIN "core_sale" ON ("core_restaurant"."id" = "core_sale"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---

### **Real-World Scenario: Annotating the Number of Reviews per Restaurant**
You’re building a restaurant review app and need to show the **number of reviews** and the **average rating** for each restaurant.

```python
from django.db.models import Count, Avg

restaurants = Restaurant.objects.annotate(
    num_reviews=Count('ratings'),
    avg_rating=Avg('ratings__rating')
)

for r in restaurants:
    print(f'{r.name}: {r.num_reviews} reviews, {r.avg_rating} avg rating')
```
**Output:**
```python
Pizzeria 1: 2 reviews, 2.5 avg rating
Pizzeria 2: 4 reviews, 2.5 avg rating
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", COUNT("core_rating"."id") AS "num_reviews", 
AVG("core_rating"."rating") AS "avg_rating" 
FROM "core_restaurant" 
LEFT OUTER JOIN "core_rating" ON ("core_restaurant"."id" = "core_rating"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---

## **Using `values()` and `values_list()`**

- **`values()`** returns a **dictionary** for each object in the queryset.
- **`values_list()`** returns a **tuple** for each object in the queryset.

### **Example: Using `values()`**
```python
restaurants = Restaurant.objects.values('name', 'date_opened')
print(restaurants)
```
**Output:**
```python
<QuerySet [{'name': 'Bombay Bustle', 'date_opened': datetime.date(2024, 8, 24)}, {'name': 'Chinese 2', 'date_opened': datetime.date(2024, 9, 6)}]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", "core_restaurant"."date_opened" 
FROM "core_restaurant";
```

---

### **Example: Using `values_list()`**
```python
restaurants = Restaurant.objects.values_list('name', flat=True)
print(restaurants)
```
**Output:**
```python
<QuerySet ['Bombay Bustle', 'Chinese 2', 'Golden Dragon', ...]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name" FROM "core_restaurant";
```

---

## **Transforming Values with `Upper()` and `Concat()`**

### **Example: Uppercasing Restaurant Names**
```python
from django.db.models.functions import Upper

restaurants = Restaurant.objects.values(name_upper=Upper('name'))
print(restaurants)
```
**Output:**
```python
<QuerySet [{'name_upper': 'BOMBAY BUSTLE'}, {'name_upper': 'CHINESE 2'}, ...]>
```
**SQL Query:**
```sql
SELECT UPPER("core_restaurant"."name") AS "name_upper" FROM "core_restaurant";
```

---

### **Example: Concatenating Fields with `Concat()`**
```python
from django.db.models import Value, CharField
from django.db.models.functions import Concat

restaurants = Restaurant.objects.annotate(
    message=Concat('name', Value(' [Rating: '), Avg('ratings__rating'), Value(']'), output_field=CharField())
)

for r in restaurants:
    print(r.message)
```
**Output:**
```python
Bombay Bustle [Rating: 2.0]
Chinese 2 [Rating: 2.5]
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name" || ' [Rating: ' || AVG("core_rating"."rating") || ']' AS "message" 
FROM "core_restaurant" LEFT OUTER JOIN "core_rating" ON ("core_restaurant"."id" = "core_rating"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---
