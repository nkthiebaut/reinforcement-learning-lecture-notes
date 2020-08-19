# Kaggle RL tutorial

https://www.kaggle.com/alexisbcook/play-the-game

## Connect 4 

### One-step lookahead

![image-20200817102351443](assets/image-20200817102351443.png)



![image-20200817102702227](assets/image-20200817102702227.png)

![image-20200817102723251](assets/image-20200817102723251.png)

### Minimax

![image-20200818203429134](assets/image-20200818203429134.png)

Optimization technique: [Alpha-Beta pruning](https://en.wikipedia.org/wiki/Alpha–beta_pruning)

$\alpha$:  minimum score that the maximizing player is assured of

$\beta$:  maximum score that the minimizing player is assured of

Example of when search can stop based on the values of $\alpha$ and $\beta$

![image-20200818213611055](assets/image-20200818213611055.png)

