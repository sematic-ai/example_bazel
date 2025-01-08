import ray
import sematic
import time
from sematic.ee.ray import RayCluster, RayNodeConfig, SimpleRayCluster


@ray.remote
def do_it(x: int) -> int:
    print(f"Doing {x}")
    return 2*x


@sematic.func(standalone=True)
def pipeline():
    with RayCluster(
        config=SimpleRayCluster(
            n_nodes=2,
            node_config=RayNodeConfig(cpu=1, memory_gb=2),
        )
    ):
        print(ray.get([do_it.remote(16)]))
    print("Done!!!!")

