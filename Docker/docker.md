# 🛠️ **Microservices, Containers, and Cloud Native**

---

## 🎯 **Microservices vs. Monolithic Architecture**

| **Aspect**           | **Monolithic Architecture**                                    | **Microservices Architecture**                      |
|-----------------------|---------------------------------------------------------------|----------------------------------------------------|
| **Definition**        | Built and deployed as a single unit.                          | Fine-grained services communicating via lightweight protocols. |
| **Deployment**        | The entire system is deployed at once.                        | Individual services can be deployed independently. |
| **Scaling**           | Scales as one large unit, leading to resource inefficiency.   | Scales each service independently.                |
| **Structure**         | 3-tier (Web ➡️ Business ➡️ Data).                             | Divides big systems into smaller services with specific responsibilities. |
| **Technology Choice** | Same tech stack across the system.                            | Each service can use its own language and database. |

---

### **Transitioning from Monolith to Microservices**
1. Break the application into small, manageable units.
2. Focus on the principle of **separation of responsibilities**.

---

## 🌟 **Benefits and Drawbacks of Microservices**

### **Benefits**
- **Improved Fault Isolation**: Issues in one service don’t affect others.
- **Smaller Deployments**: Faster and easier to understand.
- **Independent Scalability**: Scale only the services that need more resources.

### **Drawbacks**
| **Challenges**              | **Explanation**                                                      |
|------------------------------|----------------------------------------------------------------------|
| **Multiple Databases**       | Managing different databases for each service.                      |
| **Latency Issues**           | Increased communication overhead between services.                  |
| **Multiple Points of Failure** | Failure in one service may propagate if not handled properly.      |
| **Security**                 | More services mean more attack surfaces to secure.                  |

---

## 🌐 **Cloud Native Applications**

### **Key Principles**
| **Cloud Native Features**   | **Explanation**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Containers**              | Use lightweight containers for portability.                                    |
| **Service Meshes**          | Connect and manage microservices communication.                                |
| **Immutable Infrastructure**| Deploy infrastructure that cannot be modified, only replaced.                 |
| **Declarative APIs**        | Use APIs to define desired states for applications and infrastructure.         |

### **Design Philosophy**
- **Clean Code** using Domain-Driven Design (DDD).
- Transition to **Microservices Architecture**.
- Adopt **Kubernetes Patterns** for orchestration.

---

### **🛠 Pets vs. Cattle Mentality**
| **Pets**                     | **Cattle**                                  |
|------------------------------|---------------------------------------------|
| Individually managed servers. | Disposable, provisioned in minutes.        |
| Require manual updates/repairs. | Destroyed and re-provisioned automatically. |
| Unique and precious.          | Identical and replaceable.                 |

---

## 📦 **Containers**

### **What is a Container?**
A container is a **unit of software deployment** that packages:
- Code
- Runtime
- System Tools
- System Libraries

---

### **Why Use Containers?**
| **Advantages**               | **Details**                                                                       |
|------------------------------|----------------------------------------------------------------------------------|
| **Faster Deployments**        | Deploy smaller units quickly using CI/CD pipelines.                             |
| **Resource Efficiency**       | Fit more containers on the same host.                                           |
| **Isolation**                 | Separate environments to avoid conflicts.                                       |
| **Portability**               | Run anywhere (on-premise or cloud).                                             |

---

### **Containers vs. Virtual Machines (VMs)**

| **Feature**         | **Virtual Machines**                   | **Containers**                    |
|---------------------|----------------------------------------|-----------------------------------|
| **Boot Time**       | Slow (minutes).                       | Fast (seconds).                   |
| **Footprint**       | Heavy (entire OS and dependencies).   | Lightweight (shares host OS kernel). |
| **Ideal Use Case**  | Long-running tasks.                   | Short-lived or dynamic tasks.     |

---

### **Container Layers**
Containers are built in layers:
1. **Base OS** (Linux/Windows).
2. **Customizations** (dependencies, libraries).
3. **Application**.

Example:  
```bash
docker pull microsoft/dotnet
```
Each layer is downloaded individually and cached.

