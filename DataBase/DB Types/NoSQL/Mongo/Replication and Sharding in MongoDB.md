

### 4. Replication and Sharding in MongoDB

Replication and sharding are two key MongoDB features for ensuring high availability and horizontal scalability.

---

#### Replication

Replication involves copying data across multiple servers to improve availability, data redundancy, and fault tolerance.

- **Replica Set**: A group of MongoDB servers (nodes) that maintain the same data set through replication.
  - **Primary Node**: The main node that receives all write operations. Reads can also be directed here.
  - **Secondary Nodes**: Nodes that replicate data from the primary node. Can serve as read replicas to distribute read load.
  - **Arbiter**: A lightweight node that participates in voting to elect a primary but does not store data. Useful in small deployments to maintain odd numbers in the replica set.

- **Failover**: If the primary node fails, an election is triggered to promote a secondary node to primary, ensuring high availability.

- **Replication Example**:
  ```bash
  rs.initiate()  // Initialize a replica set
  db.collection.insertOne({ name: "Alice", age: 25 });  // Write to primary; data replicates to secondaries
  ```

---

#### Sharding

Sharding is MongoDB’s method for horizontal scaling, dividing data across multiple servers to handle large datasets and high-throughput applications.

- **Shard**: A single server or replica set that holds a subset of the data. Together, all shards form a distributed database.
- **Shard Key**: A field (or fields) that determines data distribution across shards.
- **Chunks**: MongoDB splits data into chunks and assigns each chunk to a shard based on the shard key. As data grows, chunks are balanced across shards.

- **Components**:
  - **Config Servers**: Store metadata about the cluster and manage data distribution across shards.
  - **Query Routers (mongos)**: Act as middleware to route client requests to the appropriate shard based on the shard key.

- **Sharding Example**:
  ```bash
  sh.enableSharding("myDatabase")  // Enable sharding on a database
  sh.shardCollection("myDatabase.myCollection", { user_id: "hashed" })  // Define shard key
  ```

---

### Interview Questions and Answers

**Q1. What is a replica set, and why is it used in MongoDB?**  
- **Answer**: A replica set is a group of MongoDB nodes that replicate data for high availability, fault tolerance, and read scalability. Replica sets ensure data is available even if the primary node fails, and they can distribute read load across secondary nodes.

**Q2. How does MongoDB handle primary node failure in a replica set?**  
- **Answer**: If the primary node fails, an election process is initiated among the remaining nodes. A secondary node is elected as the new primary, allowing operations to continue with minimal downtime.

**Q3. What is sharding, and when would you use it?**  
- **Answer**: Sharding is the process of distributing data across multiple servers or shards. It is used when a single server cannot handle the load or data volume, allowing MongoDB to horizontally scale by distributing data and queries across shards.

**Q4. What is a shard key, and why is it important?**  
- **Answer**: A shard key is a field that determines how data is distributed across shards. It is essential to choose an effective shard key to ensure data is evenly distributed and avoid hot spots (uneven load distribution across shards).

**Q5. How do config servers and query routers work in a sharded cluster?**  
- **Answer**: Config servers store metadata about data distribution across shards, while query routers (mongos) direct client queries to the correct shard based on the shard key. Config servers ensure consistent and balanced distribution, while query routers manage client interaction with the sharded cluster.


