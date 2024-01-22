# Poisson Approximation

### poisson_approx_binomial.py

$$Po(\lambda) \approx B(n,p)$$

```bash
python poisson_approx_binomial.py
```
### poisson_approx_indicators_sum.py

$$Po(\lambda) \approx \sum_{i=1}^n X_i\quad\mbox{where}\ X_i \sim B(p_i)$$

```bash
python poisson_approx_indicators_sum.py
```

### number_of_couples_with_same_birthday.py

Approximately 80,000 marriage took place in NY. 
Estimate the probability that
there are more than 250 couples with same birthday
who married in NY last year. 
$$S_n=\sum_{i=1}^n1_{A_{i}}\sim B(n,p)\approx Po(\lambda)$$

##### Exact probability using $S_n\sim B(n,p)$
$$P(S_n>250)=0.0187$$

##### Approximate probability using $X\sim Po(\lambda)$
$$P(X>250)=0.0188$$

##### Theoretical error bound
$$|P(S_n>250)-P(X>250)|
\le\sum_{i=1}^np_i^2=80000*\left(\frac{1}{365}\right)^2=0.6005$$

```bash
python number_of_couples_with_same_birthday.py
```