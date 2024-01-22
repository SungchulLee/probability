# probability of no fixed points

For a bijective function $f$ on $\{1,2,\cdots,n\},$ 
$x$ is called a fixed point of $f$ if $f(x)=x$.
Count the number of the bijective functions $f$ on $\{1,2,\cdots,n\}$ with no fixed points.

$$\begin{array}{llll}
\Omega&\mbox{Set of all the bijective functions $f$ on $\{1,2,\cdots,n\}$}\\
\\
A_i&\mbox{Set of the bijective functions $f$  which fixes $i$}\\
\\
A=\cup_{i=1}^nA_i&\mbox{Set of the bijective functions $f$  which fixes some $i$}\\
\\
B=\Omega\setminus\cup_{i=1}^nA_i&\mbox{Set of the bijective functions $f$ with no fixed points}\\
\end{array}$$

##### $A=\cup_iA_i$ bijective functions that fix some $i$
By the inclusion-exclusion principle  
\begin{eqnarray}
\left|\cup_{i=1}^nA_i\right|
&=&\sum_{i=1}^n\left|A_i\right|-\sum_{1\le i<j\le n}\left|A_iA_j\right|+\cdots+(-1)^{n+1}\left|A_1A_2\cdots A_n\right|\nonumber\\
&=&{n\choose 1}\times (n-1)!-{n\choose 2}\times (n-2)!+\cdots+(-1)^{n+1}{n\choose n}\times (n-n)!\nonumber\\
&=&n!\left(\frac{1}{1!}-\frac{1}{2!}+\cdots+(-1)^{n+1}\frac{1}{n!}\right)\nonumber
\end{eqnarray}

##### $B=\Omega\setminus\cup_{i=1}^nA_i$ bijective functions with no fixed points
$$
|B|=|\Omega|-\left|\cup_{i=1}^nA_i\right|
=n!-n!\left(\frac{1}{1!}-\frac{1}{2!}+\cdots+(-1)^{n+1}\frac{1}{n!}\right)
=n!\left(1-\frac{1}{1!}+\frac{1}{2!}-\cdots+(-1)^{n}\frac{1}{n!}\right)
$$

##### probability of no fixed points
$$
\displaystyle
\mathbb{P}\left(B\right)=\frac{|B|}{|\Omega|}=1-\frac{1}{1!}+\frac{1}{2!}-\cdots+(-1)^{n}\frac{1}{n!}\sim e^{-1}
$$