# 🔒 Security Headers Checker

A simple Python script that checks if a given URL has the important security headers configured properly.

It fetches all HTTP response headers and reports:
- Missing security headers
- Weak security settings (e.g., `Server` header exposed, missing `Secure`/`HttpOnly` on cookies)

---

## 🚀 Features
- Sends a `HEAD` request first (falls back to `GET` if needed)
- Lists **all response headers**
- Checks against a **comprehensive list** of modern security headers
- Gives **warnings** if important flags are missing (e.g., in cookies)
- Helps web developers and security testers quickly audit a website

---

## 📋 Security Headers Checked

| Header | Purpose |
|:-------|:--------|
| Content-Security-Policy | Prevent XSS and code injection |
| Strict-Transport-Security | Enforce HTTPS connections |
| X-Content-Type-Options | Prevent MIME type sniffing |
| X-Frame-Options | Protect against clickjacking |
| Referrer-Policy | Control referrer information |
| Permissions-Policy | Restrict browser features like camera, mic |
| X-XSS-Protection | Legacy browser XSS filter |
| Cross-Origin-Resource-Policy | Cross-origin resource isolation |
| Cross-Origin-Embedder-Policy | Cross-origin embedder isolation |
| Cross-Origin-Opener-Policy | Cross-origin opener isolation |
| Expect-CT | Certificate Transparency enforcement |
| Cache-Control | Cache behavior (privacy) |
| Pragma | Legacy cache control |
| Access-Control-Allow-Origin | CORS header |
| Access-Control-Allow-Methods | CORS header |
| Access-Control-Allow-Headers | CORS header |
| Feature-Policy | Deprecated; older feature restrictions |
| Server | Warn if server technology is exposed |
| Set-Cookie | Warn if missing Secure/HttpOnly flags |

check [this](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html) out for more information about security headers

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install the required library:
```bash
pip install requests
```
special thanks to ChatGPT to write readme.md :)
