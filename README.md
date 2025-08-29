# unsafe-http-methods
Python script designed to test for unsafe or dangerous HTTP methods enabled on a web server. The script uses the http.client module to send various HTTP requests, including OPTIONS, TRACE, PUT, DELETE, and DEBUG, to a specified URL and port.

**Key Features**

**Method Enumeration:** The script can identify which HTTP methods are supported by the target server by sending an OPTIONS request and checking the "Allow" header in the response.

**Vulnerability Testing**: It tests for methods that are often considered unsafe for public-facing servers, such as TRACE (which can be leveraged for Cross-Site Tracing) and PUT/DELETE (which can allow unauthorized modification or deletion of resources).

**Connection Handling**: The script handles both HTTP (port 80, 8080) and HTTPS (port 443) connections and includes a timeout for requests.

**Error Handling**: It includes basic error handling for connection refusals, timeouts, and SSL errors.
