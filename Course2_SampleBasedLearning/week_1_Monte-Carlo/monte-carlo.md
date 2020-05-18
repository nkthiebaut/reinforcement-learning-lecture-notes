# Monte-Carlo Methods



Monte-Carlo = repeated random sampling

No need for prior knowledge of the environment's dynamics!

Similarity with bandits: estimation of average reward (multi-arm bandits)→ estimation of average return (Monte-Carlo)

![image-20200507085736570](assets/image-20200507085736570.png)

## Monte Carlo for control

### Exploring start

Same algorithm as before, but with exploring start and assignement of policy actions.

![image-20200508174737788](assets/image-20200508174737788.png)

### $\epsilon$-soft policies

![image-20200508175234034](assets/image-20200508175234034.png)

Algorithm is the same as before with the following changes

![image-20200510151810822](assets/image-20200510151810822.png)

![image-20200508175412640](assets/image-20200508175412640.png)



## Off-policy learning

The behavioral policy $b$ must **cover** the target policy $\pi$.

### Importance sampling

![image-20200508180113118](assets/image-20200508180113118.png)



![image-20200510152453336](assets/image-20200510152453336.png)



## Written notes

![image-20200518162455918](assets/image-20200518162455918.png)

![image-20200518162516104](assets/image-20200518162516104.png)

![image-20200518162541441](assets/image-20200518162541441.png)

![image-20200518162552878](assets/image-20200518162552878.png)

![image-20200518162601149](assets/image-20200518162601149.png)

![image-20200518162609620](assets/image-20200518162609620.png)