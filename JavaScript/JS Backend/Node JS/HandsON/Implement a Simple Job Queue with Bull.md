


### **Question 10: Implement a Simple Job Queue with Bull in Node.js**

**Problem:**  
Create a simple job queue in Node.js using the `Bull` library. Implement a job that processes a long-running task (e.g., a mock task that simulates processing with a delay) and then returns a result once completed. Demonstrate the use of adding, processing, and monitoring jobs.

**Answer:**  
Here’s the implementation using `Bull` for job queues:

1. **Install the required packages:**
    
    ```bash
    npm install express bull ioredis
    ```
    
2. **Create the Express app with a job queue:**
    

```javascript
const express = require('express');
const Bull = require('bull');
const app = express();

// Create a new queue
const queue = new Bull('jobQueue', {
  redis: { host: 'localhost', port: 6379 }, // Use Redis for job queue storage
});

// Job processing logic (simulate long-running task)
queue.process(async (job) => {
  console.log('Processing job:', job.id);
  // Simulating a long-running task (e.g., file processing, data crunching)
  await new Promise(resolve => setTimeout(resolve, 5000)); // 5 seconds delay
  return `Job ${job.id} completed successfully!`;
});

// Route to add a job to the queue
app.post('/add-job', async (req, res) => {
  try {
    const job = await queue.add({ task: 'longTask' }); // Add a job to the queue
    res.status(200).json({ message: 'Job added to the queue', jobId: job.id });
  } catch (err) {
    res.status(500).send('Error adding job to queue');
  }
});

// Route to get job status
app.get('/job-status/:id', async (req, res) => {
  try {
    const job = await queue.getJob(req.params.id);
    if (!job) {
      return res.status(404).send('Job not found');
    }
    const state = await job.getState(); // Get the current state of the job
    res.json({ jobId: job.id, state });
  } catch (err) {
    res.status(500).send('Error fetching job status');
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Explanation:**

1. **Bull Queue:**
    
    - We use `Bull` to create a job queue (`jobQueue`).
    - The queue is connected to a Redis instance (make sure Redis is running on `localhost:6379` or adjust the configuration accordingly).
2. **Job Processing:**
    
    - The `queue.process()` function defines the logic for processing jobs. In this case, the job simulates a long-running task by using `setTimeout` to introduce a 5-second delay before completing.
3. **Adding a Job:**
    
    - The `/add-job` route allows users to add jobs to the queue. Each job contains a simple task property (`task: 'longTask'`), which can be expanded for more complex jobs.
4. **Getting Job Status:**
    
    - The `/job-status/:id` route lets users check the status of a job by its ID. It returns the state of the job (e.g., `waiting`, `completed`, `failed`).
5. **Redis and Bull:**
    
    - Redis acts as the backend for the queue system. `Bull` will store jobs in Redis, allowing for job persistence, retries, delayed jobs, and more.

**Testing:**

1. **Add a Job:**
    
    - `POST /add-job` to add a new job to the queue.
    - Example response:
        
        ```json
        {
          "message": "Job added to the queue",
          "jobId": 1
        }
        ```
        
2. **Check Job Status:**
    
    - `GET /job-status/1` to check the status of the job (job ID 1).
    - Example response when the job is completed:
        
        ```json
        {
          "jobId": 1,
          "state": "completed"
        }
        ```
        
3. **Job Processing:**
    
    - Once the job is added, you will see logs in the console like:  
        `Processing job: 1`.

**Notes:**

- You need a Redis server running for this example to work. You can run Redis locally using Docker:
    
    ```bash
    docker run -p 6379:6379 redis
    ```
    

This completes the set of advanced Node.js interview questions! Let me know if you need any further clarification on any of the topics.

