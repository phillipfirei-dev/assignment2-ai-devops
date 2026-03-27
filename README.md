# 🚀 Agentic AI-Enhanced DevOps Automation

## 📌 Overview
This project demonstrates the modernization of a legacy monolithic system into a **cloud-native microservices architecture**, combined with the development of an **Agentic AI-powered DevOps assistant**.

The solution integrates:
- Cloud-native design principles
- Kubernetes orchestration
- DevOps automation
- AI-driven log analysis

---

## 🏗️ Modernisation Analysis

### Legacy System (Monolith)
The original system is a tightly coupled monolithic e-commerce application with:
- Single deployment unit
- Shared database
- Limited scalability

### Key Issues
- Poor scalability
- High deployment risk
- Lack of fault isolation
- No observability (logging/monitoring gaps)

---

## ☁️ Cloud-Native Architecture

The system is redesigned into a **microservices architecture** consisting of:

- User Service
- Product Service
- Order Service
- Payment Service

### Key Features
- Independent service deployment
- Improved scalability and fault isolation
- API Gateway for request routing
- Kubernetes for orchestration

---

## ⚙️ Kubernetes Deployment

The application is containerized and deployed using Kubernetes.

### Features:
- Replica-based scaling
- Load balancing via services
- Rolling updates for zero downtime deployment

### Deployment File:
- `deployment.yaml`

---

## 🔄 Deployment Strategy

A **Rolling Update strategy** is implemented:
- Gradual updates without downtime
- Reduced deployment risk
- Automatic rollback capability

---

## 🤖 DevOps AI Agent

### 📌 Overview
A Python-based **Agentic AI system** is implemented to analyse CI/CD logs and classify failure types.

---

## 🧠 Agent Architecture

The agent follows a structured reasoning process:

1. **Planning**
   - Determines how to analyse CI logs

2. **Tool Execution**
   - Scans logs for known error patterns

3. **Self-Reflection**
   - Evaluates confidence in the result

---



## ⚡ Fail-Fast Mechanism

The system follows a **fail-fast approach**, where errors are detected early in the CI/CD pipeline, allowing:
- Faster debugging
- Reduced deployment failures
- Improved system reliability

---

## 📊 Agent Capabilities

The AI agent detects:
- Build failures
- Test failures
- Dependency errors

It simulates intelligent decision-making using:
- Pattern recognition
- Structured reasoning
- Confidence evaluation

---

## 📈 Role of AI in DevOps

This project demonstrates how AI enhances DevOps by:
- Automating log analysis
- Reducing manual intervention
- Improving incident response time
- Supporting proactive system monitoring


## 📁 Repository Structure

- agent.py → AI agent implementation
- deployment.yaml → Kubernetes configuration
- diagrams/ → Architecture diagrams
- report/ → Final report


## 🔍 Example Output
