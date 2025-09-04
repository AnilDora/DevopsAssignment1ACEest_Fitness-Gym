# DevopsAssignment1ACEest_Fitness-Gym
ACEest_Fitness and Gym


Installation
# Clone the repository
git clone https://github.com/AnilDora/DevopsAssignment1ACEest_Fitness-Gym.git

cd user-service

# Running it
1. Install Flask:

   pip install flask
3. Save the new app.py + templates/ folder.
4. Run: 

    python app.py
5. Visit http://127.0.0.1:5000

# Install dependencies
pip install flask 
1. Install pytest in your environment
   

     pip install pytest
2. Verify pytest is installed

   pip show pytest

# Unit Testing Framework Integration
Test Case Results
<img width="1904" height="1066" alt="image" src="https://github.com/user-attachments/assets/c09d40d9-1f38-42d7-899d-a4b23eea183d" />

# Automated Testing Configuration
Configured pytest to know how to discover and run tests.

Create a file in the project root called pytest.ini:
Now whenever we run **pytest**  it will automatically pick up everything inside tests/.

Result:
<img width="1825" height="1004" alt="image" src="https://github.com/user-attachments/assets/7808ef90-1195-432b-9572-5bf79eaec5b1" />

Pre-Commit Hook (Local Automation)
1. Install pre-commit:

      pip install pre-commit

2. Add a .pre-commit-config.yaml to your project root:

3. Install hooks:

   pre-commit install

# Containerization with Docker: 

1. Added requirements.txt to list all dependencies (Flask + pytest for dev/test):
2. Added Dockerfile, which will create the image of the project
3. Added .dockerignore file to avoid copying unnecessary files into the image.
4. Running docker build -t fitness-gym-app .

<img width="1916" height="1070" alt="image" src="https://github.com/user-attachments/assets/36e47024-e069-45ed-aea5-aa1296093ffa" />






    

   
    

   
