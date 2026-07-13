# Version Control & Continuous Integration Foundation

![CI](https://github.com/glickens/ci-quality-gate-project/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project demonstrates a Continuous Integration foundation using Git, GitHub, and GitHub Actions. The purpose is to make sure code is checked automatically whenever changes are pushed or submitted through a pull request.

Repository:

https://github.com/glickens/ci-quality-gate-project

## Branching Strategy

This project uses a feature branch workflow.

The `master` branch contains the approved version of the project. New work is completed in a separate feature branch and merged into `master` through a pull request.

Example branch name:

```text
documentation-quality-report
