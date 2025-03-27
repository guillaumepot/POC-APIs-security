# scripts/test_api_routes.py


# Lib
import requests

API_BASE_URL = "http://localhost:8000"


routes_to_test = [
                # Utils
                {'route': '/login',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                'data': 'grant_type=password&username=John%20Doe&password=johndoe'},

                {'route': '/read_payload',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/jwt_secret_key',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                # Vuln 1
                {'route': '/vuln1/broken/collaborator/3',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln1/fixed/collaborator/3',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                # Vuln 2
                {'route': '/vuln2/broken/login?username=admin&password=test',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln2/fixed/login?username=admin&password=test',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},
                ]




def test_route(url=API_BASE_URL, route="/", method="GET", headers=None, data=None):
    if method == "GET":
        response = requests.get(url + route, headers=headers, data=data)
    elif method == "POST":
        response = requests.post(url + route, headers=headers, data=data)
    elif method == "PUT":
        response = requests.put(url + route, headers=headers, data=data)
    elif method == "DELETE":
        response = requests.delete(url + route, headers=headers, data=data)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

    return response.json()


if __name__ == "__main__":
    with open("./logs/script_test_api.log", "w") as file:
        file.write("Testing routes:\n")

        token = None

        for route in routes_to_test:
            if token and route['headers']['Authorization'] is None:
                route['headers']['Authorization'] = f"Bearer {token}"

            response = test_route(API_BASE_URL,
                                  route['route'],
                                  route['method'],
                                  route['headers'],
                                  route['data'])
            
            if route['route'] == '/login':
                token = response.get("access_token", "No token found")

            file.write(f"{route['route']} \n")
            file.write(f"{str(response)} \n\n")