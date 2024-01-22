# lognorm

$$
X=e^Y\sim \mbox{Lognormal}(\mu,\sigma ^2)
\quad\Leftrightarrow\quad
Y\sim N(\mu,\sigma ^2)
$$

### random_samples.py

generate lognorm random samples using scipy.stats.lognorm and scipy.stats.norm separately

### log_of_random_samples.py

Generate log of lognorm random samples using scipy.stats.lognorm and scipy.stats.norm separately, which should agree with normal distribution.