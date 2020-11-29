# Predictive Analysis of COVID-19

      
  On 31st  December 2019, WHO was alerted to several cases of pneumonia in Wuhan City, Hubei Province of China. The virus did not match any other known virus. This raised 
concern because when a virus is new,  its effect on people was unknown.<br />
  Coronavirus disease 2019 (COVID-19) is a contagious respiratory and vascular (blood vessel) disease. It is caused by becoming infected with severe acute respiratory 
syndrome coronavirus 2 (SARS-CoV-2), which is a specific type of coronavirus. 

## Goal of this Model
Forecasting future COVID-19 case counts would allow governments, businesses, and individuals to prepare in advance and plan their responses accordingly. For instance, 
local governments can use the results to anticipate the need for emergency supplies and health-related public services. Hospitals can use the results to foresee medical 
supply and personnel shortages. Universities and companies can also use the results to plan for adequate protection for students and employees. 

### Dataset
- - - 
[id1]: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset?select=covid_19_data.csv
[id2]: https://drive.google.com/file/d/1F5jBhDrawzO6nJv6rj1OQWKEksuMcSm2/view?usp=sharing
The [Novel Coronavirus 2019 Dataset][id1] has been used to build the model. The dataset can also be found [here][id2].
*Dataset was last updated on November 16th, 2020.*

### Installation
- - -
The modules required for executing the program are numpy, pandas, matplotlib, plotly, seaborn, scikit-learn, pmdarima and statsmodels.
* **Numpy** and **Pandas** are predominantly used for pre-processing. 
* **Matplotlib** and **Plotly** help in plotting graphs. 
* The **scikit-learn** module will be useful in calculating metrics such as Root Mean Square Error(RMSE). 
* For forecasting, we use the **auto_arima package of the pmdarima module**. 
* The **statsmodels** module will come handy while performing exponential smoothing.

      $ pip install pandas
      $ pip install numpy
      $ pip install matplotlib
      $ pip install seaborn
      $ pip install scikit-learn
      $ pip install pmdarima
      $ pip install statsmodels
      $ pip install plotly

### 
