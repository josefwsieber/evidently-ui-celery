# Evidently UI Extension with Celery Task Scheduling
## Video Walkthrough ->
[![Alt Text](https://img.youtube.com/vi/LVglC8KsWz4/0.jpg)](https://www.youtube.com/watch?v=LVglC8KsWz4)


This project is an extension to Evidently UI that incorporates Celery for scheduling tasks, making it easier for users to adopt Evidently for monitoring their machine learning models when they don't have an existing setup for orchestration.

<img src="./docs/project.png" alt="alt text" width="500px">

## Purpose

The main goal of this project is to simplify the process of integrating Evidently into your machine learning workflow by providing a convenient way to schedule monitoring tasks using Celery. <br> <br>
By leveraging the power of Celery and Docker Compose, this extension allows users to quickly set up and run Evidently UI without the need for a complex orchestration infrastructure.

## Features

 Seamless integration with Evidently UI<br>
 Celery-based task scheduling for easy monitoring setup<br>
 Docker Compose for simple orchestration and deployment<br>
Ideal for users who want to adopt Evidently without an existing orchestration setup

## Prerequisites

Before running this project, ensure that you have the following installed on your system:

- **Docker**
- **Docker Compose**

## Getting Started

To get started with Evidently UI with Celery Task Scheduling, follow these steps:

```bash
#!/bin/bash

# Clone the repository
git clone https://github.com/jsieber2/evidently-ui-celery.git

# Navigate to the project directory
cd evidently-ui-celery

# Build and start the Docker containers using Docker Compose
# This command will download/build the necessary Docker images and start the 
# containers for Evidently UI, Celery, and any other required services.
docker-compose up --build
```

Note: Access the Evidently UI by opening your web browser and navigating to `http://localhost:8000`

You should now see the Evidently UI dashboard, where you can configure and monitor your machine learning models.

To stop the containers, press `Ctrl+C` in the terminal where you started the containers, and then run:

```bash
docker-compose down
```

This will stop and remove the containers.

Make sure to rebuild the Docker containers after making any changes to the files in the directory.

<!-- Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes and commit them with descriptive commit messages
Push your changes to your forked repository
Submit a pull request to the main repository -->

## More UI images

Click these toggles to expand...

<details>
<summary>Project Dashboard</summary>

<img src="./docs/dashboard.png" alt="Dashboard" width="500px">

</details>

<details>
<summary>Project Report</summary>

<img src="./docs/report.png" alt="Report" width="500px">

</details>

## Architecture

```mermaid
graph LR
    redis[Message Queue - Redis]
    scheduler[Celery Scheduler]
    worker[Celery Worker]
    evidently-ui[Evidently UI]
    volume[Shared Volume ./app/]

    scheduler -- Enqueue monitoring tasks --> redis
    worker -- Fulfill tasks --> redis
    worker -- Write JSON reports --> volume
    evidently-ui -- Read/visualize reports --> volume
```

<!-- License
This project is licensed under the MIT License. -->
## Acknowledgements

- **Evidently** - Open-source tool for monitoring machine learning models
- **Celery** - Distributed task queue library for Python
- **Docker** - Containerization platform
- **Docker Compose** - Tool for defining and running multi-container Docker applications