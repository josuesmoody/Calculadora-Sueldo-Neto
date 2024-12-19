
# Net Salary Calculator 💰

## Overview
This project is a Python-based tool designed to calculate net salary based on gross income, deductions, and tax rates. 
It simplifies salary calculations for employees, employers, and payroll managers by providing clear breakdowns of all 
components affecting take-home pay.

## Features
- **Gross to Net Calculation**: Automatically calculate net salary from gross income.
- **Tax Deductions**: Apply customizable tax rates and deductions.
- **Social Contributions**: Factor in contributions like social security or retirement plans.
- **Flexible Inputs**: Specify custom deduction categories and rates.
- **Reports**: Generate detailed salary breakdowns.

## Prerequisites

### Tools & Environment
- Python 3.7 or later.
- A virtual environment is recommended for managing dependencies.

### Libraries
Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/josuesmoody/Net-Salary-Calculator.git
cd Net-Salary-Calculator
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Calculator
Use the main script to calculate net salary. For example:
```bash
python scripts/calculate_salary.py --gross 5000 --deductions tax=20,insurance=5 --output ./results/salary_report.txt
```

### Customizing Deductions
Modify the `deductions.json` file to define custom deduction categories and rates.

### Example Output
After running the script, the tool generates a report like this:
```
Salary Breakdown:
Gross Salary: $5000
Deductions:
  - Tax: $1000
  - Insurance: $250
Net Salary: $3750
```

## Directory Structure
```
Net-Salary-Calculator/
├── data/                 # Directory for configuration files (e.g., deductions.json)
├── results/              # Directory for generated reports
├── scripts/              # Scripts for salary calculation and customization
│   ├── calculate_salary.py  # Main script for salary calculations
│   └── deductions.py        # Script for managing deductions
├── requirements.txt      # Dependencies list
├── README.md             # Project documentation
└── LICENSE               # License file
```

## Key Technologies Used

- **Python argparse**: For creating command-line interfaces.
- **JSON**: To manage flexible deduction configurations.
- **Pandas (optional)**: For advanced data handling and reporting.

## Contributing

Contributions are welcome! If you'd like to improve or add features:
1. Fork this repository.
2. Create a new branch for your changes.
3. Test thoroughly and submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Acknowledgments

- Inspired by the need for transparency in salary calculations.
- Supported by the Python community and open-source libraries.

## Contact

Created by **Josué Elías Santana**.  
Feel free to [contact me](https://www.linkedin.com/in/josue-santana/) for any inquiries.

---
✨ Simplify payroll management and take control of salary breakdowns! ✨
