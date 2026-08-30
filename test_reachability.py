import requests
import json

url = "http://localhost:8000/scan"
urls_to_test = [
    "google.com",
    "satheesh.com"
]

for test_url in urls_to_test:
    payload = {"url": test_url}
    try:
        print(f"\n--- Testing: {test_url} ---")
        response = requests.post(url, json=payload, timeout=15)
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Verdict: {data.get('status')}")
        print(f"Website Status: {data.get('website_status')}")
        print(f"Risk Score: {data.get('risk_score')}")
        print(f"Explanation Preview: {data.get('explanation')[:100]}...")
    except Exception as e:
        print(f"Error testing {test_url}: {e}")
