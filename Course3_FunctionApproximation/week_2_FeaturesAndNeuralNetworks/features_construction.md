# Features construction

## Coarse coding

Generalization of state aggregation, allowing for overlapping encoding regions of the state space.

![image-20200616235203667](/Users/nicolasthiebaut/Library/Application Support/typora-user-images/image-20200616235203667.png)

In coarse coding, **more features** leads to a **better discrimination** (otherwise many states have the same representation), while **"bigger" features** (more states covered) gives **better generalization** (because with "small" features learning cannot generalize to other states with overlapping representations).

## Tile coding

Computationally efficient coarse coding.

![image-20200617000147650](/Users/nicolasthiebaut/Library/Application Support/typora-user-images/image-20200617000147650.png)

Note: the number of requires tiling grows exponentially with the dimension.