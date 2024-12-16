
# How to Dockerize Your Django Application
---

## 1. Install Docker Desktop
- Download Docker Desktop from [docker.com](https://www.docker.com/).

---

## 2. Understand Containers & Images

### **Images**
- Blueprints used to create containers, containing your app’s dependencies and configurations.  
- **Example:** A recipe or blueprint—like a cake recipe—you use to bake cakes.

### **Containers**
- Lightweight, portable environments that run your application.  
- **Example:** The actual cake made from the recipe, ready to eat or serve.

---

## 3. Prepare Your Django App for Docker
- Install Gunicorn for production readiness:

```bash
pip install gunicorn
pip freeze > requirements.txt
```

---

## 4. Create a Dockerfile
The `Dockerfile` contains instructions to build your application image.

```dockerfile
FROM python:3.8.3-slim

ENV PYTHONBUFFERED=1  # Useful for debugging

WORKDIR /dock_django

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000  # Make the app accessible outside the container
```

- **Base Image:** Choose a Python version from Docker Hub. Use slim variants (e.g., `3.8.3-slim`) for smaller images.

---

## 5. Create a `docker-compose.yaml` File
This file orchestrates multiple containers (if needed) and simplifies the build and run process.

```yaml
version: "3.8"
services:
  app:
    build: .
    volumes:
      - .:/dock_django
    ports:
      - 8000:8000
    image: app:dock_django
    container_name: tanjiro_container
    command: python manage.py runserver 0.0.0.0:8000
```

---

## 6. Build and Run the Container
- **Build the container:**
  ```bash
  docker-compose build
  ```
- **Start the container:**
  ```bash
  docker-compose up
  ```
- Visit `http://127.0.0.1:8000` to see your Django app live.

---

## 7. Environment Management
- Use `.env` files to store sensitive data and configuration variables locally.

**Example `.env` file:**
```plaintext
SECRET_KEY=your_secret_key
POSTGRES_USER=your_db_username
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=your_db_name
POSTGRES_HOST=your_db_host
```

- Access these variables in Django:
  ```python
  # settings.py
  import os

  SECRET_KEY = os.environ.get('SECRET_KEY')
  DB_USERNAME = os.environ.get('POSTGRES_USER')
  DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
  DB_DATABASE = os.environ.get('POSTGRES_DB')
  DB_HOST = os.environ.get('POSTGRES_HOST')
  ```

---

## 8. Clean Up Cache
- Free up space by pruning unused Docker resources:

```bash
docker system prune
```

---

## 9. Deploy Dockerized Django App on AWS with ECR and ECS

### Step 1: Create and Push Docker Image to AWS ECR

1. **Create an ECR Repository:**
   ```bash
   aws ecr create-repository --repository-name my-django-app
   ```
2. **Authenticate Docker with ECR:**
   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
   ```
3. **Build Docker Image:**
   ```bash
   docker build -t my-django-app .
   ```
4. **Tag the Docker Image:**
   ```bash
   docker tag my-django-app:latest <account_id>.dkr.ecr.<region>.amazonaws.com/my-django-app:latest
   ```
5. **Push Image to ECR:**
   ```bash
   docker push <account_id>.dkr.ecr.<region>.amazonaws.com/my-django-app:latest
   ```

### Step 2: Create a Task Definition for ECS
- Create a JSON file (e.g., `task-definition.json`) with the following content:
  ```json
  {
    "containerDefinitions": [
      {
        "name": "my-django-application",
        "image": "<account_id>.dkr.ecr.<region>.amazonaws.com/my-django-app:latest",
        "memory": "256",
        "cpu": "256",
        "essential": true
      }
    ],
    "networkMode": "bridge",
    "family": "django-app-task-definition"
  }
  ```

### Step 3: Deploy to ECS
1. **Register Task Definition:**
   ```bash
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
2. **Run the Task on ECS (EC2 or Fargate):**
   ```bash
   aws ecs create-service \
       --cluster <cluster-name> \
       --service-name my-django-app-service \
       --task-definition django-app-task-definition \
       --desired-count 1
   ```

---

## 10. Kubernetes Cluster Setup and Deployment

### Cluster Setup and Communication
- **Kubernetes Cluster:** DigitalOcean provisions a cluster of virtual machines (Droplets) with Kubernetes installed.
- **VPC Network:** Secure communication is established between your Kubernetes cluster and external services like databases (e.g., PostgreSQL).

### Application Deployment
1. **Deployments:**
   ```bash
   kubectl apply -f deployment.yaml  # Deploys the app
   kubectl get deployments          # Verifies the deployment
   kubectl get pods                 # Checks running pods
   kubectl exec -t <podname> -- /bin/bash  # Access pod shell
   ```

### Networking and Exposing Services
- **Expose Services:**
  ```bash
  kubectl get services
  ```
  _Sample Output:_
  ```plaintext
  NAME               TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)
  nginx-service      LoadBalancer   10.245.166.184  161.35.266.32    80:31988/TCP
  ```

### Scaling and Resource Management
- **Horizontal Scaling:**
  ```bash
  kubectl scale deployment nginx-deployment --replicas=5
  kubectl get pods  # Verify new pods
  ```
- **Rolling Updates:**
  ```bash
  kubectl set image deployment/nginx-deployment nginx=nginx:latest
  ```

---

## 11. Automate CI/CD Pipelines
- Use tools like GitHub Actions or Jenkins to automate deployments.

---

**Your Dockerized Django app is now ready to deploy, scale, and manage like a pro! 🚀**
