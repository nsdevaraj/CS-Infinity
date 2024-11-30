

#### **1. Basics of Docker**

- **What is Docker and its architecture?**
- Differences between **Docker** and **Virtual Machines (VMs)**.
- **Containers vs Images**: Understanding the concepts.
- Installation and setup of Docker on various platforms.



### **1. Basics of Docker**

#### **What is Docker and its Architecture?**

Docker is a platform that enables **containerization**, allowing applications to run in isolated environments. It uses the **Docker Engine** to manage and run containers.

**Architecture Components**:

1. **Docker Client**: CLI for interacting with Docker.
2. **Docker Daemon**: Core service that runs on the host, manages containers, images, volumes, and networks.
3. **Images**: Templates for creating containers.
4. **Containers**: Runtime instances of images.
5. **Docker Registry**: Stores Docker images (e.g., Docker Hub).

---

**Interview Q&A**:

- **Q: What is Docker?** A: Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers.
    
- **Q: What are the main components of Docker architecture?** A: Docker Client, Docker Daemon, Images, Containers, and Docker Registry.
    
- **Q: How does Docker differ from a traditional hypervisor-based system?** A: Unlike hypervisors, Docker containers share the host OS kernel, making them lightweight and faster to start.
    

---

#### **Differences Between Docker and Virtual Machines (VMs)**

|Feature|Docker|Virtual Machines|
|---|---|---|
|**Isolation**|Uses containers|Uses full OS virtualization|
|**Performance**|Lightweight and fast|Resource-heavy and slower|
|**Resource Usage**|Shares host kernel|Requires full OS for each VM|
|**Start-up Time**|Seconds|Minutes|
|**Size**|MBs (container size)|GBs (VM disk size)|

---

**Interview Q&A**:

- **Q: Why is Docker faster than VMs?** A: Docker containers share the host OS kernel, avoiding the overhead of starting a full operating system like in VMs.
    
- **Q: Can you explain the difference between Docker and VMs?** A: Docker uses containerization with shared OS kernel, while VMs virtualize the hardware, requiring separate OS instances.
    

---

#### **Containers vs Images**

|Aspect|Containers|Images|
|---|---|---|
|**Definition**|Running instance of an image|Blueprint for containers|
|**State**|Stateful|Stateless|
|**Mutability**|Mutable|Immutable|
|**Use Case**|Executes applications|Used to create containers|

---

**Interview Q&A**:

- **Q: What is the difference between an image and a container?** A: An image is a read-only template for creating containers, while a container is the running instance of an image.
    
- **Q: Can containers share the same image?** A: Yes, multiple containers can be created from the same image.
    

---

#### **Installation and Setup of Docker**

1. **Installation Steps**:
    
    - Install Docker Engine using the package manager (`apt` for Ubuntu, `brew` for macOS, or `.msi` for Windows).
    - Verify installation: `docker --version`.
    - Start the Docker daemon.
2. **Post-installation**:
    
    - Add your user to the `docker` group to avoid using `sudo`.
    - Test by running: `docker run hello-world`.

---

**Interview Q&A**:

- **Q: How do you verify if Docker is installed and running?** A: Use `docker --version` to check the installation and `docker ps` to confirm the daemon is running.
    
- **Q: What is the command to test Docker after installation?** A: `docker run hello-world`.

