# HW №6 {3}

*Pavlo Kukurik | IT & BA*

## Task №1 – FastAPI App Containerized with Podman

### Build the Image

```bash
podman build -t fastapi-app1 .
```

### Run the Container

```bash
podman run -d -p 8000:8000 --name app1-container fastapi-app1
```

### Test the API

```bash
curl http://localhost:8000/
```

Expected:

```json
{"message":"Hello"}
```

### View Logs

```bash
podman logs app1-container
```

### Clean Up

```bash
podman stop app1-container
podman rm app1-container
podman rmi fastapi-app1
```

---

## Task №2 – FastAPI App with Periodic Requests

### Build the Image

```bash
podman build -t fastapi-app2 .
```

### Run the Container

```bash
podman run -d -p 8001:8001 \
  -e APP1_URL=http://host.containers.internal:8000 \
  --name app2-container fastapi-app2
```

### Test the API

```bash
curl http://localhost:8001/ping
```

Expected:

```json
{"message":"App2 is running"}
```

### View Logs (auto requests to App1)

```bash
podman logs app2-container
```

### Clean Up

```bash
podman stop app2-container
podman rm app2-container
podman rmi fastapi-app2
```

---

## Run Both Services with Podman Compose

### Build and Start Services

```bash
podman-compose up --build
```

### Test Services

```bash
curl http://localhost:8000/
```

Expected:

```json
{"message":"Hello"}
```

```bash
curl http://localhost:8001/ping
```

Expected:

```json
{"message":"App2 is running"}
```

### View Logs

```bash
podman logs app1-container
podman logs app2-container
```

### Stop and Clean Up

```bash
podman-compose down
```

