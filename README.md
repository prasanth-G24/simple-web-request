# simple-web-request
This project is created for simplifying java HTTP requests. This is inspired from python's request library. You can send http requests with just one line of code. This is still in beta and I will be adding functionalities for PUT and DELETE requests soon. Feel free to contribute to this project. For and doubts reach me at prasanthmaverick@gmail.com.

This project depends on org.json library. You can get it [here](https://github.com/stleary/JSON-java)

## Code snippets

### HTTP GET
We can send GET requests in 4 ways:
  * GET without parameters and headers
  * GET with parameters and without headers
  * GET with headers and without parameters
  * GET with both parameters and headers
## Make sure to import these Classes before compilation! 
```java
import org.simplehttp.Request;
import org.simplehttp.Response;
```

**Simple GET**
```java
Request request = new Request();
Resposne response = request.get("www.example.com");
int statusCode = response.statusCode;
String responseText = response.responseText;
JSONObject json = response.getJSONResponse();
String encoding = response.encoding;
```
**GET with parameters**
```java
HashMap<String, String> params = new HashMap<String, String>();
params.put("paramname","paramvalue");
Request request = new Request();
Resposne response = request.get("www.example.com", params, "");
```
**GET with headers**
```java
HashMap<String, String> headers = new HashMap<String, String>();
headers.put("headername","headervalue");
Request request = new Request();
Resposne response = request.get("www.example.com", "", headers);
```
**GET with both parameters and headers**
```java
HashMap<String, String> params = new HashMap<String, String>();
HashMap<String, String> headers = new HashMap<String, String>();
params.put("paramname","paramvalue");
headers.put("headername","headervalue");
Request request = new Request();
Resposne response = request.get("www.example.com", params, headers);
```
### HTTP POST

The POST method works exactly like the GET method. That is the main advantage of this library. When you want to pass request body, pass it in the same way as passing the request headers in GET.

