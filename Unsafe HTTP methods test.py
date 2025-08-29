import http.client
import ssl
import socket


target = input("Please enter the URL (without http/https): ")

methods = ["OPTIONS", "TRACE", "PUT", "DELETE", "DEBUG"]
ports = [80, 443, 8080]
headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/plain, */*"
        }
        
def test_method(host, port, method):
    try:
        # Pick HTTPS for 443, otherwise HTTP
        if port == 443:
            context = ssl._create_unverified_context()
            conn = http.client.HTTPSConnection(host, port, context=context, timeout=5)
        else:
            conn = http.client.HTTPConnection(host, port, timeout=5)

        conn.request(method, "/", headers=headers)
        response = conn.getresponse()

        print(f"[+] {method} on {host}:{port} -> {response.status} {response.reason}")


        if method == "OPTIONS":
            allow = response.getheader("Allow")
            if allow:
                print(f"    Allowed methods: {allow}")

        conn.close()

    except (ConnectionRefusedError, socket.timeout, TimeoutError):
        print(f"[-] {method} on {host}:{port} -> No response / connection refused")
    except ssl.SSLError as e:
        print(f"[-] {method} on {host}:{port} -> SSL error: {e}")
    except Exception as e:
        print(f"[-] {method} on {host}:{port} -> Error: {e}")

# Main loop
for port in ports:
    print(f"\n=== Testing {target}:{port} ===")
    for method in methods:
        test_method(target, port, method)