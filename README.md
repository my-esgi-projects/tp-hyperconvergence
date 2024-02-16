# Pynutanix 

Python cli tools for interact with nutanix api

## Requirements
* python3, Tested on 3.11
* python3-pip

## Installation

* Clone repository
```bash
git clone https://github.com/my-esgi-projects/tp-hyperconvergence
```

* Install dependencies
```bash
cd tp-hyperconvergence/
python3 -m pip install -r requirements.txt
```

* Install package in editable mode
```bash
python3 -m pip install --editable . 
```


## Configuration

* Export NUTANIX_ENDPOINT_API, NUTANIX_PASS, NUTANIX_USER as environnement variables
```bash
export NUTANIX_ENDPOINT_API=https://10.38.4.199:9440/PrismGateway/services/rest/v2.0/
export NUTANIX_USER=admin
export NUTANIX_PASS=nx2Tech795!
```

## Basics commands

* Run help
```bash
pynutanix --help
```

* Create storage
```bash
pynutanix storage create -n test6-storage -c 20000000000
```


* Create Network
```bash
pynutanix network create -n test6-network -v 1 -i '{"network_address": "10.0.16.0", "prefix_length": "24"}'
```

Ps: Rest of commands as soon as possible, see how to launch exam TP in bottom

## Run TP

* Show help
```bash
pynutanix tp launch --help
```

* Launch using default prefix value 
```bash
pynutanix tp launch
```

* Launch with specific prefix=tp-esgi-SRC2-GRP6
```bash
pynutanix tp launch --prefix my-custom-prefix
```


Ps: Feel Free To leave us comment or open github issues if any problems.

