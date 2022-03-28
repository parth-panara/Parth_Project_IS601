"""This page consists the test for terms, aaa, oops, and solid web pages"""

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



def test_request_aaa(client):
    """This checks the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"aaa" in response.data

def test_request_main_menu_aaa(client):
    """This checks menubar on AAAPage"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" ' \
           b'aria-current="page">Home</a></li>'in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python' \
           b'/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/aaa">AAA' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS' \
           b'</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID' \
           b'</a></li>'in response.data

def test_request_heading_aaa(client):
    """This checks the AAA page for the heading"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b'<h3><strong>Arrange</strong></h3>'in response.data
    assert b'<h3><strong>Act</strong></h3>'in response.data
    assert b'<h3><strong>Assert</strong></h3>' in response.data
    assert b'<h3><strong>Calculator Tutorial demonstrates AAA testing' \
           b'</strong></h3>' in response.data
    assert b'<h3><strong>Why is testing important?</strong></h3>' in response.data
    assert b'<h4>Step 1: Arrange</h4>' in response.data
    assert b'<h4>Step 2: Act</h4>'in response.data
    assert b'<h4>Step 3: Assert</h4>'in response.data

def test_request_aaa_images(client):
    """This checks the images and its properties for AAA Page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b'<div style="width:810px;height:1259px;border:1px solid #000;">' in response.data
    assert b'<h6 style="text-align:center">' in response.data
    assert b'<img src="/static/images/aaa page pics/test.jpg"' in response.data
    assert b'<img src="/static/images/aaa page pics/aaa cover pic.jpg"' in response.data

def test_request_aaa_content(client):
    """This checks a few content for AAA Page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b'It means prepare inputs, targets all the operations like need of object, ' \
           b'log in web etc.' in response.data
    assert b'Execution is being taken into the programming code syntax. For Instance, ' \
           b'it could be for function,'in response.data
    assert b'It means to add the result that we expect as outcome from program. So we can ' \
           b'verify/ test the response'in response.data
    assert b'We need a python test file to explain it. I am selecting a calculation_test.py ' \
           b'file from my calculator'in response.data
    assert b'program. please, follow steps number from 1 to 3 on right side of ' \
           b'image.' in response.data
    assert b'As well as other sorts of testing,AAA testing is critical to ' \
           b'ensuring that our'in response.data
    assert b'software is up and operating without any'in response.data
    assert b'problems.' in response.data
    assert b'The major purpose of unit testing is to find bugs and other ' \
           b'inconsistencies in the' in response.data
    assert b'application while it is still in' in response.data
    assert b'development so that these issues can be caught before the software ' \
           b'is released into' in response.data
    assert b'production.' in response.data
    assert b'I am arranging a test which I called ' \
           b'test_calculation_divide_get_result_method().' in response.data
    assert b'Here, In line 54 I am creating a condition for my test. The condition ' \
           b'is <strong>tuple_list =' in response.data
    assert b'After setting up the condition, we will generate a division action as ' \
           b'a method to call a tuple' in response.data
    assert b'list and store its value in the variable' in response.data
    assert b'calculation. see line number 55 of image.' in response.data
    assert b'In step 3, we will look for a result of step 1 and step2. So, to verify ' \
           b'step 1 and step2 in' in response.data
    assert b'regard to calculation object will play the' in response.data
    assert b'inheritance principle.' in response.data


def test_request_oops(client):
    """This checks the OOPS page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"oops" in response.data

def test_request_main_menu_oops(client):
    """This checks menubar on OOPS Page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" ' \
           b'aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">' \
           b'Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">' \
           b'Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" ' \
           b'href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data

def test_request_heading_oops(client):
    """This checks the AAA page for the heading"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b'<h3><strong>Encapsulation</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(a) Calculator program demonstrates ' \
           b'Encapsulation</h6>' in response.data
    assert b'<h3><strong>Inheritance</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(b) Calculator program ' \
           b'demonstrates' in response.data
    assert b'<h6 style="text-align:center">image(d) Calculator program demonstrates ' \
           b'Polymorphism</h6>' in response.data
    assert b'<h3><strong>Abstraction</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(e) Highlighted portion from ' \
           b'image c</h6>' in response.data
    assert b'<h6 style="text-align:center">Read Calculator program in terms of ' \
           b'OOPS!</h6></div>' in response.data

