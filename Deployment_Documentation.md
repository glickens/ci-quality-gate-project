# Deployment Documentation

## Overview

This project implements a Continuous Delivery (CD) pipeline using GitHub Actions. Every successful build is automatically deployed to a staging environment hosted on Render. The pipeline validates the application before deployment and performs a smoke test to verify that the deployment completed successfully.

---

## CI/CD Architecture

Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Build and Validate
    │      ├── Install dependencies
    │      ├── Run Flake8
    │      ├── Run Pytest
    │      └── Upload build artifact
    │
    ▼
Deploy to Staging
    │
    ├── Download artifact
    ├── Trigger Render deployment
    ├── Wait for deployment
    └── Run smoke test
    │
    ▼
Render Staging Environment

---

## Deployment Platform

Platform: GitHub Actions

GitHub Actions was selected because it integrates directly with GitHub repositories, supports automated workflows, artifact management, environment protection, secrets management, and Continuous Delivery pipelines.

---

## Deployment Process

1. Code is pushed to the feature/staging-deployment branch.
2. GitHub Actions starts the Build and Validate job.
3. Dependencies are installed.
4. Flake8 performs linting.
5. Pytest executes automated tests.
6. The application artifact is uploaded.
7. The Deploy to Staging job begins after a successful build.
8. The artifact is downloaded.
9. Render Deploy Hook is triggered.
10. The application is deployed to the Render staging environment.
11. GitHub performs a smoke test using the /health endpoint.
12. Deployment completes successfully.

---

## Environment Configuration

GitHub Environment:
- Staging

Environment Secret:
- RENDER_DEPLOY_HOOK

Environment Variable:
- STAGING_URL

Sensitive deployment information is stored using GitHub Environment Secrets instead of being hardcoded into the workflow.

---

## Validation

The deployment was successfully validated by:

- Successful GitHub Actions pipeline execution.
- Successful deployment to Render.
- Live staging application.
- Successful smoke test using the /health endpoint.