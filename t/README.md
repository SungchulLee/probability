# t

$$
\frac{Z}{\sqrt{\frac{V}{d}}}\sim t_d\quad\quad\quad\quad\mbox{where$\quad$ $Z\sim N(0,1^2)$ and
$V\sim\chi^2_d$ are independent}
$$

### why_t.py

For $n$ iid samples $X_i$ from $N(\mu,\sigma ^2)$,
$$
\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{n}}}=N(0,1)
\quad\mbox{but}\quad
\frac{\bar{X}-\mu}{\frac{S}{\sqrt{n}}}=t_{n-1}
$$
where
$$
\bar{X}=\frac{\sum_{i=1}^nX_i}{n}\ \ \ \ \ \mbox{and}\ \ \ \ \ 
S^2=\frac{\sum_{i=1}^n(X_i-\bar{X})^2}{n-1}
$$