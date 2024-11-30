

## Pillars of System Design

### Pillars of System Design

To create a robust and resilient application, it’s essential to understand the following key pillars:

1. **Scalability**: The ability of the system to handle increased load by adding resources. This can be vertical (adding more power to existing machines) or horizontal (adding more machines).

2. **Reliability**: Ensures that the system consistently performs as expected, minimizing downtime and failures. This includes redundancy and failover strategies.

3. **Performance**: The speed and efficiency of the application, ensuring quick response times and optimal resource utilization.

4. **Maintainability**: The ease with which the system can be updated or modified. This includes clean code, proper documentation, and modular design.

5. **Security**: Protecting the system against unauthorized access and vulnerabilities. This involves implementing encryption, authentication, and authorization measures.

6. **Observability**: The ability to monitor and understand the internal state of the system through logging, metrics, and tracing, enabling effective debugging and performance analysis.

Understanding these pillars is crucial for designing systems that are not only functional but also robust and capable of adapting to changing demands.


### Principles of Good System Design

Good design in system architecture focuses on several key principles:

#### Key Principles:

1. **Scalability**: 
   - Ensures the system can grow alongside its user base.

2. **Maintainability**: 
   - Facilitates future developers' ability to understand and improve the system.

3. **Efficiency**: 
   - Optimizes resource usage for better performance.

4. **Resilience**: 
   - Plans for failure, ensuring the system can handle issues gracefully and maintain performance during failures.

In summary, good system design balances these principles to create robust, adaptable, and efficient applications.



## Key Elements of System Design

At the heart of system design are three essential elements:

1. **Moving Data**:
   - Ensures seamless data flow within the system, whether it’s user requests to servers or data transfers between databases. Optimization for speed and security is crucial.

2. **Storing Data**:
   - Involves choosing between SQL and NoSQL databases, but also understanding access patterns, indexing strategies, and backup solutions. Data must be stored securely and be readily accessible when needed.

3. **Transforming Data**:
   - Focuses on converting raw data into meaningful information, such as aggregating log files for analysis or formatting user input.

These elements are foundational for creating effective and efficient systems.



## The CAP Theorem

The **CAP Theorem**, also known as Brewer's Theorem, outlines key principles for trade-offs in distributed systems, focusing on three components: **Consistency**, **Availability**, and **Partition Tolerance**.

#### Key Concepts:

1. **Consistency**:
   - All nodes in the system reflect the same data at the same time. For instance, updating a Google Doc means everyone sees the changes immediately.

2. **Availability**:
   - The system remains operational and responsive to requests at all times, akin to a reliable online store that is always open to take orders.

3. **Partition Tolerance**:
   - The system continues to function even during network partitions, allowing nodes to operate despite communication disruptions. This is like a group chat where conversations continue even if one member loses connection.

#### Trade-Offs:

According to the CAP Theorem, a distributed system can achieve only two out of the three properties simultaneously:

- **Consistency + Partition Tolerance**: May compromise Availability.
- **Availability + Partition Tolerance**: May compromise Consistency.

**Example**: A banking system prioritizes Consistency and Partition Tolerance to ensure financial accuracy, even if it temporarily affects Availability.


![[ProductionAppArchitechture.png]]


### Decision-Making in Design

Every design decision involves trade-offs. For instance, optimizing for read operations might degrade write performance. To gain performance in write, we sacrifice bit of complexity. Therefore, the goal is not to find a perfect solution, but to identify the best solution for specific use cases, making informed choices about where compromises can be made.



## Availability

**Availability** is a critical measure of a system's operational performance and reliability. It addresses the question: Is our system up and running when users need it?

#### Key Points:

- **Measurement**: Availability is typically expressed as a percentage, with the goal of achieving "five nines" (99.999%).

- **Example**:
  - **99.9% Availability**: Allows for approximately 8.76 hours of downtime per year.
  - **99.99% Availability**: Reduces downtime to about 52.56 minutes per year.
  - **99.999% Availability**: Limits downtime to just about 5.26 minutes per year.

This distinction is significant, especially for critical services where every second counts.

- **Metrics**: Availability is measured in terms of **uptime** (the time the system is operational) and **downtime** (the time the system is non-operational).

In summary, high availability is crucial for maintaining user trust and ensuring the reliability of critical services.


## SLOs and SLAs

**Service Level Objectives (SLOs)** and **Service Level Agreements (SLAs)** are essential for managing system performance and user expectations.

#### Key Points:

- **SLOs**:
  - SLOs set specific goals for system performance and availability.
  - Example: An SLO might state that a web service should respond to requests within 300 milliseconds, 99.9% of the time.

- **SLAs**:
  - SLAs are formal contracts with users or customers that define the minimum level of service guaranteed.
  - Example: If an SLA guarantees 99.99% availability and the service drops below this threshold, the provider may need to offer refunds or other compensations.

In summary, SLOs focus on performance goals, while SLAs outline commitments to users, ensuring accountability and trust in service delivery.



### Building Resilience in Systems

Building resilience into our system involves anticipating potential failures and ensuring continuous operation.

#### Key Strategies:

1. **Redundant Systems**:
   - Implement backup systems that can take over in case of failure.

2. **Graceful Degradation**:
   - Design the system to maintain core functionality even when certain features are unavailable.

#### Key Concepts:

- **Reliability**:
  - Ensures that the system operates correctly and consistently under expected conditions.

- **Fault Tolerance**:
  - Prepares the system to handle unexpected failures or attacks, ensuring continued operation.

- **Redundancy**:
  - Involves having backups in place, so if one part of the system fails, another can immediately take its place.

In summary, resilience is about being proactive in design to maintain system performance and reliability in the face of challenges.


## Measuring System Speed: Throughput and Latency

To evaluate the speed of our system, we focus on two key metrics: **Throughput** and **Latency**.

#### Throughput

- **Definition**: Measures how much data the system can handle over a specific period.
  
- **Types**:
  - **Server Throughput**: Measured in **requests per second (RPS)**, indicating how many client requests a server can handle. A higher RPS value signifies better performance and capacity for concurrent users.
  
  - **Database Throughput**: Measured in **queries per second (QPS)**, reflecting the number of queries a database can process per second. Again, a higher QPS indicates improved performance.
  
  - **Data Throughput**: Measured in **bytes per second**, showing the amount of data transferred over a network or processed by a system within a given timeframe.

#### Latency

- **Definition**: Measures the time taken to handle a single request, or the duration from when a request is made until a response is received.

#### Trade-offs

Optimizing for one metric can often lead to compromises in the other. For instance, while batching operations can enhance throughput, it may also increase latency.

In summary, balancing throughput and latency is crucial for achieving optimal system performance.



## Importance of Thoughtful System Design

Designing a system poorly can lead to numerous issues, including performance bottlenecks and security vulnerabilities. Unlike code, which can be refactored relatively easily, redesigning a system is a monumental task.

#### Key Points:

- **Consequences of Poor Design**: Inadequate design can cause ongoing challenges that may affect performance and security.

- **Investment in Design**: It’s crucial to invest time and resources in getting the design right from the outset.

- **Solid Foundation**: A well-thought-out design lays a solid foundation capable of supporting future features and accommodating user growth.

In summary, careful system design is essential for long-term success and adaptability.



