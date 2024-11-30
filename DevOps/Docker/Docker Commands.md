



#### **2. Docker Commands**

- Basic commands:
    - `docker run`, `docker ps`, `docker stop`, `docker rm`
- Managing images:
    - `docker pull`, `docker build`, `docker images`, `docker rmi`
- Container lifecycle:
    - `docker start`, `docker exec`, `docker logs`
- Docker volumes and networking commands.



### **2. Docker Commands**

#### **Basic Commands**

1. **`docker run`**  
    Starts a container from an image. If the image isn't available locally, it pulls it from Docker Hub.  
    Syntax:
    
    ```
    docker run [OPTIONS] IMAGE [COMMAND]
    ```
    
    Example:
    
    ```
    docker run -it ubuntu bash
    ```
    
    - `-it`: Interactive mode with a terminal.
    - `ubuntu`: Image name.
    - `bash`: Command to execute.
2. **`docker ps`**  
    Lists running containers.  
    Syntax:
    
    ```
    docker ps [OPTIONS]
    ```
    
    Example:
    
    ```
    docker ps -a  # Lists all containers, including stopped ones
    ```
    
3. **`docker stop`**  
    Stops a running container.  
    Syntax:
    
    ```
    docker stop [CONTAINER_ID/NAME]
    ```
    
4. **`docker rm`**  
    Removes stopped containers.  
    Syntax:
    
    ```
    docker rm [CONTAINER_ID/NAME]
    ```
    
    Example:
    
    ```
    docker rm $(docker ps -aq)  # Removes all stopped containers
    ```
    

---

**Interview Q&A**:

- **Q: What happens if you run `docker run` with an image that doesn't exist locally?**  
    A: Docker automatically pulls the image from the Docker registry (e.g., Docker Hub).
    
- **Q: How do you list stopped containers?**  
    A: Use `docker ps -a`.
    

---

#### **Managing Images**

1. **`docker pull`**  
    Pulls an image from a registry (e.g., Docker Hub).  
    Syntax:
    
    ```
    docker pull [IMAGE]
    ```
    
    Example:
    
    ```
    docker pull nginx
    ```
    
2. **`docker build`**  
    Builds an image from a Dockerfile.  
    Syntax:
    
    ```
    docker build -t [TAG] [PATH]
    ```
    
    Example:
    
    ```
    docker build -t my-image .
    ```
    
3. **`docker images`**  
    Lists all images stored locally.  
    Syntax:
    
    ```
    docker images
    ```
    
4. **`docker rmi`**  
    Removes unused or specific images.  
    Syntax:
    
    ```
    docker rmi [IMAGE_ID/NAME]
    ```
    
    Example:
    
    ```
    docker rmi $(docker images -q)  # Deletes all images
    ```
    

---

**Interview Q&A**:

- **Q: How do you tag an image during a build process?**  
    A: Use the `-t` option with `docker build`, e.g., `docker build -t my-image .`.
    
- **Q: How do you clean up dangling images?**  
    A: Use `docker rmi $(docker images -f dangling=true -q)`.
    

---

#### **Container Lifecycle**

1. **`docker start`**  
    Restarts a stopped container.  
    Syntax:
    
    ```
    docker start [CONTAINER_ID/NAME]
    ```
    
2. **`docker exec`**  
    Executes a command inside a running container.  
    Syntax:
    
    ```
    docker exec -it [CONTAINER_ID/NAME] [COMMAND]
    ```
    
    Example:
    
    ```
    docker exec -it my-container bash
    ```
    
3. **`docker logs`**  
    Retrieves logs of a container.  
    Syntax:
    
    ```
    docker logs [CONTAINER_ID/NAME]
    ```
    
    Example:
    
    ```
    docker logs -f my-container  # Follows live logs
    ```
    

---

**Interview Q&A**:

- **Q: How can you access a running container's shell?**  
    A: Use `docker exec -it [CONTAINER_ID/NAME] bash`.
    
- **Q: What is the difference between `docker start` and `docker run`?**  
    A: `docker start` restarts a stopped container, while `docker run` creates and starts a new container.
    

---

#### **Docker Volumes and Networking Commands**

1. **Volumes**:
    
    - **`docker volume create`**: Creates a volume.
        
        ```
        docker volume create my-volume
        ```
        
    - **`docker run -v`**: Mounts a volume to a container.
        
        ```
        docker run -v my-volume:/data alpine
        ```
        
    - **`docker volume inspect`**: Views details of a volume.
        
        ```
        docker volume inspect my-volume
        ```
        
2. **Networking**:
    
    - **`docker network ls`**: Lists available networks.
        
        ```
        docker network ls
        ```
        
    - **`docker network create`**: Creates a custom network.
        
        ```
        docker network create my-network
        ```
        
    - **`docker network connect`**: Connects a container to a network.
        
        ```
        docker network connect my-network my-container
        ```
        

---

**Interview Q&A**:

- **Q: How do you persist data for a Docker container?**  
    A: Use volumes by specifying `-v [VOLUME_NAME]:[CONTAINER_PATH]` in the `docker run` command.
    
- **Q: How do you connect two containers on the same network?**  
    A: Create a network with `docker network create` and use `docker network connect` to link containers.
    

---

