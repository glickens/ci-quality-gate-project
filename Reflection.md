# Reflection: How Quality Gates Strengthen the Commit Stage

Quality gates strengthen the Commit Stage by adding automated checks that verify software quality before code can move further through the development process. Instead of depending only on manual review, developers receive immediate feedback when code does not meet required standards.

In this project, GitHub Actions automatically validates every commit by running tests, checking code coverage, performing linting analysis, and running SonarQube Cloud quality analysis. These checks help prevent unstable or low-quality code from reaching the protected master branch.

The minimum 80% coverage requirement ensures that code changes are supported by adequate testing. Flake8 helps maintain coding standards by detecting errors early, while SonarQube Cloud provides additional analysis for security, reliability, and maintainability.

Branch protection rules improve the Commit Stage by requiring successful CI checks before code can be merged. This creates a controlled development workflow where only validated changes become part of the main branch.

Overall, quality gates improve CI/CD practices by moving testing and analysis earlier in the development lifecycle. They reduce risks, improve collaboration, and help teams deliver more reliable software.