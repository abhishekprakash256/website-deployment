# **Deployment Guide: Personal Portfolio Website on AWS**

---

## **Target IP Address**

> **IP Address:** `3.128.143.84`
> ** Important:** Do **NOT** release or change this IP.
> It is linked to your **GoDaddy DNS / Hosting console**.

---

##  **AWS Instance Configuration**

### **Instance Type**

* Use: `t3.xlarge` (for deployment and build)
* After deployment, you may scale down to: `t2.small` (to reduce cost)

### **Operating System**

* **Ubuntu (latest stable version)**

### **Storage**

* **Disk space:** Minimum **20 GB**

  * Required due to build artifacts and future development growth.

### **Network and Security**

Allow the following inbound connections:

* **HTTP (80)**
* **HTTPS (443)**
* **SSH (22)**

### **SSH Key**

* **Use:** `abhi key` in AWS console

---

##  **Deployment and Rollback Commands**

### **Deploy**

```bash
ansible-playbook -i inventory.ini ansible/deploy.yml -vvv
```


### **Note**

- For Testing and Checking a service don't reset the nginx certs as that are limited and comment the steps in nginx.yml in provsion steps 
- In the rollback-provsion-steps as well the file -> rollback-nginx.yml
- if there is no change into the nginx conf just commnet in the deploy and rollback as well 

### **Rollback**

```bash
ansible-playbook -i inventory.ini ansible/rollback.yml -vvv
```

---

## 🐳 **Docker Setup and Service Configuration**

### **Ports Used by Services**

| Service    | Port Mapping |
| ---------- | ------------ |
| Redis      | 6379:6379    |
| MongoDB    | 27017:27017  |
| PostgreSQL | 5432:5432    |
| Typesense  | 8108:8108    |

---

##  **Install Docker on Ubuntu**

```bash
# Update system and install dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl

# Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine and components
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

## 👥 **Run Docker Without `sudo`**

```bash
sudo groupadd docker
sudo gpasswd -a $USER docker
```

Then log out and log back in for changes to take effect.

---

##  **Create Docker Network**

```bash
docker network create my_network
```

---

##  **Run Service Containers**

### **Redis**

```bash
docker run -d --name redis --network my_network -p 6379:6379 redis:latest
```

### **MongoDB**

```bash
docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest
```

### **PostgreSQL**

```bash
docker run -d --name postgres-container \
  -e POSTGRES_USER=abhi \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=test_db \
  -p 5432:5432 \
  postgres
```

### **Typesense**

```bash
docker run -d \
  --name typesense \
  --network my_network \
  -p 8108:8108 \
  -v $(pwd)/typesense-data:/data \
  typesense/typesense:29.0.rc30 \
  --data-dir /data \
  --api-key=$TYPESENSE_API_KEY \
  --enable-cors
```

---

##  **Docker Compose (Optional Shortcut)**

You can use Docker Compose to simplify service management.

### **Start All Containers**

```bash
docker compose up -d
```

### **Stop and Remove All Containers**

```bash
docker compose down
```

---

##  **Troubleshooting and Maintenance**

### **Restarting Blog Service (if it goes down after reboot)**

```bash
sudo systemctl restart blog-service
```

### **Check Running Containers**

```bash
docker ps
```

### **View Container Logs**

```bash
docker logs <container_name>
```

---

##  **Post-Deployment Scaling**

After successful deployment and verification:

* Scale down the instance type to **t2.small** for cost efficiency.

---

##  **Summary Checklist**

| Step | Description                                   | Status |
| ---- | --------------------------------------------- | ------ |
| 1    | Create EC2 instance (t3.xlarge, Ubuntu, 20GB) | ☐      |
| 2    | Open ports 22, 80, 443                        | ☐      |
| 3    | SSH using `abhi key`                          | ☐      |
| 4    | Install Docker & Ansible                      | ☐      |
| 5    | Run Docker containers                         | ☐      |
| 6    | Deploy via `ansible-playbook`                 | ☐      |
| 7    | Verify services                               | ☐      |
| 8    | Scale down to `t2.small`                      | ☐      |

---




##  **Nginx and SSL Setup**

### **1. Install Nginx**

```bash
sudo apt install nginx -y
```

---

### **2. Install Certbot (for SSL Certificates)**

```bash
sudo apt install certbot python3-certbot-nginx -y
```

---

### **3. Obtain SSL Certificate**

Run the following to automatically issue an SSL certificate for your domain:

```bash
sudo certbot certonly --non-interactive --nginx --agree-tos \
--email abhishekprakash47@gmail.com -d meabhi.me

