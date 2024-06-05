# Decentralized Data Parallel

The package is an PyTorch extension that faciliates multi-GPU decentralized data parallel training.

## Install
```bash
pip install decent-dp
```

## How to use

Firstly, it should have distributed environment available, which means the script should be run by [`torchrun`](https://pytorch.org/docs/stable/elastic/run.html).

Before making the model distributed, it should initialize the distributed environment by
```python
import torch.distributed as dist
dist.init_process_group()
```
Then wrap the model with `DecentralizedDataParallel`. Since the optimizer and the learning rate scheduler are fused in the backward pass, one will need to provide two functions: (1) `optim_fn` (`Callable[[List[Tuple[Tensor, str]]], Optimizer]`): the function constructs the optimizer based on the list of parameters with their names. (2) `lr_scheduler_fn` (`Callable[[Optimizer], LRScheduler]`, optional): the function constructs the learning rate scheduler based on the provided optimizer. Examples of two functions can be found at `decent_dp.optim.optim_fn_adam` and `decent_dp.optim.lr_scheduler_fn_cosine_with_warmup`.


```python
from decent_dp import DecentralizedDataParallel as DDP
model = ...
model = DDP(model,
            optim_fn=...,
            lr_scheduler_fn=...,
            topology=...)
```

## Supported Schema

The decentralized algorithm schema should follow
$$x_{i}^{(t)}=d_i^{(t)}+\sum_{j\in\mathcal{N}(i)}W_{ij}x_i^{(t-1)}\\ d_i^{(t)}=G\left(F_i,x_j^{(t-1)}\right)$$
which means that the local update doesn't depend on the neighbors' models in the same iteration, but it can 

## Customized Communication Topology

Currently, the provided communication topologies are `complete`, `ring`, `one-peer-exp` and `alternating-exp-ring`.

One can introduce customized by registering additional topologies.
```python
from decent_dp.topo import Topology, TopologyReg, Edge

@TopologyReg.register('custom-topology')
class CustomTopology(Topology):
    def _get_topo_edges(self) -> List[List[Edge]]:
        ...
```

One should override the `_get_topo_edges` method to provide the edges in every iteration in the loop. In the current version, it performs sanity check to make sure that (1) every worker is involved in every iteraion. (2) every worker is involvede in only one edge in every iteration.

The preset topologies are good examples which can be found at `decent_dp.topo.CompleteTopology`, `decent_dp.topo.RingTopology`, and etc..