---

### **Container Registry**
A centralized repository for container images, similar to GitHub but for containers.
- **Docker Hub**: [hub.docker.com](https://hub.docker.com)
- **Cloud Providers**: AWS, Azure, Digital Ocean.

---

## ⚙️ **Container Orchestration**

### **What is Orchestration?**
Orchestration tools manage:
- Infrastructure
- Containers
- Deployment
- Scaling
- Failover
- Health Monitoring
- Zero Downtime Deployments

### **Popular Orchestrators**
| **Orchestrator**    | **Details**                                      |
|---------------------|-------------------------------------------------|
| **Kubernetes**      | Industry standard for container orchestration.  |
| **Docker Swarm**    | Native Docker orchestration solution.           |
| **Service Fabric**  | Used for microservices (e.g., Azure Service Fabric). |

---

## 🐳 **Docker Commands Cheat Sheet**

### **Basic Commands**
| **Command**                          | **Description**                                    |
|--------------------------------------|--------------------------------------------------|
| `docker pull [imageName]`            | Pull an image from a registry.                   |
| `docker run [imageName]`             | Run a container.                                 |
| `docker ps`                          | List running containers.                         |
| `docker stop [containerName]`        | Stop a running container.                        |
| `docker rm [containerName]`          | Remove a container.                              |
| `docker system prune -a`             | Clean up unused images, containers, and volumes. |

### **Advanced Commands**
| **Command**                          | **Description**                                    |
|--------------------------------------|--------------------------------------------------|
| `docker run --memory="256m" nginx`   | Limit memory usage to 256MB.                     |
| `docker run --cpus=".5" nginx`       | Limit CPU usage to 50%.                          |
| `docker run -d -p 8080:80 nginx`     | Run in detached mode and map port 8080 to 80.    |

---

## 📂 **Persistent Data with Volumes**

### **Types of Data**
| **Type**           | **Description**                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| **Ephemeral Data**  | Stored in a container's writable layer; lost when the container is destroyed. |
| **Persistent Data** | Stored outside the container using volumes, mapped to logical folders.        |

---

## 📄 **YAML in Docker Compose and Kubernetes**

- **YAML** stands for "YAML Ain't Markup Language."
- **Format**: Key-Value pairs.
  ```yaml
  version: '3.8'
  services:
    web:
      image: nginx
      ports:
        - "80:80"
  ```

---

## 🚀 **Docker Compose Commands**
| **Command**            | **Description**                                   |
|------------------------|--------------------------------------------------|
| `docker-compose build` | Build multi-container applications.              |
| `docker-compose up`    | Start all services in the background.            |
| `docker-compose down`  | Stop and remove all services.                    |
| `docker-compose logs`  | View container logs.                             |

---



# Docker Compose Workflow:

## 🛠 **Building and Running the Application**
1. **Build the Docker Compose services:**
   ```bash
   docker compose build
   ```

2. **Run the application in detached mode:**
   ```bash
   docker compose up -d
   ```

3. **Access the Voting App:**  
   Open your browser and visit:  
   👉 **http://localhost:5000**

---

## 📋 **Useful Docker Compose Commands**

### 1. **List Running Containers**
   ```bash
   docker compose ps
   ```

### 2. **Check Logs of Specific Services**  
   Example: Checking logs for the `web-fe` service.
   ```bash
   docker compose logs -f web-fe
   ```

### 3. **List Current Projects**  
   Displays all projects managed by Docker Compose:
   ```bash
   docker compose ls
   ```

---

## 🌟 **Deploying Multiple Versions**
By default, Docker Compose runs one instance of the application. To deploy multiple versions:

1. **Attempt to Deploy a Second Version:**  
   ```bash
   docker compose up -d
   ```  
   This fails because the `5000` port is already in use.

2. **Use a Different Project Name:**  
   Deploy with the `-p` flag and a custom project name:
   ```bash
   docker compose -p test up -d
   ```  
   This still fails if the same port (`5000`) is being used.

3. **Modify Ports:**  
   Change the port mapping in the `docker-compose.yml` file from:
   ```yaml
   - "5000:80"
   ```
   To:
   ```yaml
   - "5001:80"
   ```

4. **Deploy Again:**  
   ```bash
   docker compose -p test up -d
   ```

5. **Check Running Versions:**  
   ```bash
   docker compose ls
   ```

---

## 🧹 **Cleanup: Stop and Remove Containers**
To clean up running containers:

1. For the default project:
   ```bash
   docker compose down
   docker compose ls
   ```

2. For the custom project:
   ```bash
   docker compose -p test down
   docker compose ls
   ```

---

## 📝 **Example: Docker Compose YAML**
Here’s a complete example of a `docker-compose.yml` file:
```yaml
version: "3"
services:
  web-fe:
    build:
      context: .
    command: gunicorn --bind 0.0.0.0:5000 main:app
    ports:
      - "5001:5000"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PASSWORD=yourpasswordhere
  
  redis:
    image: redis:alpine
    ports:
      - "6371:6379"
    environment:
      - REDIS_PASSWORD=yourpasswordhere
```

---

## 📦 **Dockerfile**
Here’s an example `Dockerfile` to set up your application:
```dockerfile
FROM python:alpine
WORKDIR /code
ADD main.py requirements.txt /code/
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
```

---

## 🚀 **Advanced Docker Compose Features**

### 1. **Resource Limits**
Control resource usage with limits and reservations:
```yaml
resources:
  limits:
    cpus: '0.50'  # Max 50% of a single CPU
    memory: 150M  # Max 150 MB RAM
  reservations:
    cpus: '0.25'  # Reserve 25% of a single CPU
    memory: 20M   # Reserve 20 MB RAM
```

### 2. **Environment Variables**
Pass dynamic values using environment variables:
```yaml
db:
  image: "postgres:${POSTGRES_VERSION}"
```

### 3. **Networking**
Define how services communicate:
```yaml
services:
  web:
    image: nginx:alpine
    ports: 
      - "8000:80"  # External:Internal
  db:
    image: postgres
    ports:
      - "5432"
```
- **Web Access:** Accessible externally via port `8000`.
- **Database Access:** Web can use `5432` to communicate with `db`.

#### Restricting Visibility
To isolate services:
```yaml
networks:
  frontend:
  backend:
```

### 4. **Service Dependencies**
Ensure dependent services start first:
```yaml
app:
  image: myapp
  depends_on:
    - db

db:
  image: postgres
  networks:
    - back-tier
```
> Example: The `db` starts first because `app` depends on it.

---

## 📂 **Managing Data with Volumes**
- **Named Volumes:** Persist data even after stopping containers.
- Example:
  ```yaml
  volumes:
    db-data:
      driver: local
  ```

---

## 🔄 **Restart Policies**
Define container restart behavior:
```yaml
restart: "no"     # Default. Does not restart.
restart: "always" # Always restart until explicitly stopped.
```

---

## 🌐 **Using Container Registries**
Container images are stored in repositories:
- **Default:** [Docker Hub](https://hub.docker.com)
- **Private:** AWS Elastic Container Registry (ECR).

### **Push an Image to Docker Hub**
1. Build and tag the image:
   ```bash
   docker build -t username/repo:tag .
   ```

2. Log in to Docker Hub:
   ```bash
   docker login -u <username> -p <password>
   ```

3. Push the image:
   ```bash
   docker push username/repo:tag
   ```

### **Example:**
```bash
docker build -t aryanthedockerman/flask:v1 .
docker push aryanthedockerman/flask:v1
docker build -t aryanthedockerman/flask:v2 .
docker push aryanthedockerman/flask:v2
```

---

## 🌟 **Real-World Example: Scaling with Docker Compose**
- Imagine deploying a **voting app** with multiple frontends (`web-fe`) and a shared database (`redis`).  
- Each version can run on a unique port (`5000`, `5001`, etc.).  
- Use a **load balancer** (e.g., NGINX) to distribute traffic for high availability.

Docker Compose simplifies such deployments by managing dependencies, scaling, and resource allocation with minimal effort.

---

