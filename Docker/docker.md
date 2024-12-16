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
