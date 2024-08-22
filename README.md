# Explanation

## Problem
We have a queue of people waiting to be served.
The queue is emptied at a constant rate $a$ at the tail.
There is a small chance $b$ that an individual in the queue leaves.

We want to predict the time remaining in queue for a person at position $x$.

The code is for Poke Genie queue prediction. With 8s position polling. The position is entered manually.
Just run and enter your position in queue as it changes.

# Discrete (abandonned for continuous below)

The queue is emptied at a constant rate $a$ at the tail.
There is a small chance $b$ that an individual in the queue leaves.


Thus, time from position $n$ to $n-1$ ($b$ is negative in this case):

$$
g(n) = f(n) - f(n-1) = a + bn
$$
$$
f(n) = a + bn + f(n-1)
$$
$$
\text{with} \space f(0) = 0
$$

<br>

$$
\begin{align}
f(n) &= an + \frac{n(n+1)}2 * b + c \\
	&= an + \frac b2 (n^2 + n) + c\\
	&= (a + \frac b2)n + \frac b2 n^2 + c\\
\end{align}
$$
Total time from position $n$:
$$f(n) = \frac b2 n^2 + (a + \frac b2)n + c\space,\space c=0$$
Time from $n$ to $n-1$:
$$g(n) = f(n) - f(n-1) = a + bn$$
Time from $n$ to $n-k$:
$$
\begin{align}
h(n, k) &= f(n) - f(n-k) \\
&= \sum_{i=0}^{k-1}{g(n-i)} \\
&= ka + b (kn - \frac{k(k-1)}2) \\
&= kbn + ka - \frac{k(k-1)}2 b \\
&= (kn - \frac{k(k-1)}2)b + ka
\end{align}
$$

$$
\frac{h(n,k)}{k} = (n - \frac{(k-1)}2)b + a
$$

<br>

# Continuous approximation

Time from position $x$ to $x-1$:
$$
g(x) = a + bx
$$

Time from position $x$ to $0$ (too few samples):
$$
G(x) = f(x) = ax + \frac b2 x^2 + 0
$$

Time from $x_1$ to $x_2$ (unusable):
$$
\begin{align}
G(x1) - G(x2) &= ax_1 + \frac b2 x_1^2 - ax_2 - \frac b2x_2^2 \\
&= a(x_1 - x_2) + \frac b2 (x_1^2 - x_2^2) \\
&= G(x_1 - x_2) + \frac b2 (2x_1x_2 - 2x_2^2)\\
\\
\\
&= a(x_1 - x_2) + \frac b2 (x_1 - x_2)(x_1 + x_2) \\
&= (x_1 - x_2) (a + \frac b2 (x_1 + x_2))
\end{align}
$$

Time from start $n$ to $x$:
$$
\begin{align}
H_n(x) &= G(n) - G(x)\\
&= G(n) - ax - \frac b2 x^2, \space\space G(n) = an + \frac b2 n^2
\end{align}
$$

# Final
We'll collect $H_n(x)$ as the queue moves, and use quadratic regression to find $-a$ and $-\frac b2$.

Then we'll convert for $G$ and predict the remaining time in queue $G(x)$.