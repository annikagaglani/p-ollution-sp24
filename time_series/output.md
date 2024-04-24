(pollution-env) breckenenright@Breckens-MacBook-Pro-4 time_series % python3 ./ARIMA.py
/Users/breckenenright/Desktop/p-ollution/p-ollution-sp24/time_series/./ARIMA.py:12: FutureWarning: The argument 'date_parser' is deprecated and will be removed in a future version. Please use 'date_format' instead, or read your data in as 'object' dtype and then call 'to_datetime'.
  series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)
            AQI
date           
2017-01-01   54
2017-01-02   46
2017-01-03   53
2017-01-04   70
2017-01-05   54
                               SARIMAX Results                                
==============================================================================
Dep. Variable:                    AQI   No. Observations:                 2187
Model:                 ARIMA(5, 1, 0)   Log Likelihood               -9020.097
Date:                Fri, 19 Apr 2024   AIC                          18052.194
Time:                        12:19:53   BIC                          18086.333
Sample:                    01-31-2017   HQIC                         18064.673
                         - 03-31-2023                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.1866      0.012    -15.443      0.000      -0.210      -0.163
ar.L2         -0.2907      0.019    -14.982      0.000      -0.329      -0.253
ar.L3         -0.1965      0.020     -9.992      0.000      -0.235      -0.158
ar.L4         -0.1307      0.022     -5.867      0.000      -0.174      -0.087
ar.L5         -0.1422      0.020     -7.075      0.000      -0.182      -0.103
sigma2       224.9328      3.665     61.371      0.000     217.749     232.116
===================================================================================
Ljung-Box (L1) (Q):                   0.37   Jarque-Bera (JB):              3285.11
Prob(Q):                              0.54   Prob(JB):                         0.00
Heteroskedasticity (H):               1.23   Skew:                            -0.22
Prob(H) (two-sided):                  0.00   Kurtosis:                         8.99
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
                 0
count  2187.000000
mean      0.009128
std      15.033472
min    -113.252677
25%      -7.468218
50%       0.576272
75%       7.800222
max      97.583556
