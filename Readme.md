WIP! Webapp for pandas-ta indicators.

Select a pandas-ta indicator, enter the desired parameters (on the sidebar, you will find a description and possible arguments to submit).

Once validated, it will backtest a strategy based on this indicator using vectorbt. For data, it is using Cac40 (French main indice) data from yahoo finance using those settings:

```
"^FCHI", start="2020-01-01", end="2022-01-01", timeframe="1d", limit=10000
```

This is just for training purposes as my knowledge in trading is very limited and many functions aren't implemented yet.

![Animation](https://user-images.githubusercontent.com/66461774/158669709-89f9e2c5-9db9-455d-a4cf-884b46df155b.gif)
