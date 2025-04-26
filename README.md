# Apache Airflow Drag-and-Drop Plugin

<div style="text-align: center; margin: 30px 0;">
  <img src="https://airflow.apache.org/images/airflow-logo.png" alt="Airflow Logo" style="height: 80px; margin-bottom: 20px;">
  <h1 style="color: #007AFF; font-size: 2.5rem; margin: 10px 0;">Drag-and-Drop Plugin</h1>
  <p style="font-size: 1.2rem; color: #2C3E50;">Visual Workflow Designer for Apache Airflow</p>
</div>

<div style="background: #F8F9FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h2 style="color: #007AFF; margin-top: 0;">✨ Enhanced DAG Creation Experience</h2>
  <p>The <strong>Apache Airflow Drag-and-Drop Plugin</strong> revolutionizes workflow creation by providing an intuitive visual interface for building and managing DAGs (Directed Acyclic Graphs).</p>
</div>

## Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h3 style="color: #007AFF;">🖱️ Drag-and-Drop Interface</h3>
  <p>Intuitively design workflows by dragging operators onto the canvas and connecting them visually.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h3 style="color: #007AFF;">📋 Predefined Templates</h3>
  <p>Accelerate development with templates for common workflow patterns and use cases.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h3 style="color: #007AFF;">⚙️ Custom Operators</h3>
  <p>Extend the visual palette with your organization's custom operators.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h3 style="color: #007AFF;">✅ Real-Time Validation</h3>
  <p>Get immediate feedback on your workflow's validity before deployment.</p>
</div>

<div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <h3 style="color: #007AFF;">💾 Export DAG Code</h3>
  <p>Seamlessly convert visual workflows to Python code with one click.</p>
</div>

</div>

## Installation Guide

### Standard Airflow Installation

```bash
pip install apache-airflow-dragdrop-plugin
airflow webserver --reload
airflow scheduler --daemon

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
```
1️⃣ Open the Drag-and-Drop Interface : Navigate to the "Drag-and-Drop" tab in the Airflow UI. 

2️⃣ Add Nodes : Drag operators onto the canvas and connect them. 

3️⃣ Configure Nodes : Click on each node to set its properties. 

4️⃣ Validate and Save : Ensure your workflow is error-free and save it as a DAG.
```

### 🔄 Exporting and Importing Workflows

- **Export**: Click "Export" to save your DAG as a Python file.
---

## Contributing 🤝

We welcome contributions! Follow these steps: 
1️⃣ **Fork the repository** 
2️⃣ **Create a new branch** for your feature or bugfix. 
3️⃣ **Submit a pull request** with a detailed description.

---

## License 📜

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

## Support 🆘

If you encounter any issues or have questions, please **open an issue** on our GitHub repository.

## Acknowledgments 🙏

Special thanks to the **Apache Airflow community** for their support and inspiration.

---

🌎 Connect with Us

akshay.thakare031@gmail.com 
https://www.linkedin.com/in/akshaythakare3

---

🚀 **Happy Workflow Building!** 🚀
