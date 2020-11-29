# Predictive Analysis of COVID-19

      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On 31<sup>st</sup>  December 2019, WHO was alerted to several cases of pneumonia in Wuhan City, Hubei Province of China. The virus did not
match any other known virus. This raised concern because when a virus is new,  its effect on people was unknown. Since then the number of cases has only seen an uphill.<p />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coronavirus disease 2019 (COVID-19) is a contagious respiratory and vascular (blood vessel) disease. It is caused by becoming infected with
severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), which is a specific type of coronavirus. On the 11<sup>th</sup> of March 2020, WHO declared the Coronavirus
outbreak to be a pandemic.<p />
      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COVID-19 has been recognized as a global threat, and several studies are being conducted using various mathematical models to predict the
probable evolution of this epidemic. These mathematical models are based on various factors and analysis are subject to potential bias. Data analytics plays an important role in
analyzing and predicting the spread of the virus, which will help in stabilizing the situation in the fastest possible way.

## Goal of this Model
- - -
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forecasting future COVID-19 case counts would allow governments, businesses, and individuals to prepare in advance and plan their responses accordingly. For instance, local governments can use the results to anticipate the need for emergency supplies and health-related public services. Hospitals can use the results to foresee medical supply and personnel shortages. Universities and companies can also use the results to plan for adequate protection for students and employees. 

## Dataset
- - - 
[id1]: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset?select=covid_19_data.csv
[id2]: https://drive.google.com/file/d/1F5jBhDrawzO6nJv6rj1OQWKEksuMcSm2/view?usp=sharing
The [Novel Coronavirus 2019 Dataset][id1] has been used to build the model. The dataset can also be found [here][id2]. <br />
<strong><em>Dataset was last updated on November 16th, 2020</strong></em>

## Installation
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

## Project Flow
- - -
The project begins with pre-processing and EDA. The province column is dropped due to the high amount of missing values in it. The dataset is then grouped by countries and 
the observation date of the reported case. All the cases reported on any day is added on a cumulative basis. The mortality rate and recovery rate are computed and visualized to
get a better understanding of the spread of the virus. The dataset can be categorized as a time series data as the data points are indexed in time order.<br />
Different models such as Holt Winters, AR, MA, ARIMA, SARIMA, Prophet etc. can be used for forecasting a time series data. 
### Time Series Analysis
Any time series data will have four important components, i.e..., trend, seasonality, noise and cyclicity and the ones with the presence of trend and seasonality can be marked
as non-stationary time series. The two common ways of converting a non-stationary time series to a stationary time series is either by simple exponential smoothing or
differencing. The ADF (Augmented Dickey Fuller) statistic is compared with the p-statistic to check for stationarity.<br />
The importance of converting a dataset from non-stationary to stationary arises due to the fact that the behavior of the time series in a particular time interval may repeat
over a different interval and it will affect the forecasting if that is not taken into account. This eventually helps in improving the accuracy of the model.<p />
### Models
This project sees the usage of the following models:
* *Holt's Linear Model*
* *Holt Winters Model*
* *AutoRegressive(AR) Model*
* *Moving Average(MA) Model*
* *AutoRegressive Integrated Moving Average(ARIMA) Model*
* *Seasonal AutoRegressive Integrated Moving Average(SARIMA) Model*
After building the model, the RMSE evaluator is used to check the metrics(such as error) between the actual(test dataset) value and the predicted value. Since the number
of cases is in the scale of millions, the RMSE will also be a relatively a high number. <p />
### Results
It can be seen that SARIMA gives the best predictions among all the models. After SARIMA falls the ARIMA model which has a much higher RMSE than SARIMA but does a decent job
with the predictions.<p />

## Conclusion
- - -
The model can give a fair idea about the rate at which the virus is going to spread around the globe. This information can be very helpful to understand how and when offices,
colleges and other institutions can be opened. To make this model perform better many other factors such as lockdown implementation, control on gatherings, economy etc. need to
be considered to predict the inflection points. This is because the number of cases can have an impact if people do not follow the safety norms. 
