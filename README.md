# PRD Improver - AI-Powered PRD Analysis System

An intelligent, multi-agent system designed to analyze and improve Product Requirement Documents (PRDs). Utilizing Groq's LLaMA 3.3 model (or Gemma 2.1 model) and Streamlit, it provides actionable insights, persona-specific feedback, and a collaborative platform for PRD enhancement.

---

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
  - [Manual Server Deployment](#manual-server-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features
- **Multi-Agent Collaboration**: Dedicated AI agents analyze PRDs with specialized roles to cover all aspects of improvement.
- **Persona-Focused Feedback**: Generates feedback tailored to key personas, such as developers, designers, and stakeholders.
- **Collaborative Discussion Synthesis**: Combines input from agents to provide a holistic summary of PRD improvements.
- **Comprehensive Recommendations**: Offers actionable insights, including clarity improvements, gap identification, and optimization suggestions.
- **Interactive User Interface**: Built with Streamlit, featuring intuitive navigation and an easy-to-use dashboard.
- **Advanced Model Integration**: Seamlessly integrates with Groq's LLaMA 3.3 model or Gemma 2.1 model for enhanced natural language understanding.

---

## 🚀 Installation

### Local Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/prd-improver.git
   cd prd-improver
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   ```bash
   cp .env.example .env
   # Open .env and add your Groq API key
   ```

### Docker Setup

1. **Build the Docker Image:**
   ```bash
   docker build -t prd-improver .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 8501:8501 --env-file .env prd-improver
   ```

---

## 💻 Usage

1. **Start the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the App in Your Browser:**
   Navigate to `http://localhost:8501`

3. **Provide Authentication:**
   Enter your Groq API key in the sidebar (if not pre-configured in the `.env` file).

4. **Analyze PRD:**
   - Paste your PRD text into the input field.
   - Click "Analyze PRD" to initiate analysis.

5. **Explore Results:**
   - **Team Feedback Tab:** View specialized feedback from multiple perspectives.
   - **Persona Analysis Tab:** Understand insights tailored to personas.
   - **Discussion Summary Tab:** Explore synthesized recommendations from all agents.
   - **Recommendations Tab:** Access actionable suggestions to refine your PRD.

---

## 📦 Deployment

### Streamlit Cloud Deployment

1. Push your code to GitHub.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click **"New App"** and select your repository and branch.
4. Set the main file path as `app.py`.
5. Add environment variables (e.g., `GROQ_API_KEY`) under app settings.
6. Deploy the app with a single click.

### Manual Server Deployment

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/prd-improver.git
   ```

2. **Set Up Environment Variables:**
   ```bash
   cp .env.example .env
   # Add necessary keys to the .env file
   ```

3. **Install Dependencies and Run the App:**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py --server.port 80 --server.address 0.0.0.0
   ```

---

## 🤝 Contributing

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request and describe your changes.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project for both personal and commercial purposes.

For more details, see the [LICENSE](LICENSE) file in the repository.

---
