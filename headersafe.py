import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection",
    "Cross-Origin-Resource-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Opener-Policy",
    "Cache-Control",
    "Pragma",
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Methods",
    "Access-Control-Allow-Headers",
    "Server",
    "Set-Cookie",
]

def check_security_headers(url):
    try:
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            if not response.headers:
                raise Exception("Empty headers with HEAD request.")
        except:
            print("[*] HEAD request failed or returned no headers. Trying GET...")
            response = requests.get(url, allow_redirects=True, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter the URL (include http/https): ").strip()
    check_security_headers(target_url)