import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"


def test_can_create_task():
    payload = new_task_pyload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    # create a task
    payload = new_task_pyload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # update the task
    new_pyload = {
        "content": "my update content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True,
    }
    update_task_response = update_task(new_pyload)
    assert update_task_response.status_code == 200

    # get and validate the changes

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_pyload["content"]
    assert get_task_data["is_done"] == new_pyload["is_done"]


def test_can_list_tasks():
    # create N tasks
    n = 3
    pyload = new_task_pyload()
    for _ in range(n):
        create_task_response = create_task(pyload)
        assert create_task_response.status_code == 200
    user_id = pyload["user_id"]
    list_task_response = list_task(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n


def test_can_delete_task():
    # create a task
    pyload = new_task_pyload()
    create_task_response = create_task(pyload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # delete task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # get the task, and check that it's not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404



def create_task(pyload):
    return requests.put(ENDPOINT + "/create-task", json=pyload)


def update_task(pyload):
    return requests.put(ENDPOINT + "/update-task", json=pyload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def list_task(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")


def new_task_pyload():
    task_id = f"test_task_{uuid.uuid4().hex}"
    content_task = f"test_content_{uuid.uuid4().hex}"

    print(f"Creating task for user {task_id} with content {content_task}")

    return {
        "content": content_task,
        "user_id": task_id,
        "is_done": False
    }








