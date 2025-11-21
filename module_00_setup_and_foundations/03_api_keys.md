# 0.3 API Key Management 🔑

Agents need access to LLMs, and that usually means API keys. **Never commit your API keys to GitHub!**

## 🛡️ The `.env` File Pattern

We will use the `python-dotenv` library to load our keys from a local file that is ignored by Git.

### Step 1: Create a `.env` file
In the root of your project (or inside this module's folder), create a file named `.env`.

```bash
touch .env
```

### Step 2: Add your Keys
Open `.env` and add your keys like this:

```env
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
SERPER_API_KEY=... # For Google Search tool later
```

### Step 3: Update `.gitignore`
Ensure your `.gitignore` file includes `.env`.

```text
# .gitignore
.env
venv/
__pycache__/
```

### Step 4: Loading Keys in Python

Here is how you load these keys in your scripts:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the key
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    print("Error: OPENAI_API_KEY not found. Please check your .env file.")
else:
    print("Successfully loaded API key!")
```

## 💰 Cost Control
*   **Set Limits**: Most providers (OpenAI, Anthropic) allow you to set monthly spend limits. Set a low limit (e.g., $5-$10) when starting out.
*   **Monitor Usage**: Check your dashboard regularly. Agents can make many calls in a loop!

You are now set up and secure! 🔒
