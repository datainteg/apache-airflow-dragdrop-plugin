# Apache Airflow Drag-and-Drop Plugin 🚀

![alt text](image-1.png)


&#x20;&#x20;

The **Apache Airflow Drag-and-Drop Plugin** enhances the Apache Airflow UI by allowing users to create and manage workflows using a **drag-and-drop interface**. 

This plugin simplifies the process of creating DAGs (Directed Acyclic Graphs) by providing an intuitive visual interface. 🎉

### Features ✨

✅ **Drag-and-Drop Interface** – Easily create and modify DAGs visually. 

✅ **Predefined Templates** – Use templates for common workflows.

✅ **Custom Operators** – Extend the palette with custom operators.

✅ **Real-Time Validation** – Validate workflows before deployment. 

✅ **Export DAG Code** – Save workflows as .py file.

---

### Installation 🛠️

### 🔹 For Non-Dockerized Airflow Setup

#### 1️⃣ Install the Plugin via `pip`:

```bash
pip install apache-airflow-dragdrop-plugin
```

#### 2️⃣ Restart Airflow Services:

```bash
airflow webserver --reload
airflow scheduler --daemon
```

#### 3️⃣ Access the Plugin:

Open the Airflow UI and navigate to the **"Drag-and-Drop"** tab.

---

### 🐳 For Dockerized Airflow Setup

#### Option 1️⃣: Add the Plugin to `requirements.txt`

1. Add the following line to your `requirements.txt` file:
   ```
   apache-airflow-dragdrop-plugin
   ```
2. Rebuild your Docker image:
   ```bash
   docker-compose build -t your-image-name
   ```
3. Restart your Docker containers:
   ```bash
   docker-compose up -d
   ```

#### Option 2️⃣: Install the Plugin Directly Inside the Running Container

1. Install the plugin inside the running Airflow container:
   ```bash
   docker exec -it <container_id> pip install apache-airflow-dragdrop-plugin
   ```
2. Restart the Airflow webserver and scheduler inside the container:
   ```bash
   docker exec -it <container_id> airflow webserver --reload
   docker exec -it <container_id> airflow scheduler --daemon
   ```
3. If needed, restart the container:
   ```bash
   docker restart <container_id>
   ```

---

## Usage 🖥️

### 🚀 Creating a New Workflow

1️⃣ Open the Drag-and-Drop Interface : Navigate to the "Drag-and-Drop" tab in the Airflow UI. 

2️⃣ Add Nodes : Drag operators onto the canvas and connect them. 

3️⃣ Configure Nodes : Click on each node to set its properties. 

4️⃣ Validate and Save : Ensure your workflow is error-free and save it as a DAG.




### Contributing 

We welcome contributions! Follow these steps: 

1️⃣ **Fork the repository**

2️⃣ **Create a new branch** for your feature or bugfix. 

3️⃣ **Submit a pull request** with a detailed description.

---

### License 

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

### Support

If you encounter any issues or have questions, please **open an issue** on our GitHub repository.


### Acknowledgments 

Special thanks to the **Apache Airflow community** for their support and inspiration.

---


### Connect with Us

akshay.thakare031@gmail.com 

https://www.linkedin.com/in/akshaythakare3

```
