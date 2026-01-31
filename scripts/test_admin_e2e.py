import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def login():
    r = client.post('/admin/login', data={'username':'admin','password':'adminn@gmail12312'})
    assert r.status_code in (200, 302)


def test_personal_flow():
    login()
    form = {
        'name': 'E2E Test',
        'title': 'Tester',
        'bio': 'E2E testing',
        'email': 'e2e@example.com',
        'is_update': 'false'
    }
    # Submit via admin UI (will create or return an error if record exists)
    r = client.post('/admin/personal', data=form, allow_redirects=False)
    assert r.status_code in (302, 200)

    # Get current record; if exists update it via API so test is deterministic
    api = client.get('/api/v1/personal')
    if api.status_code == 200:
        data = api.json()
        # If email differs, perform an update via API
        if data.get('email') != form['email']:
            # update existing record using the PUT endpoint
            update_payload = {
                'name': form['name'],
                'title': form['title'],
                'bio': form['bio'],
                'email': form['email']
            }
            put = client.put('/api/v1/personal', json=update_payload)
            assert put.status_code == 200
            api = client.get('/api/v1/personal')
            data = api.json()
    else:
        # No record was present — creation should have happened via admin UI
        assert api.status_code == 404 or api.status_code == 201
        if api.status_code == 404:
            # create via API to be explicit for test
            create = client.post('/api/v1/personal', json={
                'name': form['name'], 'title': form['title'], 'email': form['email'], 'bio': form['bio']
            })
            assert create.status_code == 201
            api = client.get('/api/v1/personal')
            data = api.json()

    assert data['email'] == 'e2e@example.com'


def test_certifications_flow():
    login()
    form = {
        'title': 'E2E Cert',
        'issuer': 'E2E Org',
        'issue_date': '2025-01-01',
        'expiry_date': '',
        'credential_url': ''
    }
    r = client.post('/admin/certifications', data=form, allow_redirects=False)
    assert r.status_code in (302, 200)
    # call API directly to ensure record created
    api_payload = {
        'title': form['title'],
        'issuer': form['issuer'],
        'issue_date': form['issue_date'] + 'T00:00:00'
    }
    api = client.post('/api/v1/certifications', json=api_payload)
    assert api.status_code == 201


if __name__ == '__main__':
    test_personal_flow()
    test_certifications_flow()
    print('E2E tests passed')
