import pytest
import requests

base_url = "https://yougile.com/api-v2"
login_credentials = {
    'login': '', # Прописать E-mail
    'password': '', # Прописать пароль
    'companyId': '' # Прописать id компании
}


@pytest.fixture(scope="module")
def auth_token():
    with requests.Session() as session:
        response = session.post(base_url + '/auth/keys', json=login_credentials)
        response.raise_for_status()
        return response.json().get('key')


@pytest.fixture
def session(auth_token):
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {auth_token}'})
    return session


def test_create_project_success(session):
    project_data = {
        "title": "ТестТестТест",
        "users": {"": ""}  # Прописать {"id сотрудника":"роль сотрудника"}
    }

    response = session.post(base_url + '/projects', json=project_data)
    assert response.status_code == 201

    response_data = response.json()
    project_id = response_data.get('id')
    assert project_id is not None, "Project ID should not be None"

    print(f"Project successfully created with ID: {project_id}")
    return project_id


def test_create_project_missing_title(session):
    project_data = {
        # "title": "ТестТест",
        "users": {"": ""}  # Прописать {"id сотрудника":"роль сотрудника"}
    }

    response = session.post(base_url + '/projects', json=project_data)
    assert response.status_code == 400
    print("Negative test passed: Project creation failed due to missing title.")


def test_update_project_success(session):
    project_id = test_create_project_success(session)

    updated_project_data = {
        "title": "ТестОбновление",
        "users": {"": ""}  # Прописать {"id сотрудника":"роль сотрудника"}
    }

    response = session.put(base_url + f'/projects/{project_id}', json=updated_project_data)
    assert response.status_code == 200

    response_data = response.json()
    received_id = response_data.get('id')
    assert received_id == project_id, "The project ID remained unchanged"

    print(f"Project updated successfully with ID: {received_id}")


def test_update_project_failure_with_invalid_id(session):
    invalid_project_id = "invalid-id"

    updated_project_data = {
        "title": "НекорректныйТест",
        "users": {"": ""}  # Прописать {"id сотрудника":"роль сотрудника"}
    }

    response = session.put(base_url + f'/projects/{invalid_project_id}', json=updated_project_data)
    assert response.status_code == 404

    print(f"Project update failed with status code: {response.status_code}")


def test_get_project_positive(session):
    project_id = test_create_project_success(session)

    response = session.get(base_url + f'/projects/{project_id}')
    assert response.status_code == 200

    response_data = response.json()
    get_id = response_data.get('id')
    assert get_id == project_id, "The project ID remained unchanged"

    print(f"Project retrieved successfully with ID: {get_id}")


def test_get_project_negative(session):
    invalid_project_id = "invalid-id"

    response = session.get(base_url + f'/projects/{invalid_project_id}')
    assert response.status_code == 404

    print(f"Failed to retrieve project with status code: {response.status_code}")
