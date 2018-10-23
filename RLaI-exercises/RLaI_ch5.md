5.2
    No different, since each state would visited once

5.3
    same as the one shown on page 95

5.4
    $$ Q(s,a)=\frac{\sum_{t\in \tau(s,a)}\rho _{t+1:T(t)-1}G_t}{\sum_{t\in \tau(s,a)}\rho _{t+1:T(t)-1}} $$
    
5.5
    when there are few episodes, for weighted import ance-sampling method, the variance in not obvious at first.

5.6
    with every-visit method, variance on each term is still big, then the sum is even more.
    
5.7
    - Initialize:
        V(s)=0 (arbitrarily), for all $ s\in S $
    - remove Returns(s) list
    - after unless $S_t$ appears in $S_0,S_1,...,S_{t-1}$:
        $$ V(S_t) \leftarrow V(S_t)+\frac{G_t-V(S_t)}{T-t} $$
        
5.8
    as $C_n$ is cumulative sum of the weights of first n returns, then:
    $$\begin{eqnarray}
    V_{n+1}=&=&\frac{\sum^n_{k=1}W_kG_k}{\sum^n_{k=1}W_k}=\frac{\sum^n_{k=1}W_kG_k}{C_n} \\
    &=& \frac{1}{C_n}(\sum^n_{k=1}W_kG_k) \\
    &=& \frac{1}{C_n}(W_nG_n+\sum^{n-1}_{k=1}W_kG_k) \\
    &=& \frac{1}{C_n}(W_nG_n+C_{n-1}\frac{1}{C_{n-1}}\sum^{n-1}_{k=1}W_kG_k) \\
    &=& \frac{1}{C_n}(W_nG_n+C_{n-1}V_n) \\
    &=& \frac{1}{C_n}(W_nG_n+(C_n-W_n)V_n) \\
    &=& \frac{1}{C_n}(C_nV_n+W_n(G_n-V_n)) \\
    &=& V_n+\frac{W_n}{C_n}(G_n-V_n)
    \end{eqnarray}$$
    
5.9
    since target police $\pi$ is greedy, then $\pi(a|s)=1$ for $a=argmax_{a'}Q(s,a')$
