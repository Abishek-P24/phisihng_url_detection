import requests
import sys

url = "http://localhost:8000/scan"
test_url = sys.argv[1] if len(sys.argv) > 1 else "google.com"

print(f"--- Testing: {test_url} ---")
try:
    response = requests.post(url, json={"url": test_url}, timeout=30)
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Verdict: {data.get('status')}")
    print(f"Website Status: {data.get('website_status')}")
    print(f"Risk Score: {data.get('risk_score')}")
    print(f"Explanation: {data.get('explanation')}")
except Exception as e:
    print(f"Error: {e}")
