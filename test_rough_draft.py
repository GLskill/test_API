# import requests
#
# ENDPOINT = "https://todo.pixegami.io"
#
# response = requests.get(ENDPOINT)
# print(response)
#
#
# data = response.json()
# print(data)
#
# status_code = response.status_code
# print(status_code)
#
#
# def test_can_call_endpoint():
#     response = requests.get(ENDPOINT)
#     assert response.status_code == 200
#     pass
#
#
# def test_can_create_task():
#     payload = {
#         "content": "string",
#         "user_id": "string",
#         "task_id": "string",
#         "is_done": False
#     }
#     create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
#     assert create_task_response.status_code == 200
#     data = create_task_response.json()
#
#     task_id = data["task"]["task_id"]
#     get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
#
#     assert get_task_response.status_code == 200
#     get_task_data = get_task_response.json()
#     assert get_task_data["content"] == "some other content"
#     assert get_task_data["user_id"] == payload["user_id"]
#
#
# def test_can_update_task():
#     pass
#
#
# def create_task(pyload):
#     return requests.put(ENDPOINT + "/cre")
