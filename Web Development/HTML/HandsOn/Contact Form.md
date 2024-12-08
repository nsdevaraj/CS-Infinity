


### **3. Create a Contact Form**

**Question:**  
Create a simple contact form with validation for required fields: name, email, and message.

**Solution:**


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <form id="contactForm" onsubmit="logFormDetails(event)">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" placeholder="Your full name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Your email address" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" placeholder="Write your message here" required></textarea>
        
        <button type="submit">Submit</button>
    </form>

    <script>
        function logFormDetails(event) {
            // Prevent the form from submitting to the server
            event.preventDefault();

            // Get the form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Log the details to the console
            console.log("Form Submitted!");
            console.log("Name:", name);
            console.log("Email:", email);
            console.log("Message:", message);
        }
    </script>
</body>
</html>

```


