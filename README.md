# Evidently UI Extension with Celery Task Scheduling
This project is an extension to Evidently UI that incorporates Celery for scheduling tasks, making it easier for users to adopt Evidently for monitoring their machine learning models when they don't have an existing setup for orchestration.

# Purpose
The main goal of this project is to simplify the process of integrating Evidently into your machine learning workflow by providing a convenient way to schedule monitoring tasks using Celery. 
By leveraging the power of Celery and Docker Compose, this extension allows users to quickly set up and run Evidently UI without the need for a complex orchestration infrastructure.
# Features

 Seamless integration with Evidently UI
 Celery-based task scheduling for easy monitoring setup
 Docker Compose for simple orchestration and deployment
Ideal for users who want to adopt Evidently without an existing orchestration setup

# Prerequisites
Before running this project, ensure that you have the following installed on your system:

Docker
Docker Compose

# Getting Started
To get started with Evidently UI with Celery Task Scheduling, follow these steps:

Clone the repository:
```git clone https://github.com/jsieber2/evidently-ui-celery.git```

Navigate to the project directory:
```cd evidently-ui-celery-extension```

Build and start the Docker containers using Docker Compose:
```docker-compose up --build```

This command will build the necessary Docker images and start the containers for Evidently UI, Celery, and any other required services.

Access the Evidently UI by opening your web browser and navigating to:
```http://localhost:8080```

You should now see the Evidently UI dashboard, where you can configure and monitor your machine learning models.

To stop the containers, press Ctrl+C in the terminal where you started the containers, and then run:
```docker-compose down```
This will stop and remove the containers.


Make sure to rebuild the Docker containers after making any changes to the files in the directory.
<!-- Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes and commit them with descriptive commit messages
Push your changes to your forked repository
Submit a pull request to the main repository -->

<!-- License
This project is licensed under the MIT License. -->
# Acknowledgements

Evidently - Open-source tool for monitoring machine learning models
Celery - Distributed task queue library for Python
Docker - Containerization platform
Docker Compose - Tool for defining and running multi-container Docker applications