MindMate MCP Server – “Your Mindful Companion”

MindMate is a lightweight AI-powered wellness companion designed to help users reduce stress, prevent burnout, and practice daily mindfulness.
It provides short, supportive responses such as motivational quotes, relaxation tips, and reflection prompts.

This project is implemented as an MCP (Model Context Protocol) server, making its tools accessible to compatible AI clients such as Claude Desktop.

#Project Overview

MindMate supports three core well-being functions:

1-Motivational Quotes

Returns an uplifting quote depending on the user’s emotional state.
Example → "stressed" → returns an anti-stress motivational quote.

2-Mindfulness Activities

Suggests a quick, practical relaxation activity such as breathing, grounding, or stretching.

3-Daily Reflection Prompt

Provides a short gratitude or self-awareness question to promote mindful habits.

All content is sourced from local JSON files. No external APIs are required.

#Project Structure
mindmate-mcp/
│

├── mcp_server/

│   ├── app.py

│   ├── Dockerfile

│   ├── requirements.txt

│   ├── data/

│   │   ├── quotes.json

│   │   ├── activities.json

│   │   └── prompts.json

│   └── schemas.py

│

└── README.md

Running Locally with Docker
1-Build the Docker image

Inside the mcp_server directory:

docker build --no-cache -t mindmate-mcp:local .

2-Run the image
docker run --rm -p 8000:8000 mindmate-mcp:local


Expected logs:

INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000


Stop with CTRL + C.

#(Optional) Push Image to Docker Hub
docker tag mindmate-mcp:local DOCKERUSERNAME/mindmate-mcp:latest
docker push DOCKERUSERNAME/mindmate-mcp:latest


Replace nakata3 with your own DockerHub username.

#MCP Tools
getMotivationalQuote(emotion: str) → dict

Returns a quote matching the emotional category.

suggestMindfulnessActivity(emotion: str) → dict

Suggests a mindfulness activity.

dailyReflectionPrompt() → dict

Returns a daily reflection / gratitude prompt.

💻 Claude Desktop Integration
Using Docker

Place under:

Windows: %APPDATA%\Claude\claude_desktop_config.json

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

{
  "mcpServers": {
    "mindmate": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "DOCKERUSERNAME/mindmate-mcp:latest"
      ]
    }
  }
}

Using Python directly
{
  "mcpServers": {
    "mindmate": {
      "command": "python",
      "args": [
        "C:/path/to/mindmate-mcp/mcp_server/app.py"
      ]
    }
  }
}

Team Roles



Can Atakan - MCP Developer
-

Designed the overall MindMate concept and implemented the MCP server (tools, JSON loading, core logic). Set up containerization (Dockerfile, requirements), built and pushed the Docker image to Docker Hub, and verified container execution.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tiziano Visconti - Data & Content Designer
-

Created and curated the wellness content in quotes.json, activities.json, and prompts.json, including emotion categories and tone.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Laudecene Sippel Lemos - Claude Integration
-

Configured MindMate as a local MCP server in Claude Desktop, and validated end-to-end flows.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Jeanne Voisard - Tester
-

Tested Claude tool calls from the chat interface on the local environment.

Daria Chaiun – Documentation & Reporting
-

 Wrote and structured the README and project documentation, including setup steps, usage instructions, and team role descriptions.
