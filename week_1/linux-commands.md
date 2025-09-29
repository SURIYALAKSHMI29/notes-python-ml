# **Linux Commands & Concepts**

## **File & Shell Commands**

- `source ~/.filename` → read the file and executes all the commands in it in the current shell  
- `touch filename` → creates a file  
- `nano ~/.filename` → used to write content on the file  
  - if exists, opens that file, else creates one  
  - nano is a text editor that can be used inside the terminal  

---

## **SSH (Secure Shell)**

Used to connect remote Linux machine over the internet  

**1. Using password**  
- `ssh username@remote_host_IP`  
  - prompts for password; if valid, remote shell opens  

**2. Using passkey**  
- `ssh-keygen -t rsa`  
  - generates 2 keys: 1 public, 1 private  
  - private key: `~/.ssh/id_rsa` → never share  
  - public key: `~/.ssh/id_rsa.pub` → can be shared  
- `ssh-copy-id username@remote_host` → copy public key to server  
- `ssh username@remote_host_IP` → connect without password  
- Optional key creation:  
  - `ssh-keygen -t rsa -b 4096 -C "author name or email"`  
    - `-t rsa` → key type  
    - `-b 4096` → 4096-bit key (strong)  
    - `-C` → comment; helps differentiate keys in `~/.ssh/authorized_keys`  

---

## **File Transfer**

### **SCP (Secure Copy)**  
- used to copy entire file/dir from local to remote  
- `scp file.txt username@remote_host:/path/to/destination`  
- password-based → prompts for password  
- key-based → copies directly  

### **RSYNC (Remote Sync)**  
- used to copy only what’s changed; remote left unchanged  
- `rsync -avz file.txt username@remote_host:/path/to/destination`  
  - `-a` → archive mode (preserve permissions, timestamps)  
  - `-v` → verbose (show progress)  
  - `-z` → compress data during transfer  
- faster than scp; good for repeated backups  

---

## **Searching & Viewing Files**

### **find**
- search files by name, type, modified time, or size  
- `find /pathToSearch -name "*.txt"` → list all `.txt` files  
- `find /home/suriya -type f -size +10M` → only files bigger than 10 MB  

### **grep**
- search for a pattern in a file  
- `grep "pattern" fileName` → search in a file  
- `grep -r "pattern" path` → recursive search in directory  
- options:  
  - `-i` → case insensitive  
  - `-n` → show line numbers  
  - `-l` → only list file names  

### **wc (Word Count)**  
- count lines, words, characters  
- `wc filename` → all counts  
- `-l` → lines, `-w` → words, `-c` → characters, `-m` → multi-byte chars  

### **head & tail**
- `head` → first 10 lines  
- `tail` → last 10 lines  
- `head -n 20 filename` → first 20 lines  

### **less & more**
- `less` → flexible, scrollable, can go back  
- `more` → basic, cannot go back, line/page view  

---

## **System Utilities**

- `which python` → find executable path  
- `kill -9 PID` → force kill process  
- `man ls` → detailed manual  
- `ls --help` → quick help  

---

## **System Info**

### **Find Linux Distribution**
- `cat /etc/os-release`  

### **Kernel Version**
- `uname -r` → kernel release  
- `uname -a` → all info  

### **CPU Info**
- `lscpu` → architecture, cores, sockets  
- `nproc` → number of cores  

### **RAM Size**
- `free -h` → total, used, available RAM  
- `cat /proc/meminfo | grep MemTotal`  

### **Processes**
- `top` → live process view  
- `htop` → interactive  
- `ps aux` → static snapshot  

### **Sort by RAM/CPU Usage**
- `top` → press `M` (RAM), `P` (CPU)  
- `ps aux --sort=-%mem | head -10`  
- `ps aux --sort=-%cpu | head -10`  

### **GPU Info**
- `lspci | grep -i vga` → PCI devices  
- `lshw -C display`  

### **Disk Usage**
- `lsblk` → block devices  
- `df -h` → mounted filesystem usage  

### **USB Devices**
- `lsusb`  

---

## **Concepts**

- **super user (root):** full system privileges  
- **sudo:** execute command as root (safe)  
- **apt:** package manager (Debian-based)  
- **$PATH:** system executable directories  

---

## **Shell Shortcuts**

- `!!` → last command  
- `!git` → last command starting with "git"  
- `Ctrl + R` → reverse search history  
- `Tab` → autocomplete  
- `cd -` → go back to previous dir  

---

## **Redirection & Pipes**

- `>` → overwrite to file  
- `>>` → append to file  
- `<` → input from file  
- `|` → pipe output  

---

## **.bashrc File**

- Runs every time a new interactive bash shell starts  
- Can: set env vars, aliases, customize prompt  

**Example Alias:**  
- `alias ll="ls -alF"`  

**Example Env Var:**  
- `export VAR="Anneyeong"`  
- `echo $VAR`  

---

## **Linux Distribution**
- Ready-to-use OS built on Linux kernel  
- Includes kernel, libraries, pkg manager, utilities  
- Examples: Ubuntu, Fedora, Arch Linux  

---

## **CPU Concepts**
- **Sockets:** physical CPU slots  
- **Cores:** processing units  
- **Hyperthreading:** multiple threads per core  
- **Logical cores:** virtual subdivisions  
- **Hybrid arch:** P-cores & E-cores  

---

## **GPU**
- Specialized for graphics & parallel tasks  
- CPU → strong single worker  
- GPU → many light workers  

---

## **LVM (Logical Volume Manager)**
- Dynamically resize partitions & allocate disk space  

---

## **Encrypted Disks**
- Require passphrase before OS boots  
- **GRUB (bootloader):** asks for passphrase  

---

## **Linux Basics**
- Everything is a file (files, dirs, devices, processes)  
- **Permissions:** owner, group, others  
- Example: `rw-r--r--` → owner read/write, others read-only  
- **Paths:**  
  - absolute → `/` root  
  - relative → from current dir  
