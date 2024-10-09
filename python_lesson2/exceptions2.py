import requests

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: An issue occurred with the request: {e}")
    finally:
        print("API request completed.")

api_url = 'https://jsonplaceholder.typicode.com/posts'
result = fetch_data_from_api(api_url)

#Print the result if data is returned
if result:
    #print(result)
    for post in result[:2]:  # Print the first 5 posts for brevity
        print(f"Post ID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
                             
