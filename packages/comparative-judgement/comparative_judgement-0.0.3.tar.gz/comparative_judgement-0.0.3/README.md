# Comparative Judgement

A package for comparative judgement (CJ).


Importing the BCJ model:

```python
from cj.models import BayesianCJ

BCJ = BayesianCJ(4)
```

Creating the data:

```python
import numpy as np

data = np.asarray([
    [0, 1, 0],
    [0, 1, 0],
    [0, 3, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [2, 1, 2],
    [2, 1, 2],
    [2, 1, 2],
    [2, 3, 2],
    [3, 0, 3],
    [3, 0, 3],
    [3, 0, 3],
    [3, 0, 3],
    [3, 2, 3],
    [3, 2, 3],
    [3, 2, 3],
])
```

running the model:

```python
BCJ.run(data)
```

Finding the $\mathbb{E}[\mathbf{r}]$
```python
BCJ.rank_scores
>>> [3.046875, 2.09765625, 3.05859375, 1.796875]
```

Finding the BCJ rank:
```python
BCJ.res
>>> array([3, 1, 0, 2])
```

Importing the BTM Model:

```python
from cj.models import BayesianCJ

BTM = BTMCJ(4)
```

running the model:
```python
BTM.run(data)
```

Finding the optimised p scores:
```python
BTM.optimal_params
>>> array([-0.44654627,  0.04240265, -0.41580243,  0.81994508])
```

find BTM rank:
```python
BTM.rank
>>> array([3, 1, 2, 0])
```