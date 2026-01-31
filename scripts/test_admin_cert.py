import sys, pathlib
# ensure package root is on sys.path
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# 1) login
login = client.post('/admin/login', data={'username':'admin', 'password':'adminn@gmail12312'})
print('login status ->', login.status_code)
print('admin_session cookie ->', client.cookies.get('admin_session'))

# 2) submit certifications form (HTML form emulation)
form = {
    'title': 'sadfsadf',
    'issuer': 'sadfsadfsadfdf',
    'issue_date': '2026-02-01',
    'expiry_date': '2026-02-01',
    'credential_url': ''
}
resp = client.post('/admin/certifications', data=form, allow_redirects=False)
print('\nADMIN POST ->', resp.status_code)
print('Location header ->', resp.headers.get('location'))
print('\nResponse (first 1200 chars)')
print(resp.text[:1200])

# 3) call the API directly to confirm endpoint still works
api_payload = {
    'title': form['title'],
    'issuer': form['issuer'],
    'issue_date': form['issue_date'] + 'T00:00:00',
    'expiry_date': form['expiry_date'] + 'T00:00:00',
}
api_resp = client.post('/api/v1/certifications', json=api_payload)
print('\nAPI POST ->', api_resp.status_code)
print(api_resp.text)