def test_request_oops_images(client):
    """This checks the images and its properties for OOPS Page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b'<img src="/static/images/oops page pics/oops cover pic.jpg"' in response.data
    assert b'href="https://www.geeksforgeeks.org/encapsulation-in-python/"' in response.data
    assert b'<img src="/static/images/oops page pics/encapsulation.jpg"' in response.data
    assert b'href="https://www.geeksforgeeks.org/inheritance-in-python/"' in response.data
    assert b'<h6 style="text-align:center">image(b) Calculator ' \
           b'program demonstrates' in response.data
    assert b'href="https://www.geeksforgeeks.org/polymorphism-in-python/"' in response.data
    assert b'<div style="width:610px;height:395px;border:1px solid #000;">' in response.data
    assert b'<div style="width:610px;height:612px;border:1px solid #000;">' in response.data
    assert b'<div style="width:610px;height:395px;border:1px solid #000;">' in response.data
    assert b'href="https://www.geeksforgeeks.org/abstract-classes-in-python/"' in response.data
    assert b'xmlns="http://www.w3.org/2000/svg"' in response.data
    assert b'<img src="/static/images/oops page pics/highlighted.jpg"' in response.data
    assert b'<img src="https://img.freepik.com/free-vector/calculator-concept-' \
           b'illustration_114360-1239.jpg?w=740&t=st=1648184398~exp=1648184998~hmac=' \
           b'ebfd792b05ba0a1006aa2156e76b028c069253dfd61103b712dce916c6bf6937"' in response.data
    assert b'<img src="/static/images/oops page pics/sub class-inheritance.jpg"' in response.data

def test_request_oops_content(client):
    """This checks content for OOPS Page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b'It means to protect(encapsulate) all the data and functions into class. ' \
           b'These protected members of'in response.data
    assert b'class are not accessible' in response.data
    assert b'from outside the class. We can access it within a class. Below is the example ' \
           b'of calculator project' in response.data
    assert b'which demonstrates the encapsulation.' in response.data
    assert b'In this above image of the calculator program has four methods namely add, ' \
           b'subtract, multiply,' in response.data
    assert b'division.' in response.data
    assert b' Calculator holds the instance . For example , (line number 10 of image) ' \
           b'addition instance store'in response.data
    assert b'inside the calculation variable that' in response.data
    assert b'This principle takes place in parent class(base class) and child ' \
           b'class(subclass).' in response.data
    assert b'Subtraction(), class Multiplication(), and' in response.data
    assert b'class Division() are all child classes of class Calculation() as shown in the ' \
           b'image(b). Here, the' in response.data
    assert b'subclasses inherit the property of its' in response.data
    assert b'parent class. This demonstrates Inheritance.' in response.data
    assert b'Polymorphism means having vivid or different forms.' in response.data
    assert b'Polymorphism refers to the ability of the function with the same ' \
           b'name to' in response.data
    assert b'carry different functionality altogether. It creates a structure that can use ' \
           b'many forms of objects.' in response.data
    assert b'Image(d) illustrates the principle' in response.data
    assert b'of polymorphism in calculator program.' in response.data
    assert b'In calculator program, get_result() method of line number 11, 17, 23, 29 convert ' \
           b'on any object of' in response.data
    assert b'method Add(), Subtract(), Multiply(), and Divide().' in response.data
    assert b'So, we can call get_result() method on any class of calculation (Addition(), ' \
           b'Subtraction(),' in response.data
    assert b'Multiplication(), and Division() classes )'in response.data
    assert b'and we will get a result. Thus, the overridden of get_result() method in ' \
           b'classes present a'in response.data
    assert b'polymorphism concept.' in response.data
    assert b'The abstraction principle helps to hide all relevant data about ' \
           b'object(calculation) in order to' in response.data
    assert b'reduce complexity and increase efficiency.' in response.data
    assert b'get_result() is performing an addition method in line number 35 of ' \
           b'image(c or e).' in response.data
    assert b'a loop in addition class of calculator. In the loop, we' in response.data
    assert b'have an add function which abstracting a process of doing addition in a ' \
           b'list of numbers.' in response.data
    assert b'we have one function as a list and another is add() in a loop of def ' \
           b'get_result(self).' in response.data
    assert b'add(value, sum_of_values) function calls the addition calculation method. Both ' \
           b'function will give a' in response.data
    assert b'sum of list of numbers.' in response.data
    assert b'Thus, More complex of lists are broken down in one the function to another ' \
           b'function and that called' in response.data
    assert b'Abstraction.' in response.data
    assert b'This entire process of code will be hidden from user and only will invoke by ' \
           b'on classes Addition()' in response.data
    assert b'Subtraction(), Multiplication(), Division(). User is only allowed to run these ' \
           b'methods according to' in response.data
    assert b'their task.' in response.data


