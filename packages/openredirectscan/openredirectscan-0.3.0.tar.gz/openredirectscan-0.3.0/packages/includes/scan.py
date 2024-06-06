import requests
from urllib.parse import urlparse
from packages.includes import write

def open_redirect_scan(long_url, output=None):
    print("analyzing URL:", {long_url})
    try:
        response = requests.get(long_url, allow_redirects=False, timeout=5)

        if response.status_code == 302 and 'Location' in response.headers:
            redirect_url  = response.headers['Location']
            print(f"Redirects to: {redirect_url}")
            
            if urlparse(long_url).netloc != urlparse(redirect_url).netloc:
                print("Redirects to another site.")
            else:
                print("Redirects to the same site.")
        else:
            print("Does not redirect.")
    except requests.exceptions.RequestException as e:
        print(f"Error analyzing the URL: {long_url} - {e}")
        return
    
if __name__ == "__main":
    long_url = input("Enter the long url to scan for open redirects: ").strip()
    open_redirect_scan(long_url, output=write)