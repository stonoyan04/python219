import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_filtered_results():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        data = response.json()
        filtered_results = [
            post for post in data
            if len(post['title'].split()) <= 6 and post['body'].count('\n') <= 3
        ]
        print("Filtered GET Results:")
        for post in filtered_results:
            print(f"ID: {post['id']}, Title: {post['title']}")
        return filtered_results
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return []

def create_post():
    payload = {
        "title": "Sample Title",
        "body": "This is a sample body for testing POST request.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    if response.status_code == 201:
        print("Created Post:", response.json())
        return response.json()
    else:
        print(f"POST request failed with status code: {response.status_code}")
        return None

def update_post(post_id):
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This is an updated body for testing PUT request.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    if response.status_code == 200:
        print("Updated Post:", response.json())
        return response.json()
    else:
        print(f"PUT request failed with status code: {response.status_code}")
        return None

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with ID {post_id} successfully deleted.")
        return True
    else:
        print(f"DELETE request failed with status code: {response.status_code}")
        return False

if __name__ == "__main__":
    print("\n--- GET Request with Filtering ---")
    filtered_posts = get_filtered_results()
    print("\n--- POST Request ---")
    created_post = create_post()
    print("\n--- PUT Request ---")
    if created_post:
        updated_post = update_post(created_post['id'])
    print("\n--- DELETE Request ---")
    if created_post:
        delete_status = delete_post(created_post['id'])