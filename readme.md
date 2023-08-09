# OpenStack Neutron Module Analysis

This script analyzes the OpenStack Neutron project's Git repository to identify the five most actively changed modules over the last three years. The results are visualized in a bar chart.

## Dependencies

- Python 3.8+
- GitPython
- Matplotlib

## Setup

1. Clone this repository:
```bash
git clone https://github.com/mihailBz/NeutronTracker.git
cd NeutronTracker
```

2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```
for Windows:
```bash
venv\Scripts\activate
```

3. Install the necessary libraries:

```bash
pip install -r requirements.txt
```

## Execution

Run the script with:

```bash
python main.py
```

After execution, the script will display a bar chart showcasing the top 5 modules in the OpenStack Neutron project based on commit activity over the last three years. Additionally, the bar chart will be saved as `report_chart.png` in the same directory and the commit counts for the top 5 modules will be printed to the console.
