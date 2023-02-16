import requests

ENDPOINT = "https://todo.pixegami.io"


def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

    
def test_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    
    data = create_task_response.json()
    print(data)
    
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    
def test_update_task():
    payload = new_task_payload()
    create_new_task = create_task(payload)   
    assert create_new_task.status_code == 200
    task_id = create_new_task.json()["task"]["task_id"]
    
    new_payload = {
        "content": "updated_content",
        "is_done": True,
        "user_id": payload["user_id"],
        "task_id": task_id
    }
    
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]
    
    
def create_task(payload):
    return requests.put(ENDPOINT+ "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT+ f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content": "test_content",
        "user_id": "user",
        "is_done": False,
    }    
    
def update_task(payload):
    return requests.put(ENDPOINT+ "/update-task", json=payload)
        