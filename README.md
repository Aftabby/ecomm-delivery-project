# E-Commerce Product Delivery Prediction

This project predicts whether a product from an e-commerce company will be delivered on time or not. It also analyzes various factors affecting delivery and studies customer behavior. The project includes machine learning models for prediction and a Power BI dashboard for visualization.

## GitHub Repository

All project files and detailed documentation are available on the associated GitHub profile.  
[GitHub Repository](https://github.com/Aftabby/ecomm-delivery-project)

## Project Structure

```
ecomm-delivery-project/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   ├── mediaqueries.css
│   │   ├── js/
│   │       ├── script.js
│   ├── templates/
│   │   ├── layout.html
│   │   ├── project3.html
│   ├── app.py
│   ├── utils.py
│   ├── static/
│   │   ├── data/
│   │       ├── compare_df.csv
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run Locally

### 1. Using Flask (`app.py`)

1. Clone the repository:
   ```bash
   git clone https://github.com/Aftabby/ecomm-delivery-project.git
   cd ecomm-delivery-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app/app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

---

### 2. Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/Aftabby/ecomm-delivery-project.git
   cd ecomm-delivery-project
   ```

2. Build the Docker image:
   ```bash
   docker build -t ecomm-delivery-project .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 5000:5000 ecomm-delivery-project
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Features

- Predicts on-time delivery using machine learning models.
- Analyzes customer behavior and product attributes affecting delivery.
- Includes a Power BI dashboard for interactive visualizations.

## Machine Learning Models Used

- Random Forest Classifier
- Decision Tree Classifier
- Logistic Regression
- K Nearest Neighbors Classifier

## License

This project is licensed under the MIT License. See the LICENSE file for details.
