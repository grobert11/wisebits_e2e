## to run tests on local machine type

    pip install -r requirements.txt
    pytest tests/test_w3school.py

## **to run tests in docker type**

    docker build -t tests_run . 
    docker run -i -t test_run /bin/bash
    pytest tests/test_w3school.py

#Note:
    you might have some issuies with run docker container on mac M1
    