sudo certbot certonly --non-interactive --nginx --agree-tos \
--email abhishekprakash47@gmail.com -d api.meabhi.me
```

> **Note:**
>
> * Replace `meabhi.me` if you’re deploying to a different domain.
> * Certbot will verify the domain via Nginx and save certificates in `/etc/letsencrypt/live/meabhi.me/`.
> * Certbot will verify the domain via Nginx and save certificates in `/etc/letsencrypt/live/api.meabhi.me/`.

---

### **4. Place Nginx Configuration File**

1. Copy your site’s config file to:

   ```
   /etc/nginx/sites-available/
   ```

2. Enable it by creating a symbolic link:

   ```bash
   sudo ln -s /etc/nginx/sites-available/<your_config_file> /etc/nginx/sites-enabled/
   ```

3. (Optional) Remove the default config if not needed:

   ```bash
   sudo rm /etc/nginx/sites-enabled/default
   ```

---

### **5. Test Nginx Configuration**

```bash
sudo nginx -t
```

> This checks for syntax errors or invalid paths.

---

### **6. Reload Nginx**

```bash
sudo systemctl reload nginx.service
```

### **6. Restart Nginx**

```bash
sudo systemctl restart nginx.service
```


### For Testing in Niginx --> 

```bash

#remove the default file in both /etc/nginx/sites-available and /etc/nginx/sites-enabled
#make the new default file in both location
#restart nginx

sudo vi default
sudo rm default

sudo nginx -t             
sudo systemctl restart nginx

```

---

### **7. Verify SSL**

After reloading, visit:

```
https://meabhi.me
```

### Setup of the ports and service running

The ports -

- nextjs front end - 3000
- tiny-url service - 5050
- static-media-server - 8080
- chat server - 8050
- blog-service -5000
- academic-webiste - 5100

### Debug commands --> 

```bash
#active the virtual env
source /home/ubuntu/.venvs/global/bin/activate


#to check any sevrice replace the service name 
sudo systemctl daemon-reload
sudo systemctl enable personal-portfolio-frontend.  #replace the service name 
sudo systemctl start personal-portfolio-frontend
sudo systemctl status personal-portfolio-frontend


#check the status of the services running in the system
systemctl list-units --type=service --all
systemctl list-units --type=service
systemctl --failed
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service
ss -tulpn.  #scan all services running on the ports
ps aux
ss -tpn     #check the out connections
sudo systemctl list-timers       #list the services timers 


```


### UFW commands --> 

```bash

# Reset any existing rules (optional but clean)
sudo ufw reset

# Set secure defaults
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow and rate-limit SSH (prevents brute-force)
sudo ufw limit ssh

# Allow web traffic
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

#allow the logging 
sudo ufw logging medium

# Enable firewall
sudo ufw enable

# Verify status
sudo ufw status verbose

```


### UFW help commands ---> 

```bash

sudo ufw status numbered
sudo ufw status verbose
sudo ufw reload
sudo ufw delete <rule_number>
sudo ufw reload
sudo ufw disable
sudo ufw logging on
sudo ufw app list
sudo ufw show added

```



## Notes
- For the Cors debug use these 

Not need to activate cors in both server and nginx one can work prefer nginx doing the cors

- After the deployment restart the blog-service with systemctl command 

### Debug Commnads --> 

```bash
curl -i -X OPTIONS http://127.0.0.1:5050/tu/v1/url/submit \
  -H "Origin: https://www.meabhi.me" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: content-type"



curl -i -X OPTIONS https://api.meabhi.me/tu/v1/url/submit \
  -H "Origin: https://www.meabhi.me" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: content-type"

```


## For the static files --> **⚠️ Important:**

They are managed through the ansible/files folder , this folder is in gdrive as well 
ansible copy the file into the machine in static-media-server 

The test_data.json is used to injest the data into MongoDb
