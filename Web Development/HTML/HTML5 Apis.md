
### HTML5 APIs: Overview, Features, and Interview Q&A

HTML5 introduced several **APIs** to enhance the interactivity and functionality of web applications, providing powerful tools to interact with browsers, devices, and system resources.

---

### 1. **Geolocation API**
   - **Purpose**: Retrieves the user's geographic location (latitude and longitude) with their consent.
   - **Use Cases**: Location-based services, navigation apps, weather apps, and geotagging.
   - **Syntax**:
     ```javascript
     navigator.geolocation.getCurrentPosition(
       (position) => {
         console.log("Latitude:", position.coords.latitude);
         console.log("Longitude:", position.coords.longitude);
       },
       (error) => {
         console.error("Error occurred:", error.message);
       }
     );
     ```
   - **Key Methods**:
     - `getCurrentPosition()`: Gets the current location.
     - `watchPosition()`: Tracks location changes in real time.
     - `clearWatch()`: Stops location tracking.

   **Interview Q**: How does the Geolocation API work in HTML5?
   **A**: It retrieves the user's geographic location using the `navigator.geolocation` object, requiring explicit user consent for privacy.

---

### 2. **Canvas API**
   - **Purpose**: Enables drawing 2D graphics on a webpage.
   - **Use Cases**: Game development, data visualizations, image editing, and animations.
   - **Syntax**:
     ```html
     <canvas id="myCanvas" width="200" height="100"></canvas>
     <script>
       const canvas = document.getElementById("myCanvas");
       const ctx = canvas.getContext("2d");
       ctx.fillStyle = "blue";
       ctx.fillRect(20, 20, 150, 50); // Draws a rectangle
     </script>
     ```

   **Interview Q**: What is the difference between `<canvas>` and SVG?
   **A**: `<canvas>` is pixel-based and suitable for dynamic graphics, while SVG is XML-based and ideal for scalable, static graphics.

---

### 3. **Web Storage API**
   - **Purpose**: Provides client-side storage for key-value pairs without cookies.
   - **Components**:
     - **Local Storage**: Stores persistent data.
     - **Session Storage**: Stores data for the current session.
   - **Syntax**:
     ```javascript
     localStorage.setItem("key", "value");
     console.log(localStorage.getItem("key")); // "value"
     sessionStorage.setItem("sessionKey", "sessionValue");
     ```

   **Interview Q**: What is the difference between local storage and session storage?
   **A**: Local storage persists until explicitly cleared, while session storage is cleared when the browser or tab is closed.

---

### 4. **Drag and Drop API**
   - **Purpose**: Adds native drag-and-drop functionality to web elements.
   - **Use Cases**: File uploads, rearranging items, and interactive UIs.
   - **Syntax**:
     ```html
     <div id="drag" draggable="true" ondragstart="drag(event)">Drag Me!</div>
     <div id="drop" ondrop="drop(event)" ondragover="allowDrop(event)">Drop Here</div>
     <script>
       function allowDrop(event) {
         event.preventDefault();
       }
       function drag(event) {
         event.dataTransfer.setData("text", event.target.id);
       }
       function drop(event) {
         event.preventDefault();
         const data = event.dataTransfer.getData("text");
         event.target.appendChild(document.getElementById(data));
       }
     </script>
     ```

   **Interview Q**: How does the Drag and Drop API improve user interactivity?
   **A**: It allows native drag-and-drop support without relying on third-party libraries, simplifying UI development.

---

### 5. **File API**
   - **Purpose**: Enables users to select and read files from their local system.
   - **Use Cases**: File uploads, previews, and processing files within the browser.
   - **Syntax**:
     ```html
     <input type="file" id="fileInput">
     <script>
       document.getElementById("fileInput").addEventListener("change", (event) => {
         const file = event.target.files[0];
         const reader = new FileReader();
         reader.onload = () => console.log(reader.result); // File content
         reader.readAsText(file);
       });
     </script>
     ```

   **Interview Q**: What is the File API in HTML5?
   **A**: The File API allows web applications to access and read user-selected files directly within the browser.

---

### 6. **Media APIs**
   - **Purpose**: Handle audio and video playback, controls, and streaming.
   - **APIs**:
     - **Audio API**: Enhances audio processing and playback.
     - **MediaStream API**: Captures media streams (e.g., webcam, microphone).
   - **Syntax (MediaStream API)**:
     ```javascript
     navigator.mediaDevices.getUserMedia({ video: true, audio: true })
       .then((stream) => {
         const video = document.querySelector("video");
         video.srcObject = stream;
         video.play();
       })
       .catch((error) => console.error("Error accessing media devices:", error));
     ```

   **Interview Q**: How does the MediaStream API work in HTML5?
   **A**: It captures audio and video streams from user devices, enabling real-time media processing and communication.

---

### 7. **WebSocket API**
   - **Purpose**: Facilitates real-time, bidirectional communication between the browser and server.
   - **Use Cases**: Chat applications, live notifications, and gaming.
   - **Syntax**:
     ```javascript
     const socket = new WebSocket("wss://example.com/socket");
     socket.onopen = () => console.log("WebSocket connected");
     socket.onmessage = (event) => console.log("Message from server:", event.data);
     socket.send("Hello, Server!");
     ```

   **Interview Q**: What is the WebSocket API, and how does it differ from HTTP?
   **A**: WebSocket provides persistent, bidirectional communication, unlike HTTP, which is stateless and request-response-based.

---

### 8. **History API**
   - **Purpose**: Manipulates the browser's session history.
   - **Use Cases**: Single-page applications (SPAs) for handling navigation without full page reloads.
   - **Syntax**:
     ```javascript
     history.pushState({ page: 1 }, "Title", "/page1");
     window.onpopstate = (event) => console.log("State changed:", event.state);
     ```

   **Interview Q**: What is the History API in HTML5?
   **A**: It allows dynamic updates to the browser history, enabling SPAs to manage navigation without reloading the page.

---

### 9. **Notification API**
   - **Purpose**: Displays system-level notifications from the browser.
   - **Use Cases**: Alerts, updates, or reminders.
   - **Syntax**:
     ```javascript
     if (Notification.permission === "granted") {
       new Notification("Hello, User!", { body: "You have a new message!" });
     } else {
       Notification.requestPermission();
     }
     ```

   **Interview Q**: What is the Notification API, and when would you use it?
   **A**: It allows web apps to send system notifications, ideal for user alerts or updates.

---

### 10. **WebRTC API**
   - **Purpose**: Enables peer-to-peer communication (audio, video, and data sharing).
   - **Use Cases**: Video calls, screen sharing, and real-time file transfer.
   - **Syntax**:
     ```javascript
     const pc = new RTCPeerConnection();
     pc.createOffer().then((offer) => pc.setLocalDescription(offer));
     ```

   **Interview Q**: What is the WebRTC API, and why is it important?
   **A**: WebRTC provides real-time peer-to-peer communication, essential for video conferencing and live collaboration.

---

### Summary of Key HTML5 APIs for Interviews
1. **Geolocation API**: Accesses user location.
2. **Canvas API**: Creates 2D graphics.
3. **Web Storage API**: Stores data client-side.
4. **Drag and Drop API**: Adds drag-and-drop functionality.
5. **File API**: Reads local files.
6. **Media APIs**: Handles audio and video streaming.
7. **WebSocket API**: Real-time, bidirectional communication.
8. **History API**: Manages browser history dynamically.
9. **Notification API**: Sends system notifications.
10. **WebRTC API**: Peer-to-peer communication for video and data.

These APIs make HTML5 a robust platform for building modern, interactive web applications.