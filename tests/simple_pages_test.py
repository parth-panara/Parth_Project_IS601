"""This test the HomePage"""

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data


def test_request_main_menu_links(client):
    """This checks the menubar on GitPage"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/git">Git' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>'in response.data
    assert b' <li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>'in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data

def test_request_git(client):
    """This checks the GIT page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_h3(client):
    """This checks the page for the h3 heading"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'<h3>Branches: </h3>' in response.data
    assert b'<h3>Merge: </h3>' in response.data
    assert b'<h3>Commit: </h3>' in response.data
    assert b'<h3>Tags: </h3>' in response.data
    assert b'<h3>Repository: </h3>' in response.data

def test_request_docker(client):
    """This makes the Docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_menu_docker_links(client):
    """This checks the menubar on DockerPage"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b' <li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data

def test_request_docker_h(client):
    """This checks the heading on DockerPage"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<h3>Docker: </h3>'in response.data
    assert b'<h3>Docker Project starts: </h3>'in response.data
    assert b'<h5>Step 1.</h5>'in response.data
    assert b'<h5>Step 2.</h5>'in response.data
    assert b'<h5>Step 3.</h5>'in response.data
    assert b'<h5>Step 4.</h5>'in response.data
    assert b'<h5>Step 5.</h5>'in response.data
    assert b'<h5>Step 6.</h5>'in response.data
    assert b'<h5>Step 7.</h5>'in response.data
    assert b'<h5>Step 8.</h5>'in response.data

def test_request_decker_images(client):
    """This checks the images and its properties"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<h6 style="text-align:center">image(a) Docker Taxonomy</h6>'in response.data
    assert b'<div class="d-flex flex-column align-items-stretch ' \
           b'flex-shrink-0" style="width: 400px;">'in response.data
    assert b'<div style="width:410px;height:1150px;border:3px solid #c2d4dd;">'in response.data
    assert b'<div style="width:410px;height:250px;border:3px solid #c2d4dd;">'in response.data
    assert b'<div style="width:610px;height:350px;border:1px solid #000;">' in response.data

def test_request_python(client):
    """This makes the python page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_menu_python_links(client):
    """This checks the menubar on PythonPage"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/python">Python/Flask' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data

def test_request_python_images(client):
    """This checks the image content on PythonPage"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<div style="width:610px;height:308px;border:1px solid #000;">' in response.data
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0"' \
           b' style="width: 600px;">' in response.data
    assert b'<h6 style="text-align:center">image(b) Example of int_py file in my ' \
           b'flask app</h6>' in response.data
    assert b'<a href="https://www.python.org/">' in response.data


def test_request_python_h(client):
    """This checks the headings on PythonPage"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<h2><strong>Python/ Flask</strong></h2>' in response.data
    assert b'<h3>Pytest: </h3>' in response.data
    assert b'<h4>Testing with Pytest: </h4>' in response.data
    assert b'<h3>Creating simple pages and testing: </h3>' in response.data
    assert b'<h5>Step 1.</h5>' in response.data
    assert b'<h5>Step 2.</h5>' in response.data
    assert b'<h5>Step 3.</h5>' in response.data
    assert b'<h5>Step 4.</h5>' in response.data
    assert b'<h3>Link to the flask project on GitHub: </h3>' in response.data
    assert b'<h3>The purpose of files in the project: </h3>' in response.data


def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_menu_cicd_links(client):
    """This checks the menubar on cicdPage"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home' \
           b'</a></li>' in response.data
    assert b' <li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/' \
           b'Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/cicd">CI/' \
           b'CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data


def test_request_cicd_h(client):
    """This checks the headings on cicdPage"""
    response = client.get("/cicd")
    assert b'<h2><strong>Continuous Integration and Deployment</strong></h2>' in response.data
    assert b'<h3>GitHub actions: </h3>' in response.data
    assert b'<h6 style="text-align:center">image(a) Diagram of the GitHub ' \
           b'actions</h6></div>' in response.data
    assert b'<h3>Project setup for GitHub actions: </h3>' in response.data
    assert b'<h3>Deploy master to a production server: </h3>' in response.data
    assert b'<h4>Prerequisite</h4>' in response.data
    assert b'<h4>The steps in the process are as follows:</h4>' in response.data
    assert b'<h3>Deploy an image of my project to Dockerhub when master is ' \
           b'updated: </h3>' in response.data

def test_request_cicd_images(client):
    """This checks the properties of images on cicdPage"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b'<div style="width:610px;height:370px;border:1px solid #000;">' in response.data
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0" ' \
           b'style="width: 600px;">' in response.data
    assert b'<h6 style="text-align:center">image(a) Diagram of the GitHub ' \
           b'actions</h6>' in response.data

def test_request_cicd_steps(client):
    """This checks the procedure steps on cicdPage"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b'<P>Step 1: Under my repository name, click Pull requests.</P>' in response.data
    assert b'<P>Step 2: In the list of pull requests, click the pull request ' \
           b'you would like to review.</P>' in response.data
    assert b'<P>Step 3: On the pull request, click +/- Files changed.</P>' in response.data
    assert b'<P>Step 4: Review the changes in the pull request, and optionally, comment on ' \
           b'specific lines.</P>' in response.data
    assert b'<P>Step 5: Above the changed code, click Review ' \
           b'changes.</P>' in response.data
    assert b'<P>Step 6: Type a comment summarizing your feedback on the proposed ' \
           b'changes.</P>' in response.data
    assert b'<P>Step 7: Select Approve to approve merging the changes proposed ' \
           b'in the pull request.</P>' in response.data
    assert b'<P>Step 8: Click Submit review.</P>' in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
