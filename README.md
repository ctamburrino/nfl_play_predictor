## Problem
American Football is a strategy based game where critical offensive and defensive plays can drastically change the outcome of the game. 
Defensively, being able to predict your opponents plays and strategies can cause key stops to help limit the opponents opportunities to score. 
The two main offensive plays that are made by a team are passing plays and running plays. If the defense can predict with more accuracy when the 
offense will pass or run, they can generate formations to better stop these plays. Our AI model seeks to predict whether the next offensive play 
will be a run or pass (or specific formation) given down, distance from first down line, score differential, field position, and other factors. 
Our model will specifically look at the National Football League (NFL) teams and their previous playmaking decisions.

---

## Algorithims

Logistic Regression as a Baseline model
Gradient Boosted Trees to explore decision tree model approach
XGBoost
CatBoost
Neural Networks to explore deep learning approach
MLP
LSTM

---

## Expected Outcomes

We expect to create a play prediction model with visualized tendencies for each team or situation. Our model will be able to predict to a higher 
degree of accuracy (compared to random guessing) when a team will run or pass the ball based on the circumstances that the team is in (downs, 
distance from the 1st down, score differential, and field position, etc.).

## Instructions for Use

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git (for cloning the repository)
- Homebrew (for macOS users - needed for XGBoost OpenMP support)

### Setup Instructions

#### Clone the Repository

git clone <repository-url>

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activateYou should see `(venv)` in your terminal prompt when activated.

#### Install Dependencies

# Make sure venv is activated, then install packages
pip install --upgrade pip
pip install -r requirements.txt

**Note for macOS users:** XGBoost requires OpenMP. 
Install it with: brew install libomp

# With venv activated
pip install ipykernel
python -m ipykernel install --user --name=nfl_play_predictor --display-name "Python (nfl_play_predictor)"Then in VS Code/Cursor, select the kernel: `Python (nfl_play_predictor`

### Dataset Setup

**Important:** The original dataset is too large to include in the repository.

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016?select=NFL+Play+by+Play+2009-2018+%28v5%29.csv)
2. Place the file in the `dataset/` folder
3. Rename it to: `nfl_playbyplay_dataset_2009_2018.csv`

### Running the Pipeline

#### Step 1: Data Filtering

Run `data_preprocessing/data_filtering.ipynb`:
- Loads the original dataset
- Removes irrelevant features
- Filters to only "run" and "pass" play types
- Removes rows with null values
- Saves to `dataset/nfl_filtered.csv`

#### Step 2: Feature Encoding

Choose one encoding approach based on your model:

**For Logistic Regression:**
- Run `data_preprocessing/feature_encoding_v1.ipynb`
- One-hot encodes categorical features
- Saves to `dataset/nfl_encoded_v1.csv`

**For Tree-Based Models (XGBoost, CatBoost):**
- Run `data_preprocessing/feature_encoding_v2.ipynb`
- Keeps categorical features as category dtype
- Saves to `dataset/nfl_encoded_v2.csv`

#### Step 3: Train Models

**Logistic Regression:**
- Run `models/logisticregression.ipynb`
- Uses `nfl_encoded_v1.csv`

**XGBoost:**
- Run `models/xgBoost.ipynb`
- Uses `nfl_encoded_v2.csv`
- Includes hyperparameter tuning with GridSearchCV