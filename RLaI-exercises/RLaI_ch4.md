4.1
​    $q_{\pi}(11,down)=-1$, $q_{\pi}(7,down)=-15$
​    
4.2
​    if transitions are unchanged, $v_{\pi}=-12$
​    if 13 changed, $v_{\pi}=-20$
​    
4.3
​    $$ q_{k+1}(s,a)=\sum_{s'.r}p(s',r|s,a)[r+\gamma \sum_{a'}\pi(a'|s)q_k(s',a')] $$

4.4
​    part 3 in algorithm, change first if: if old-action$\ne \pi(s)$ and q(s, old-action)<q(s, $\pi(s)$), then......

4.5
​    Instead of updating v, update q value at each step,and choose police based on $argmax_aq(s,a)$

4.6
    1. no change
    2. v update as bellman exceptation:
        $$ v(s) \leftarrow \sum_{a\in A(s)}\pi(a|s)\sum_{s',r}p(s'.r|s.a)[r+\gamma v(s')] $$
    3. choose greedy police than maximize expectation of v  
    
4.8
    

4.10
    $$ q_{k+1}(s,a)=\sum_{s',r}p(s',r|s',a)[r+\gamma \max_{a'}q_k(s',a')] $$