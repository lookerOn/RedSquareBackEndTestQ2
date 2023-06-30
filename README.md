# RedSquareBackEndTestQ2

Two framework have been tried
:- Flask framwork with Python

1. Importing necessary libraries:
   - `hashlib`: Provides various hash functions, in this case, it's used to calculate SHA-256 hash.
   - `random`: Used to generate random strings.
   - `string`: Provides a set of constants containing letters and digits for generating random strings.
   - `time`: Used for introducing a delay in one of the endpoints.
   - `Flask`, `jsonify`: These are from the Flask framework to create a web application and return JSON responses.

2. Creating a Flask app:
   - `app = Flask(__name__)`: Creates a new Flask application.

3. Generating a random hash:
   - `generate_random_hash()`: This function generates a random string of length 32 (combination of letters and digits) and calculates its SHA-256 hash using the `hashlib` library. The resulting hash is returned as a hex string.

4. Defining endpoints:
   - `@app.route("/endpoint1")`: This decorator binds the function `endpoint1()` to the URL "/endpoint1". When the user sends an HTTP GET request to this URL, the function will be executed.
   - `@app.route("/endpoint2")`: This decorator binds the function `endpoint2()` to the URL "/endpoint2". Similar to endpoint1, this function will be executed when the user sends an HTTP GET request to this URL.

5. Implementing "endpoint1":
   - This endpoint (`/endpoint1`) is a simple GET request.
   - The function `endpoint1()` uses the `generate_random_hash()` function to generate a random hash and then returns it as a JSON response with the key "hash".

6. Implementing "endpoint2":
   - This endpoint (`/endpoint2`) also responds to a GET request.
   - Inside the function `endpoint2()`, there is an infinite loop (`while True:`).
   - In each iteration of the loop, the function sends a GET request to "/endpoint1" using `app.test_client().get("/endpoint1")`.
   - It then extracts the JSON data from the response and returns it as a JSON response to the client. However, the loop never continues to the next iteration, so this endpoint only provides one response.

7. Running the Flask application:
   - `app.run(host='0.0.0.0', debug=True)`: This statement runs the Flask application on the local host (0.0.0.0) and enables debugging.

Summary:
The provided code defines a Flask web application with two endpoints:
- `/endpoint1`: Returns a JSON response containing a randomly generated SHA-256 hash.
- `/endpoint2`: Sends a GET request to `/endpoint1` and returns the same hash value in a JSON response, but this endpoint keeps running indefinitely.

Note: The usage of an infinite loop in `endpoint2` might not be desirable in a real-world scenario, as it can lead to server resource exhaustion and poor performance. Instead, you could consider implementing some form of request throttling or rate limiting to prevent excessive requests.
____________________________________________________________________________________________________________________________________________________________________

  
:- NodeJs framework with JavaScript

1. Importing necessary libraries:
   - `express`: This is a popular Node.js web application framework used for building web applications and APIs.
   - `sha256`: This is a library used to calculate SHA-256 hash.

2. Creating an Express app:
   - `app = express()`: Creates a new Express application.

3. Implementing "endpoint1":
   - `app.get('/endpoint1', (req, res) => { ... })`: This sets up a GET route for the URL "/endpoint1".
   - Inside the route handler function, the following steps are performed:
     - `setTimeout(() => { ... }, 1000)`: Introduces a delay of 1 second (1000 milliseconds) before generating the random SHA-256 hash.
     - `Math.random().toString(36).substring(2, 34)`: Generates a random 32-character string using `Math.random()` and then converts it to base-36 (using `toString(36)`) to include both letters and digits. The `.substring(2, 34)` is used to trim the string to 32 characters.
     - `sha256(randomString)`: Calculates the SHA-256 hash of the random string generated in the previous step using the `sha256` library.
     - `res.json({ hash })`: Responds with the JSON object containing the generated SHA-256 hash.

4. Implementing "endpoint2":
   - `app.get('/endpoint2', async (req, res) => { ... })`: Sets up a GET route for the URL "/endpoint2".
   - Inside the route handler function, the following steps are performed:
     - `const response = await fetch('http://localhost:3000/endpoint1')`: Sends a GET request to the "/endpoint1" of the same server to obtain the random SHA-256 hash.
     - `data = await response.json()`: Extracts the JSON data from the response.
     - `res.json(data)`: Responds with the same JSON data obtained from "Endpoint #1".

5. Running the Express application:
   - `const PORT = 3000`: Sets the port number for the server to 3000.
   - `app.listen(PORT, () => { ... })`: Starts the Express app, and it listens on port 3000.
   - Once the server is up and running, it will log "Server running on http://localhost:3000" in the console.

Summary:
The provided code sets up an Express web application with two endpoints:
- `/endpoint1`: Responds with a JSON object containing a randomly generated SHA-256 hash. The hash is generated after a 1-second delay to simulate some processing time.
- `/endpoint2`: Sends a GET request to `/endpoint1` on the same server and responds with the same JSON data containing the random SHA-256 hash.

Note: The `fetch` function used in "Endpoint #2" is a client-side function typically available in modern web browsers. If you want to run this code on the server (Node.js environment), you'll need to use a library like `node-fetch` to perform the GET request to "Endpoint #1" from "Endpoint #2".


!! Both Load tester using Locust Python (Same Code)



![image](https://github.com/lookerOn/RedSquareBackEndTestQ2/assets/128567524/8c10b785-748e-46d2-887c-5c8aa3be94a9)

![image](https://github.com/lookerOn/RedSquareBackEndTestQ2/assets/128567524/cdbc5887-d8b7-4f8d-8a2b-26acf42a5525)


