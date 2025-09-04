# DevOps Assignment 1 – ACEest Fitness & Gym  

This project is a simple **Flask-based web application** for ACEest Fitness & Gym, integrated with **unit testing, pre-commit hooks, Docker containerization, and CI/CD automation** as part of a DevOps workflow.  

---

## Installation  

### Clone the Repository  
```bash
git clone https://github.com/AnilDora/DevopsAssignment1ACEest_Fitness-Gym.git
cd DevopsAssignment1ACEest_Fitness-Gym
```

### Running the Application  
1. Install Flask:  
   ```bash
   pip install flask
   ```
2. Save the `app.py` file and the `templates/` folder.  
3. Run the Flask app:  
   ```bash
   python app.py
   ```
<img width="1168" height="210" alt="image" src="https://github.com/user-attachments/assets/6e125077-6745-4496-9bcb-fde66309620e" />

4. Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## Install Dependencies  

```bash
pip install flask 
```

### Install Pytest for Unit Testing  
1. Install:  
   ```bash
   pip install pytest
   ```
2. Verify installation:  
   ```bash
   pip show pytest
   ```

---

## Unit Testing Framework Integration  

- The project uses **pytest** for testing.  
- Test results look like this:  

![Test Results](https://github.com/user-attachments/assets/c09d40d9-1f38-42d7-899d-a4b23eea183d)  

---

## Automated Testing Configuration  

1. Added `pytest.ini` in the project root to configure test discovery.  
2. Now whenever you run:  
   ```bash
   pytest
   ```  
   it will automatically detect and run tests from the `tests/` folder.  

📊 Example result:  
![Pytest Result](https://github.com/user-attachments/assets/7808ef90-1195-432b-9572-5bf79eaec5b1)  

---

## Pre-Commit Hook (Local Automation)  

1. Install pre-commit:  
   ```bash
   pip install pre-commit
   ```
2. Add a `.pre-commit-config.yaml` file to the project root.  
3. Install hooks:  
   ```bash
   pre-commit install
   ```

---

## Containerization with Docker  

1. Added `requirements.txt` (Flask + pytest).  
2. Created `Dockerfile` for building the project image.  
3. Added `.dockerignore` to exclude unnecessary files.  
4. Build the Docker image:

    ```bash
   docker build -t fitness-gym-app .
   ```
5. Pushing the Docker image with tag latest

   ```bash
   docker push fitness-gym-app:latest
   ```

Image successfully created and visible in Docker Desktop:  

![Docker Build](https://github.com/user-attachments/assets/36e47024-e069-45ed-aea5-aa1296093ffa)  

**Showing Docker Images in Docker Desktop**

![Docker Desktop 1](https://github.com/user-attachments/assets/543de038-bd70-463c-8dca-fce98a40d0f1)  
![Docker Desktop 2](https://github.com/user-attachments/assets/96c20221-baaa-4a83-900b-7e5c19e04e78)  

**Live Hosted and running the container in Docker Desktop**

<img width="1914" height="1019" alt="image" src="https://github.com/user-attachments/assets/092796d6-8de1-4d04-9240-48cadf4b95ed" />

**LIVE Application Running URL**

<img width="1911" height="972" alt="image" src="https://github.com/user-attachments/assets/61619c56-dda9-4d74-b489-4c5d73593ba9" />

---

## CI/CD Pipeline with GitHub Actions  

A fully automated **CI/CD pipeline** has been configured using **GitHub Actions**.   

### Workflow Features  
- **Automated Build** – Builds the Docker image on every push.  
- **Automated Testing** – Runs pytest inside the Docker container.  
- **Continuous Integration** – Ensures that code changes are verified before merging.  
- **Continuous Delivery** – Prepares the application image for deployment.  

### Workflow File (`.github/workflows/ci-cd.yml`)  

👨‍💻 Developed as part of **DevOps Assignment 1**.
