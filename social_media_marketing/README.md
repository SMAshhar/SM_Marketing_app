# SocialMediaMarketing Crew

Welcome to the SocialMediaMarketing Crew project, powered by [crewAI](https://crewai.com). This t   emplate is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

# Agentic AI-Powered Social Media Marketing App

## Overview
The **Agentic AI-powered Social Media Marketing App** is a desktop application that automates social media content creation and scheduling. Using an **agentic system powered by  [CrewAI](https://crewai.com)**, this app analyzes businesses, conducts market research, and generates optimized social media posts.

## Key Features
- **Business Analysis & Market Research** (One-time per client)
- **Automated Social Media Post Generation** (Recurring for weeks)
- **Custom AI-Generated Images**
- **Multi-Platform Optimization** (LinkedIn, X/Twitter, Facebook, etc.)
- **Post Scheduling for Engagement Optimization**

---

## Workflow
The application is structured into three agentic subsystems:

### **1. Business Analysis Agents (One-time per Client)**
- Extracts key business details like mission, products, services, tone, and branding.
- Outputs structured data to be used for content generation.

**Agents:**
- **Business Profiler:** Analyzes the company’s website and documents to understand its offerings.
- **Brand Identity Expert:** Defines brand voice, messaging style, and values.
- **Target Market Analyzer:** Identifies ideal customers, their preferences, and key demographics.

### **2. Market Research Agents (One-time per Client)**
- Studies industry trends, competitors, and audience behavior.
- Provides strategic insights for post optimization.

**Agents:**
- **Competitor Analyst:** Monitors social media activities of competitors.
- **Industry Trend Tracker:** Analyzes trending topics in the client’s industry.
- **Engagement Strategist:** Studies what type of content performs best.

### **3. Content Generation Agents (Recurring, Based on Analysis Data)**
- Uses business and market research insights to generate high-quality posts.
- Creates **platform-specific** posts for LinkedIn, Facebook, and X/Twitter.
- Generates **custom images** with AI (DALL·E API).

**Agents:**
- **Content Strategist:** Crafts social media posts tailored to each platform.
- **Visual Content Generator:** Uses AI to generate relevant images.
- **Post Scheduler:** Schedules posts for maximum engagement.

### **Example Output Format (JSON)**
```json
{
  "facebook_post": "A post tailored for Facebook",
  "linkedin_post": "A post tailored for LinkedIn",
  "x_post": "A post tailored for X/Twitter",
  "url_from_DALL-E": "https://image-generated-url.com"
}
```

---

## Installation & Usage
### **Requirements**
- Python 3.9+
- CrewAI
- FastAPI
- OpenAI API (for DALL·E & LLMs)

### **Setup**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/agentic-social-media-app.git
   cd agentic-social-media-app
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

---

## Future Enhancements
- **Multi-Client Support**
- **Integration with Social Media APIs for Direct Posting**
- **Performance Analytics on Engagement & Reach**
- **More AI Models for Image & Video Generation**

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
MIT License


First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY`, `GEMINI_API_KEY` and `MODEL_NAME` into the `.env` file**

- Modify `src/social_media_marketing/config/agents.yaml` to define your agents
- Modify `src/social_media_marketing/config/tasks.yaml` to define your tasks
- Modify `src/social_media_marketing/crew.py` to add your own logic, tools and specific args
- Modify `src/social_media_marketing/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the social_media_marketing Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The social_media_marketing Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the SocialMediaMarketing Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


# Docmentation for Crew:

## Agents & Roles:
### Business Analyst – Extracts key insights from the website/document.

    Tools: Web scraper, NLP summarization, document parser.

### Market Researcher – Identifies the target audience and trends.

    Tools: Web search, competitor analysis, audience analytics API.

### Content Strategist – Crafts tailored posts for each platform.

    Tools: LLM for text, DALL·E for images, video API.

### Scheduler – Determines optimal posting times.

    Tools: Engagement analytics API, historical post data analysis.

### Publisher – Posts content using the provided API keys.

    Tools: Social media API integrations.

### Engagement Monitor – Tracks responses and gathers insights.

    Tools: Sentiment analysis, chatbot integration.


# Backend Architecture
FastAPI for API endpoints to handle requests and agent coordination.

CrewAI to manage the agentic workflow.

PostgreSQL or Neon DB to store user data, post schedules, and analytics.

Langchain for LLM-powered text generation and retrieval.

Social Media APIs (Facebook, LinkedIn, Twitter, etc.) for posting.

Celery/Background Scheduler for scheduled post execution.

# User Interface (Desktop App)
### Tech Stack:

- Electron.js (if web-based) or Tauri (for a lightweight Rust-backed app).

- Next.js + TailwindCSS for a sleek, responsive UI.

## Key UI Features
- Onboarding Screen: Upload website/doc & enter social media API keys.

- Dashboard: Overview of posts, engagement metrics, and recommendations.

- Content Editor: Allows manual editing of AI-generated posts.

- Scheduler View: Calendar with suggested posting times.

- Analytics Panel: Engagement insights and feedback loop.