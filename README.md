# 🌿 VayuSense - Carbon Emission Prediction Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vayusense.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

VayuSense is an AI-powered platform for predicting carbon emissions at both national and vehicle levels. Utilizing advanced machine learning techniques, VayuSense aims to provide accurate data-driven insights to combat climate change effectively.

🌐 **Live Demo**: [vayusense.streamlit.app](https://vayusense.streamlit.app)

## ✨ Features

- **Country-wise Predictions**: AI-based forecasting of CO₂ emissions for countries until 2050.
- **Vehicle Estimator**: Calculate lifetime emissions and trip-specific carbon footprints.
- **Data Visualization**: Interactive charts and graphs for better insight.
- **Eco Score**: Vehicle emission efficiency rating.
- **Export Results**: Download predictions in CSV format.
- **Glass Morphism UI**: Modern, visually appealing interface with glass morphism effects.
- **Neon Glow Effects**: Enhanced visual aesthetics with neon accents.

## 📂 Project Structure

```
VayuSense/
├── data/                   # Data visualizations and datasets
├── models/                 # Trained ML models
├── notebooks/              # Jupyter notebooks for analysis
├──screenshots              # EDA out put screenshots
├── src/                    # Source code modules
│   └── vehicle_estimator.py
├── streamlit_app/          # Streamlit application
│   ├── app.py              # Main application file
│   ├── favicon.ico         # Browser favicon
│   └── requirement.txt     # Required Package
└── README.md               # Project documentation
```

## 🛠️ Technologies Used

- **Machine Learning**: Random Forest, XGBoost
- **Frontend**: Streamlit with custom CSS
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Joblib

## 🚀 Getting Started

### 📝 Prerequisites

- Python 3.8 or above
- Streamlit
- Plotly
- scikit-learn
- joblib

### ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itz-nirmal/carbon-emission.git
   ```

2. Navigate to the project directory:
   ```bash
   cd carbon-emission/streamlit_app
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### 📈 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Follow the on-screen instructions to navigate through different prediction modules.

## 📊 Data Visualizations \u0026 Analysis

### Global CO2 Emissions Over Time
![Global CO2 Emissions Over Time](data/Global%20CO2%20Emissions%20Over%20Time.png)

### CO2 Emission Trend for Top 5 Emitters
![CO2 Emission Trend](data/CO2%20Emission%20Trend%20for%20Top%205%20Emitters.png)

### Top 10 CO2 Emitters (2011)
![Top 10 Emitters](data/Top%2010%20CO2%20emitters%20in%202011.png)

### GDP vs CO2 Emissions Correlation
![GDP vs CO2](data/GDP%20vs%20CO2%20Emissions.png)

### Energy Use vs CO2 Emissions
![Energy vs CO2](data/Energy%20Use%20vs%20CO2%20Emissions.png)

### CO2 Emissions Distribution by Income Group
![Income Distribution](data/CO2%20Emissions%20Distribution%20by%20Income%20Group.png)

### Correlation Matrix of Features
![Correlation Matrix](data/Correlation%20Matrix%20of%20Features.png)

### Average CO2 Emission Growth Rates by Decade
![Growth Rates](data/Average%20CO2%20Emission%20Growth%20Rates%20by%20Decade.png)

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Fork this repository
2. Sign up at [streamlit.io](https://streamlit.io)
3. Click "New app" and select your forked repository
4. Set the main file path to `streamlit_app/app.py`
5. Click "Deploy"

### Local Deployment

```bash
# Clone the repository
git clone https://github.com/itz-nirmal/carbon-emission.git
cd carbon-emission/streamlit_app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## ❓ FAQ

**Q: Why am I getting a "model not found" error?**
A: Make sure you've run the Jupyter notebooks in the `notebooks/` folder to train and save the models.

**Q: Can I add more countries to the prediction list?**
A: Yes! You can modify the countries list in `app.py` and ensure you have corresponding data.

**Q: How accurate are the predictions?**
A: The model achieves approximately 92% accuracy based on historical data patterns.

## 🤝 Contributing

We welcome contributions to enhance the platform, improve predictions or usability. Feel free to submit pull requests or open issues.

## 📝 License

This project is licensed under the MIT License.

---

<p align="center">
  Made with ❤️ for a sustainable future 🌍
</p>
