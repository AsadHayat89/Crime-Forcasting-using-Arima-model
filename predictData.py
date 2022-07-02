from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
import pickle
import numpy as np
#model=ARIMAResults.load('model.pkl')
with open('model_pickle','rb') as f:
    model = pickle.load(f)
def predictvalue(n_periods):
    fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
#print(fc[0])
    print(fc)

