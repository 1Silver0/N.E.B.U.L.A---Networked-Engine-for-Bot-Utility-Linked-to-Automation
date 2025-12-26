### N.E.B.U.L.A.

## This is a small Python project I’m building to practice real-world programming and because I’ve always thought Discord bots were "cool".

# Current focus:

**Input → processing → output**

**Persistent storage with SQLite**

**Clean embed output**

****I’m sharing this to get feedback and improve.****

# How to run N.E.B.U.L.A.

**Install dependencies**
Install all required packages using:
pip install -r requirements.txt

**Set up bot token**
Open NebulaV1.2_Main.py
Find the line that looks like:
TOKEN = "YOUR_BOT_TOKEN"
Replace "YOUR_BOT_TOKEN" with your actual Discord bot token
Run the bot normally
Start the bot by running:
python NebulaV1.2_Main.py

**Run the bot with Docker**
Save the following Dockerfile in the root of your project:
FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "NebulaV1.2_Main.py"]
Then build and run the Docker container:
docker build -t nebula-bot
docker run nebula-bot

**Database files**
Make sure the .db and .json files in the database/ folder are present

**Enjoy!**
Invite your bot to a Discord server and test the commands
