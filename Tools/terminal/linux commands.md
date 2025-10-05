
Here’s a list of commonly used **Linux terminal commands**, simplified for quick reference:

---

### 📁 **File & Directory Operations**

|Command|Description|
|---|---|
|`ls`|List files and directories|
|`ls -la`|List all (including hidden) with details|
|`cd folder_name`|Change directory|
|`cd ..`|Go up one directory|
|`pwd`|Show current directory path|
|`mkdir new_folder`|Create new directory|
|`rm file.txt`|Delete file|
|`rm -r folder_name`|Delete folder and its contents|
|`touch file.txt`|Create empty file|
|`cp file1.txt file2.txt`|Copy file|
|`mv old.txt new.txt`|Rename or move file|
|`cat file.txt`|View file content|
|`nano file.txt`|Edit file (simple editor)|
|`clear`|Clear terminal screen|

---

### 🛠️ **System Info**

|Command|Description|
|---|---|
|`whoami`|Show current user|
|`uname -a`|Show system info|
|`df -h`|Show disk usage|
|`top` or `htop`|Show running processes|
|`ps aux`|List all processes|
|`free -h`|Show memory usage|

---

### 🔍 **Search & Find**

|Command|Description|
|---|---|
|`find . -name "file.txt"`|Find file by name|
|`grep "text" file.txt`|Search for text in file|
|`grep -r "text" .`|Recursively search in current directory|

---

### 🔄 **Package Management (Debian/Ubuntu)**

|Command|Description|
|---|---|
|`sudo apt update`|Update package list|
|`sudo apt upgrade`|Upgrade installed packages|
|`sudo apt install package_name`|Install package|
|`sudo apt remove package_name`|Remove package|

---

### 🔐 **Permissions**

|Command|Description|
|---|---|
|`chmod +x file.sh`|Make file executable|
|`chown user:group file.txt`|Change file owner|

---

### 📦 **Archive & Compression**

|Command|Description|
|---|---|
|`tar -czf archive.tar.gz folder/`|Compress folder to `.tar.gz`|
|`tar -xzf archive.tar.gz`|Extract `.tar.gz`|
|`zip -r file.zip folder/`|Zip folder|
|`unzip file.zip`|Unzip file|

---

### 🌐 **Networking**

|Command|Description|
|---|---|
|`ping google.com`|Check internet connectivity|
|`curl https://example.com`|Fetch content from URL|
|`ifconfig` or `ip a`|Show IP addresses|
|`netstat -tuln`|Show open ports|

---
