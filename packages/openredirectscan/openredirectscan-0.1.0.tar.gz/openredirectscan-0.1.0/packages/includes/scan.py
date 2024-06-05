import requests
from packages.includes import write

def open_redirect_scan(url, output=None):
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        if response.status_code == 302 and 'Location' in response.headers:
            redirect_url = response.headers['Location']
            if 'evil.com' in redirect_url:
                print(f"\nOpen Redirect Vulnerability Found: {url} -> {redirect_url}")
                if output is not None:
                    write.write(output, f"{url} -> {redirect_url}\n")
            else:
                print(f"No Open Redirect: {url} -> {redirect_url}")
        else:
            print(f"No Redirect or Not Vulnerable: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Invalid URL or Connection Error: {e}")

# Example usage with a list of URLs
if __name__ == "__main__":
    urls_to_scan = [
        'http://example.com/redirect?url=http://evil.com',
        'http://testsite.com/redirect?url=http://evil.com',
        'http://anotherexample.com/redirect?url=http://evil.com'
    ]
    output_file = 'vulnerable_urls.txt'
    for url in urls_to_scan:
        open_redirect_scan(url, output_file)