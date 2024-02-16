
export NUTANIX_USER=admin
export NUTANIX_PASS=nx2Tech795!


pynutanix storage create -n test6-storage -c 20000000000
pynutanix network create -n test6-network -v 1 -i '{"network_address": "10.0.16.0", "prefix_length": "24"}'

pynutanix vm create -n toto -m 2000 -v 2 -c 1 -i "toto" -ip "10.0.6.2" -u "yum update -y && yum install -y nginx"
