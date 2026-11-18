# Hello DevOps — Kubernetes Homelab

A Python Flask application deployed on a local K3s Kubernetes cluster. This project demonstrates containerization, CI, security scanning, Kubernetes orchestration, Helm and autoscaling.

## Architecture

Developer → GitHub → GitHub Actions → Docker Build → Health Test → Trivy Scan

Docker Image → K3s → Kubernetes Deployment → Service → Traefik Ingress → hello.local

Metrics Server → HPA → Kubernetes Deployment

## Technology Stack

| Area | Technology |
|---|---|
| Application | Python, Flask, Gunicorn |
| Containerization | Docker |
| Source control | Git, GitHub |
| CI | GitHub Actions |
| Security scanning | Trivy |
| Orchestration | K3s, Kubernetes |
| Ingress | Traefik |
| Package management | Helm 4 |
| Metrics | Kubernetes Metrics Server |
| Autoscaling | Horizontal Pod Autoscaler |

## Features

- Flask application with `/` and `/health` endpoints.
- Docker image with health check.
- GitHub Actions pipeline for build, health testing and Trivy scanning.
- Single-node K3s Kubernetes cluster.
- Kubernetes Deployment, NodePort Service and Traefik Ingress.
- ConfigMap-based environment configuration.
- Kubernetes Secret for Flask signing key.
- Helm chart for application management.
- Helm upgrades and rollbacks.
- CPU-based Horizontal Pod Autoscaler.
- Container resource requests and limits.

## Kubernetes Configuration

Namespace: `hello-devops`

| Resource | Configuration |
|---|---|
| Deployment | hello-devops |
| Service | NodePort 30080 |
| Ingress | hello.local |
| ConfigMap | hello-devops-config |
| Secret | hello-devops-secret |
| HPA minimum | 1 replica |
| HPA maximum | 2 replicas |
| CPU target | 60% |

Application URL: http://hello.local

Health endpoint: `/health`

## Autoscaling Test

The HPA was tested using a controlled CPU workload.

- Started with one Pod.
- Scaled up to two Pods.
- Returned to one Pod after the workload ended.

## Helm Commands

Validate:

    helm lint helm/hello-devops

Check release:

    sudo env KUBECONFIG=/etc/rancher/k3s/k3s.yaml helm list -n hello-devops

Check HPA:

    sudo k3s kubectl get hpa -n hello-devops

Check resource usage:

    sudo k3s kubectl top nodes
    sudo k3s kubectl top pods -A

## CI Pipeline

GitHub Actions runs on pushes and pull requests targeting `main`.

1. Checkout source.
2. Build Docker image.
3. Start application container.
4. Test `/health`.
5. Scan image with Trivy for critical vulnerabilities.

The current pipeline does not publish images to a registry or deploy automatically to Kubernetes.

## Repository Structure

    hello-devops/
    ├── .github/workflows/ci-cd.yml
    ├── helm/hello-devops/
    ├── k8s/
    ├── Dockerfile
    ├── app.py
    ├── requirements.txt
    └── README.md

## Current Limitations

- Single-node K3s cluster.
- Local image import; no shared registry for worker nodes.
- HTTP Ingress; HTTPS is not configured.
- Secret is managed separately from the Helm chart.
- No automated Kubernetes deployment from GitHub Actions.

## Future Improvements

- Multi-node K3s.
- GitOps with Argo CD.
- Improved monitoring and observability.
- HTTPS and production-oriented security improvements.

Built as a hands-on DevOps and Kubernetes learning project.
