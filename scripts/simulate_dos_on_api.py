# scripts/simulate_dos_on_api.py


# Lib
import concurrent.futures
from tqdm import tqdm
import requests


BASE_URL = "http://localhost:8000"
BROKEN_ROUTE = f"{BASE_URL}/vuln4/broken/limited_route"
FIXED_ROUTE = f"{BASE_URL}/vuln4/fixed/limited_route"


NUM_REQUESTS = 200

def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code, response.json()
    except Exception as e:
        return "Error", str(e)


def test_route(route, label):
    print(f"🔄 Testing {label} ({route})...")
    
    success_count = 0
    rate_limited_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(tqdm(executor.map(send_request, [route] * NUM_REQUESTS), total=NUM_REQUESTS, desc=label))

    for status, _ in results:
        print(status)
        if status == 200:
            success_count += 1
        elif status == 429:
            rate_limited_count += 1

    print(f"✅ {label}: {success_count} success")
    print(f"❌ {label}: {rate_limited_count} rate-limited (429 Too Many Requests)")
    print("-" * 50)

if __name__ == "__main__":
    test_route(BROKEN_ROUTE, "Broken Route (No Rate Limit)")
    test_route(FIXED_ROUTE, "Fixed Route (Rate Limited)")