# Normal Distribution

### estimation_of_mu_and_sigma.py

Let $x_i$ be iid sample from $N(\mu,\sigma^2)$.
Then, $\mu$ and $\sigma^2$ can be estimated by $\hat{\mu}$ and $\hat{\sigma}^2$
where 
$$\begin{array}{lll}
\hat{\mu}&=&\frac{\sum_{i=1}^nx_i}{n}\\
\hat{\sigma}^2&=&\frac{\sum_{i=1}^n(x_i-\hat{\mu})^2}{n-1}
\end{array}$$