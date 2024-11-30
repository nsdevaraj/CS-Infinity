

### **Question 5: Implement File Upload with Multer in Node.js**

**Problem:**  
Write an Express.js application that allows users to upload files. Use the `multer` library to handle file uploads. Save the uploaded files in a `uploads/` directory and ensure only image files (`jpg`, `jpeg`, `png`) are allowed.

**Answer:**  
Here’s the implementation:

```javascript
const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();

// Configure Multer storage
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});

// File filter to allow only image files
const fileFilter = (req, file, cb) => {
  const allowedTypes = /jpeg|jpg|png/;
  const extname = allowedTypes.test(
    path.extname(file.originalname).toLowerCase()
  );
  const mimetype = allowedTypes.test(file.mimetype);

  if (extname && mimetype) {
    cb(null, true);
  } else {
    cb(new Error('Only image files are allowed!'));
  }
};

// Initialize Multer
const upload = multer({
  storage,
  fileFilter,
  limits: { fileSize: 2 * 1024 * 1024 }, // Limit file size to 2MB
});

// Route to handle file uploads
app.post('/upload', upload.single('image'), (req, res) => {
  res.send(`File uploaded successfully: ${req.file.filename}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    res.status(400).send(`Multer Error: ${err.message}`);
  } else if (err) {
    res.status(400).send(`Error: ${err.message}`);
  } else {
    next();
  }
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Explanation:**

1. **Storage Configuration:** Files are saved in the `uploads/` directory with unique names based on timestamps.
2. **File Filtering:** Only files with valid MIME types (`jpeg`, `jpg`, `png`) and extensions are accepted.
3. **Size Limit:** Files are restricted to 2MB.
4. **Error Handling:** Errors from `multer` or invalid files are handled gracefully.

**Testing:**  
Use tools like Postman or an HTML form with a file input field to test the `/upload` endpoint.

Let me know when you’re ready for the next one!

