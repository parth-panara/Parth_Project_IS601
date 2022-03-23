"""This test the TermsPage"""

def test_request_main_menu_terms(client):
    """This checks menubar on TermsPage"""
    response = client.get("/terms")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home' \
           b'</a></li>'in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/terms">Terms' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data

def test_request_terms(client):
    """This checks the Terms page"""
    response = client.get("/terms")
    assert response.status_code == 200
    assert b"terms" in response.data

def test_request_heading(client):
    """This checks the Terms page for the h3 heading"""
    response = client.get("/terms")
    assert response.status_code == 200
    assert b'<h3><strong>Class</strong></h3>' in response.data
    assert b'<h3><strong>Object</strong></h3>' in response.data
    assert b'<h3><strong>Instantiation</strong></h3>' in response.data
    assert b'<h3><strong>Namespace</strong></h3>' in response.data
    assert b'<h3><strong>Constructor</strong></h3>' in response.data
    assert b'<h3><strong>Fixture</strong></h3>' in response.data
    assert b'<h3><strong>Type hint</strong></h3>' in response.data
    assert b'<h3><strong>Type cast</strong></h3>' in response.data
    assert b'<h3><strong>Unit test</strong></h3>' in response.data
    assert b'<h3><strong>Static</strong></h3>' in response.data
    assert b'<h3><strong>Instance method</strong></h3>' in response.data
    assert b'<h3><strong>Instance property</strong></h3>' in response.data
    assert b'<h3><strong>Static method and property</strong></h3>' in response.data
    assert b'<h3><strong>Abstraction</strong></h3>' in response.data
    assert b'<h3><strong>Encapsulation</strong></h3>' in response.data
    assert b'<h3><strong>Inheritance</strong></h3>' in response.data
    assert b'<h3><strong>Polymorphism</strong></h3>' in response.data
    assert b'<h3><strong>Overview of SOLID</strong></h3>' in response.data
    assert b'<h4>Single responsibility Principle</h4>' in response.data
    assert b'<h4>Open/closed Principle</h4>' in response.data
    assert b'<h4>Liskov Substitution Principle</h4>' in response.data
    assert b'<h4>Dependency Inversion Principle</h4>' in response.data
    assert b'<h4>Interface Segregation Principle</h4>' in response.data
    assert b'<h3><strong>Overview of Design Patterns</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">' in response.data

def test_request_terms_images(client):
    """This checks the images and its properties for terms Page"""
    response = client.get("/terms")
    assert response.status_code == 200
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0" ' \
           b'style="width: 1296px;">' in response.data
    assert b'<div id="heading" class="p1 Web_link_Font"> <span style="float:' \
           b'right">' in response.data
    assert b'<div style="width:416px;height:290px;border:3px solid #c2d4dd;">' in response.data
    assert b'<div style="width:416px;height:1840px;border:3px solid #c2d4dd;">' in response.data

def test_request_terms_solid_overview(client):
    """This checks the content for terms Page"""
    response = client.get("/terms")
    assert response.status_code == 200
    assert b'<div id="paragraph" class="paraFont p1">' in response.data
    assert b'<ul style="list-style-type:circle;">' in response.data
    assert b'<li>Makes code more robust because of less side effects</li>' in response.data
    assert b'<li>Each class is responsible for one thing.</li>' in response.data

