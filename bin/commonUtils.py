from collections import namedtuple
import sys

PoolType = namedtuple("PoolType", ["listName", "solaceDockerImageName", "haEnabled"])
POOL_TYPES = {
        "Shared-VMR": PoolType("shared", "latest-evaluation", False),
        "Medium-HA-VMR": PoolType("medium_ha", "latest-evaluation", True),
        "Large-VMR": PoolType("large", "latest-evaluation", False),
        "Large-HA-VMR": PoolType("large_ha", "latest-evaluation", True),
        "Community-VMR": PoolType("community", "latest-community", False)
}

# Meant to be used with bash scripts
def isValidPoolName(poolName):
    if poolName in POOL_TYPES:
        sys.exit(0)
    else:
        sys.exit(1)

def getSolaceDockerImageName(poolName):
    if poolName in POOL_TYPES:
        print(POOL_TYPES[poolName].solaceDockerImageName)
        sys.exit(0)
    raise ValueError("{} not a valid pool type".format(poolName))

def getHaEnabled(poolName):
    if poolName in POOL_TYPES:
        # Invert because 0 is success in shell scripting
        sys.exit(not POOL_TYPES[poolName].haEnabled)
    raise ValueError("{} not a valid pool type".format(poolName))