# Air Quality Data Pipeline

This project demonstrates a simple data engineering pipeline that processes hourly sensor readings from a chemical multisensor device deployed in an Italian city. It includes preprocessing steps to clean the data, handle missing values, and convert timestamps into usable formats for time series analysis.

##  Dataset

The dataset comes from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/360/air+quality), containing:

- Hourly sensor readings from an on-field multisensor air quality device
- Reference gas concentration values (CO, NOx, NO2, Benzene, etc.)
- Data from March 2004 to February 2005
- Missing values represented by `-200`

##  Features

- Loads and parses the raw CSV
- Combines `Date` and `Time` into a single `Datetime` index
- Drops unnamed and empty columns
- Cleans missing or empty rows
- Saves cleaned data as a `.parquet` file

##  Tech Stack

- Python 3.10
- `pandas`
- `pyarrow` (for saving Parquet)
- `venv` for environment isolation
- Optional: `jupyter`, `matplotlib`, `seaborn` for exploration

##  How to Run It

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/air-quality-pipeline.git
cd air-quality-pipeline

# Step 2: Create environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Step 3: Run the pipeline
python run_pipeline.py

