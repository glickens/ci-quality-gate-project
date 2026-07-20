# Reflection

This project gave me practical experience building a Continuous Delivery pipeline from start to finish. I configured GitHub Actions to automatically build, validate, and deploy my application to a staging environment hosted on Render. Before deployment, the workflow installed dependencies, ran Flake8 for code quality, executed automated tests with Pytest, and packaged the application as an artifact.

One of the biggest challenges was configuring the deployment stage correctly. I had to connect GitHub and Render, create a staging environment, configure GitHub Environment Secrets and Variables, and troubleshoot deployment failures until the pipeline completed successfully. Working through these issues helped me better understand how CI/CD pipelines use automation to reduce manual deployment steps.

The most valuable lesson I learned is that Continuous Delivery depends on automation, validation, and repeatable deployments. Using GitHub Actions, Render, environment secrets, artifacts, and smoke tests demonstrated how modern DevOps pipelines ensure that every successful build can be deployed consistently and reliably to a staging environment before reaching production.