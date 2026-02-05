import configuration as conf
from yougile_api import YougileApi
api_client = YougileApi(conf.base_url, conf.token)


def test_create_project_positive():
    payload = {
        "title": "Новый проект pytest",
        "users": {}
    }
    # Используем api_client вместо api
    response = api_client.create_project(payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title():
    payload = {
        "title": ""
    }
    response = api_client.create_project(payload)
    assert response.status_code == 400


def test_get_project_positive():
    temp_project = api_client.create_project({"title": "Проект для получения"}).json()
    project_id = temp_project["id"]

    response = api_client.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Проект для получения"


def test_get_project_negative_not_found():
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.get_project(non_existent_id)
    assert response.status_code == 404


def test_update_project_positive():
    temp_project = api_client.create_project({"title": "Старое название"}).json()
    project_id = temp_project["id"]

    new_data = {"title": "Обновленное название"}
    response = api_client.update_project(project_id, new_data) 
    assert response.status_code == 200
    check_resp = api_client.get_project(project_id)
    assert check_resp.json()["title"] == "Обновленное название"


def test_update_project_negative_bad_id():
    bad_id = "invalid-id-format"
    response = api_client.update_project(bad_id, {"title": "Error"})
    assert response.status_code in [400, 404]
