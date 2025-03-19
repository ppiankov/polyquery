# Blockchain Client Application

This is a simple blockchain client implemented in Go that interacts with the Polygon network via its JSON-RPC API. The application exposes two endpoints to get the current block number and retrieve details about a specific block.

## Endpoints

- **GET /block/number**: Returns the latest block number.
- **GET /block/{block_number}**: Returns details of the specified block.

## Setup

*(Instructions for setting up the local environment, virtual environment, etc.)*

## Directory Structure
├── terraform
│   ├── main.tf         # Main Terraform configuration for ECS Fargate resources
│   ├── variables.tf    # Variable definitions for configuration parameters
│   ├── outputs.tf      # Outputs for key resources (e.g., ALB DNS name, ECS Cluster ID)
│   └── README.md       # terraform documentation file
├── app
│   ├── __init__.py       # This makes it a proper Python package so that it can be imported
│   ├── main.py           # FastAPI application with the endpoints
│   └── requirements.txt  # Dependencies list
├── tests
│   └── test_main.py      # Unit tests for the API endpoints
└── Dockerfile            # Dockerfile to build the container image
├── README.md             # This documentation file

### Building and Running Locally

1. Local development:
   ```bash
    pip install -r app/requirements.txt
    cd app
    uvicorn main:app --reload
   ```
   The API will be available at http://localhost:8000

   cli tests
   ```bash
    curl http://127.0.0.1:8000/block/number
    # Expected output: {"blockNumber":"0x420501f"} (example)

    curl http://127.0.0.1:8000/block/0x1
    # Expected output: {"block":{...}} (detailed block info)
   ```

2. Running Unit Tests:
   From the project root, run:
   ```bash
    pytest tests/test_main.py
   ```

2.1. if run from venv might need to add the project root to sys.path:
   add to tests/test_main.py:
   ```bash
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
   ```

3. Building the Docker Image:
   Build and run the Docker container:
   ```bash
    docker build -t blockchain-client .
    docker run -p 8000:8000 blockchain-client
   ```

## Deployment
### 4. The Terraform configuration is set up to run on ARM64 (Graviton2) in Fargate. Therefore, the container image should be built for ARM64. This ensures that your deployment leverages the cost and performance benefits of AWS Graviton2.

## Production Considerations

### 5. Production Readiness Considerations

To make this deployment production ready, consider enhancing the following areas:

- **Minimal Base Images:** Use minimal and secure base images (like Alpine or distroless) to reduce the attack surface.
- **Run as Non-Root:** Ensure containers do not run as the root user.
- **Image Scanning:** Regularly scan images for vulnerabilities using tools like Clair or Trivy.
- **Limited Capabilities:** Drop unnecessary Linux capabilities and apply resource limits.
- **Regular Updates:** Keep images and Docker Engine updated to the latest security patches.
- **AWS WAF:** Use AWS Web Application Firewall to help filter and block malicious traffic at the edge.
- **Security Groups and Network ACLs:** Configure these to restrict unwanted inbound *and* outbound traffic.
- **Monitoring & Automated Responses:** Set up logging (e.g., with CloudWatch) and use Lambda functions to react to suspicious behavior.

### 5. High-Load, High-Volume Considerations

- **Performance & Efficiency:**  
  Go is a compiled language, which generally results in faster execution and lower memory overhead compared to interpreted languages like Python. This can be critical when handling high throughput and low latency requirements.
- **Concurrency Model:**  
  Go’s built-in concurrency support using goroutines and channels makes it highly efficient for managing thousands of simultaneous connections. This design is well-suited for networking applications and can lead to more predictable performance under heavy load.
- **Deployment Simplicity:**  
  Go compiles to a single static binary, which simplifies deployment and reduces runtime dependencies. This can be an advantage in production environments where simplicity and reliability are key.
- **Robust Ecosystem for High Performance:**  
  Many high-performance systems and microservices have been successfully built using Go, particularly in areas like cloud services and real-time data processing.

---

### Summary

This project demonstrates a lightweight blockchain client that interacts with the Polygon network via JSON-RPC. It provides two primary endpoints to fetch blockchain data, making it suitable for rapid prototyping and integration into larger systems. The project is designed for local development using Python (with FastAPI) and Docker, while its deployment is facilitated by Terraform on AWS ECS Fargate with ARM64 (Graviton2) support. The README outlines steps for building, testing, and deploying the application, along with comprehensive production considerations covering security, scalability, and performance. 