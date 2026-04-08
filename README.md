# Conversational AI Evaluation Environment

##  Overview
This project simulates real-world customer support scenarios and evaluates AI responses.

##  Problem
AI systems lack realistic evaluation environments for customer support tasks.

##  Solution
We built an OpenEnv-based environment that:
- Simulates real-world queries
- Evaluates responses using scoring logic
- Provides feedback and reward

##  Features
- Easy, Medium, Hard tasks
- Real-world inspired queries
- Reward system (0 to 1 scoring)
- Feedback generation

##  How to Run

pip install -r requirements.txt  
python inference.py  

##  Example Output
Score: 0.9  
Feedback: Good response with polite tone  

##  Note
Due to API limitations, a simulated AI response is used. The system is designed to integrate with GenAI models.