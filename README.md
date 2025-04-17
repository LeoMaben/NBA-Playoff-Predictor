# NBA-Playoff-Predictor

Goal of this project is to predict the winner of the 
2025 Playoffs since the regular season has now ended.

## Tools & Technologies

- Programming Language: Python 
- Data Collection: nba_api, pandas, requests 
- Data Storage: Postgres or CSV files 
- Machine Learning Libraries: scikit-learn, xgboost 
- Model Persistence: joblib / mlflow? 
- Dashboarding: Streamlit 
- Containerization: Docker 
- Version Control & CI/CD: git, GitHub Actions 
- Testing: pytest

## Roadmap:

### 1) Project Setup
- Create GitHub repo: nba-playoff-winner-predictor
- Set up virtual environment (Poetry or venv)
- Install dependencies: nba_api, pandas, scikit-learn, streamlit, xgboost, matplotlib, joblib
- Create folder structure

### 2) Data Collection & Preprocessing
- Use nba_api to:
- Save data as playoff_teams_2025.csv or in DB 
- Engineer features for each team (normalize if needed)
- Label previous years' champions (for supervised learning)

### 3) Model Development
- Build initial model  
  - Train an XGBoostClassifier or RandomForestClassifier 
  - Inputs: team stats
  - Output: probability of being the final winner 
- Use matchups to simulate brackets (up to finals)
- Save model with joblib

### 4) App Dashboard
- Build app.py 
  - Dropdown to select team matchups 
  - Display team stats 
  - Button to “Simulate Playoffs” 
  - Show predicted winner with probability
- Add visualizations with matplotlib or seaborn

### 5) Dockerize, Test and Push
- Docker container for the project
- Testing of exisiting code
- Git repo