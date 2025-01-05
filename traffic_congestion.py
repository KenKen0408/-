from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータ（時間ごとの交通量）
data = [30, 35, 40, 38, 45, 50, 55, 53, 60, 65]
df = pd.Series(data)

# ARIMAモデルの作成と予測
model = ARIMA(df, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=5)

print("予測値:", forecast)
plt.plot(df, label="過去データ")
plt.plot(range(len(data), len(data) + len(forecast)), forecast, label="予測")
plt.legend()
plt.show()