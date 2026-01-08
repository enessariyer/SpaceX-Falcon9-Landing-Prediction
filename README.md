# SpaceX Falcon 9 Landing Prediction Project 🚀

This project encompasses an end-to-end data science workflow aimed at predicting the success of the first-stage landing of SpaceX's Falcon 9 launches. By analyzing factors such as launch sites and payload mass, it aims to forecast landing success, which directly impacts launch costs and risks.

## 📁 Project Structure

| File / Folder | Description |
| :--- | :--- |
| `notebooks/` | Jupyter Notebooks covering data collection, EDA, and Machine Learning. |
| `images/` | Visual outputs and plots used in the analysis and README. |
| `scripts/` | Python code for the interactive Plotly Dash web application. |
| `requirements.txt` | List of Python libraries required to run the project. |

---

## 🛠️ Technologies Used

* **Languages:** Python 3.x
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Folium, Plotly Dash
* **Database:** SQL / PostgreSQL
* **Machine Learning:** Scikit-Learn (Logistic Regression, SVM, Decision Tree, KNN)

---

## 🚀 Project Workflow

### 1. Data Collection & Preparation
* Data was gathered using the SpaceX API and web scraping techniques.
* Data cleaning was performed, and baseline insights were extracted using SQL queries.

### 2. Exploratory Data Analysis (EDA)
Success rates were analyzed across different launch sites, payload masses, and orbital types.
> ![Launch Site vs Payload](images/launchsite_vs_payload.png)

### 3. Interactive Visualizations
* **Folium** was used to map launch site locations and proximity to coastlines/highways.
* **Plotly Dash** was utilized to create an interactive dashboard for real-time success analysis.

### 4. Machine Learning (ML)
Features were standardized using `StandardScaler`, and `GridSearchCV` was employed to optimize model hyperparameters.
* **Best Model:** Decision Tree
* **Test Set Accuracy:** 83.3%

---

## 🏁 Conclusion & Insights

The following key findings were identified throughout the project:

* **Launch Site Dynamics:** The KSC LC-39A site shows the highest success rate. VAFB SLC-4E remains a critical site for polar orbit missions.
* **Payload Mass Correlation:** Success is most consistent within the 2000kg to 5000kg payload range. Heavier payloads (8000kg+) tend to show increased landing risks.
* **Orbital Success:** Low Earth Orbit (LEO) missions have the highest landing success rates, whereas GTO missions present a greater challenge.
* **Model Performance:** Among all tested algorithms, the **Decision Tree** model provided the most stable performance with a test accuracy of **83.3%**.
* **Cost Efficiency:** Accurate prediction of landing success supports SpaceX's goal of rocket reusability, which potentially reduces launch costs by up to 70%.

---