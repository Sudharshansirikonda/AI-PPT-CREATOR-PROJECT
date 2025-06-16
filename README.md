🧠 AI-Powered PPT Generator using Flask & Gemini API
An AI-powered web application that generates professional PowerPoint presentations from user prompts using the Gemini AI API and Flask. This tool helps students, educators, and professionals quickly create presentation decks by just entering a topic or idea.

🚀 Features
🌐 Web-based user interface built with Flask and HTML/CSS

🤖 Generates slide content using Google's Gemini API

📊 Automatically creates downloadable .pptx files using python-pptx

💡 Slide titles and bullet points are generated based on the topic

⚡ Lightweight and easy to run locally

📸 Demo
https://github.com/yourusername/ai-ppt-generator/assets/demo.gif (Add a GIF or screenshot here)

🛠️ Tech Stack
Python 3

Flask

Gemini API (via REST)

python-pptx

HTML/CSS

📂 Project Structure
csharp
Copy
Edit
ai_ppt_generator/
│
├── app.py                   # Main Flask application
├── templates/
│   └── index.html           # Frontend HTML form
├── static/
│   └── style.css            # Custom CSS styling
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
📌 How It Works
User inputs a topic or prompt on the homepage.

The app sends this prompt to the Gemini API to generate slide content.

The content is split into slides and titles using Python.

A PowerPoint presentation (.pptx) is created and sent back to the user for download.

🧪 Example Prompt
"Explain the basics of Machine Learning"

Generates slides like:

yaml
Copy
Edit
Slide 1: Introduction to Machine Learning
Slide 2: Types of Machine Learning: Supervised, Unsupervised, Reinforcement
Slide 3: Common Algorithms
Slide 4: Real-World Applications
✅ Setup Instructions
Clone this repo:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-ppt-generator.git
cd ai-ppt-generator
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your Gemini API Key
Replace 'your-gemini-api-key' in app.py with your actual API key.

Run the Flask app:

bash
Copy
Edit
python app.py
Open in browser:
http://127.0.0.1:5000

🔐 Gemini API Configuration
Make sure you have access to Gemini API from Google and your API key. If needed, refer to Google AI Studio for credentials and documentation.

🧠 Future Enhancements
Add support for image slides via AI image generation

Support for different presentation themes

Save and load past prompts and presentations

Deploy to cloud (Render/Heroku)

🤝 Contributing
Feel free to open issues or submit pull requests to improve this project.

📃 License
This project is licensed under the MIT License.

