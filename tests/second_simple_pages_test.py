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

