# scripts/test_api_routes.py


# Lib
import requests

API_BASE_URL = "http://localhost:8000"


broken_register_data = {
                        "firstname": "Louis",
                        "lastname": "Armstrong",
                        "email": "louis_armstrong@apisec.com",
                        "phone": "555-555-666",
                        "password": "louis_armstrong",
                        "department": "Hacker",
                        "annual_salary": 9999999,
                        "role": 9
                        }


fixed_register_data = {
                        "firstname": "Neil",
                        "lastname": "Armstrong",
                        "email": "neil_armstrong@apisec.com",
                        "phone": "555-555-600",
                        "password": "Ne1l_4rmstrong!"
                      }




routes_to_test = [
                # Utils
                {'route': '/login',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                'data': 'grant_type=password&username=john_doe&password=johndoe'},

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

                # Vuln 3
                {'route': '/vuln3/broken/activity?activity=log%20in',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln3/fixed/activity?activity=log%20in',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln3/broken/register',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': None},
                'data': broken_register_data},

                {'route': '/vuln3/fixed/register',
                'method': 'POST',
                'headers': {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': None},
                'data': fixed_register_data},


                # Vuln 4
                {'route': '/vuln4/broken/limited_route',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln4/fixed/limited_route',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},


                # Vuln 5
                {'route': '/vuln5/broken/limited_to_admin',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln5/fixed/limited_to_admin',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},


                # Vuln 6
                {'route': '/vuln6/broken/route_to_spam',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},

                {'route': '/vuln6/fixed/route_to_spam',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': None},


                # Vuln 7
                {'route': '/vuln7/broken/fetch',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'url=example.com'},

                {'route': '/vuln7/fixed/fetch',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'url=example.com'},


                # Vuln 8
                {'route': '/vuln8/broken/logs',
                'method': 'GET',
                'headers': {'accept': 'text/plain', 'Authorization': None},
                'data': None},

                {'route': '/vuln8/fixed/logs',
                'method': 'GET',
                'headers': {'accept': 'text/plain', 'Authorization': None},
                'data': None},


                # Vuln 9
                {'route': '/vuln9/beta/user_info',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'username=john_doe'},

                {'route': '/vuln9/administration/user_info',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'username=john_doe'},


                # Vuln 10
                {'route': '/vuln10/broken/sql_query',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'username=OR 1=1;--'},

                {'route': '/vuln9/administration/user_info',
                'method': 'GET',
                'headers': {'accept': 'application/json', 'Authorization': None},
                'data': 'username=OR 1=1;--'},

                ]



def check_api_status():
    try:
        response = requests.get(url=API_BASE_URL + "/", headers={'accept': 'application/json'})
        if response.status_code != 200:
            raise SystemExit(f"API is not running. Status code: {response.status_code}")
        else:
            print(f"{response.status_code}: API is running, starting tests...")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Failed to connect to the API: {e}")


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

    check_api_status()

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

    print("Tests completed. Check logs/script_test_api.log for results.")