def test_request_solid(client):
    """This checks the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"solid" in response.data

def test_request_main_menu_solid(client):
    """This checks menubar on OOPS Page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" ' \
           b'aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">' \
           b'Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">' \
           b'Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/terms">' \
           b'Terms</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" ' \
           b'href="/solid">SOLID</a></li>' in response.data

def test_request_heading_solid(client):
    """This checks headings for the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b'<h3><strong>Single-Responsibility Principle</strong></h3>'in response.data
    assert b'<h6 style="text-align:center">image(a) Calculator program ' \
           b'demonstrates'in response.data
    assert b'<h3><strong>Open-Closed Principle</strong></h3>'in response.data
    assert b'<h6 style="text-align:center">image(b) Calculations_test.py file ' \
           b'of calculator program'in response.data
    assert b'<h3><strong>Liskov Substitution Principle</strong></h3>'in response.data
    assert b'<h6 style="text-align:center">image(c) Calculator program ' \
           b'demonstrates Encapsulation</h6>'in response.data
    assert b'<h3><strong>Interface Segregation Principle</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(d) Calculations_test.py file ' \
           b'of calculator program' in response.data
    assert b'<h3><strong>Dependency Inversion Principle</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(e) Calculations_test.py file ' \
           b'of calculator program' in response.data
    assert b'<h6 style="text-align:center">Learn about solid and design ' \
           b'pattern!</h6>' in response.data
    assert b'<h3><strong>Factory Design Pattern</strong></h3>' in response.data
    assert b'<h6 style="text-align:center">image(f) History test of ' \
           b'calculator program' in response.data

def test_request_solid_images(client):
    """This checks the images and its properties for SOLID Page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b'<img src="/static/images/solid pics/solid cover pic.jpg"'in response.data
    assert b'<div style="width:510px;height:510px;border:1px solid #000;">'in response.data
    assert b'<img src="/static/images/oops page pics/calculator ' \
           b'class-inheritance.jpg"' in response.data
    assert b'<img src="/static/images/oops page pics/sub class-inheritance.jpg"' in response.data
    assert b'<div style="width:510px;height:810px;border:1px solid #000;">' in response.data
    assert b'<img src="/static/images/oops page pics/encapsulation.jpg"' in response.data
    assert b'<img src="/static/images/oops page pics/sub class-inheritance.jpg"' in response.data
    assert b'<div style="width:510px;height:810px;border:1px solid #000;">' in response.data
    assert b'<div style="width:510px;height:810px;border:1px solid #000;">' in response.data
    assert b'<img src="/static/images/oops page pics/sub class-inheritance.jpg"' in response.data
    assert b'href="https://towardsdatascience.com/solid-coding-in-python-' \
           b'1281392a6a94"' in response.data
    assert b'<img src="https://www.coar-repositories.org/files/peer-review-2.jpg"' in response.data
    assert b'<div style="width:416px;height:1595px;border:3px solid #c2d4dd;">' in response.data
    assert b'<div style="width:392px;height:617px;border:1px solid #000;">' in response.data
    assert b'<img src="/static/images/solid pics/fp2.jpg"' in response.data
    assert b'href="https://www.inspiredpython.com/article/five-advanced-pytest-' \
           b'fixture-patterns"' in response.data

def test_request_solid_content(client):
    """This checks content for SOLID Page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b'The solid principles improve the reliability of our code by working on its ' \
           b'structure and its logical' in response.data
    assert b'consistency.</p>' in response.data
    assert b'The SOLID principles are:' in response.data
    assert b'<li>The Single-Responsibility Principle (SRP)</li>' in response.data
    assert b'<li>The Open-Closed Principle (OCP)</li>' in response.data
    assert b'<li>The Liskov Substitution Principle (LSP)</li>' in response.data
    assert b'<li>The Interface Segregation Principle (ISP)</li>' in response.data
    assert b'<li>The Dependency inversion Principle (DIP)</li>' in response.data
    assert b'It means a class should have only one reason to change.' in response.data
    assert b'There are subclasses Addition(), Subtraction(), Multiplication(), ' \
           b'Division() of base class' in response.data
    assert b'Calculator as shown in image() which' in response.data
    assert b'demonstrates Single-Responsibility Principle.' in response.data
    assert b'For instance, Division class has one function called divide() on ' \
           b'line 52 of image(a). This function' in response.data
    assert b'returns the' in response.data
    assert b'result of that function. So it has' in response.data
    assert b'only one task to return a result. Thus, if we change anything in ' \
           b'this function, it would not affect' in response.data
    assert b'on entire software behaviour. It will' in response.data
    assert b'only affect this class method.' in response.data
    assert b'In this above image of the calculator program has four methods ' \
           b'namely add, subtract, multiply,' in response.data
    assert b'division.' in response.data
    assert b'It means that the software entities should be open for extension but closed ' \
           b'for modification.' in response.data
    assert b'As discussed the earlier the subclasses Addition(), Subtraction(), ' \
           b'Multiplication(), Division()' in response.data
    assert b'inherit the property of class Calculation.' in response.data
    assert b'As shown in image(b) of calculator program, we can see the subclasses ' \
           b'inherited the tuple list data' in response.data
    assert b'from calculation class. Now, they are extending the new process as' in response.data
    assert b'described in the image (For instance, line number 38,39 and 40).' in response.data
    assert b'It means that Functions that use pointers or references to base ' \
           b'classes must be able to use objects' in response.data
    assert b'of derived classes without' in response.data
    assert b'knowing it.' in response.data
    assert b'Many client-specific interfaces are better than one general-purpose ' \
           b'interface' in response.data
    assert b'According to image(d), There are two abstract methods create() and ' \
           b'convert_args_to_tuple_of_float()' in response.data
    assert b'have been' in response.data
    assert b'used in class Calculator. Interface' in response.data
    assert b'is a one type of class, but it has only sign method body. So here, class ' \
           b'calculator contains smaller' in response.data
    assert b'interfaces(signed method body).' in response.data
    assert b'Now as per inheritance principle, the subclasses Addition(), ' \
           b'Subtraction(), Multiplication(),' in response.data
    assert b'Division() will have that interface property.' in response.data
    assert b'subclasses will segregate this interface and each subclass will use ' \
           b'it that interface methods.' in response.data
    assert b'It means that Abstractions should not depend on details. Details ' \
           b'should depend on abstraction.' in response.data
    assert b'High-level modules should' in response.data
    assert b'not depend on low-level modules. Both should depend on abstractions.' in response.data
    assert b'the process of creating an object from the code that depends on the ' \
           b'interface of the' in response.data
    assert b'object.' in response.data
    assert b'arguments' in response.data

def test_request_solid_content_second(client):
    """This checks more content for SOLID Page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b'to a fixture is the first thing that' in response.data
    assert b'require to do with @fixtures when we start using them.' in response.data
    assert b'<li> In calculator program of history test, I have defined the two ' \
           b'fixtures namely' in response.data
    assert b'<strong>def clear_history_fixture()</strong> and <strong>' in response.data
    assert b'setup_addition_calculation_fixture()</strong> in line number ' \
           b'8 and 15 of image' in response.data
    assert b'<li>Now, I have created <strong>def test_add_calculation' \
           b'_to_history' in response.data
    assert b'(clear_history_fixture, setup_addition_calculation_fixture)' \
           b'</strong> on' in response.data
    assert b'line number 50. I have passed the two parameters to get a Test for ' \
           b'clear history' in response.data
    assert b'returns true for success regarding the mentioned' in response.data
    assert b'function. This process describes the implementation of factory ' \
           b'design pattern'in response.data
