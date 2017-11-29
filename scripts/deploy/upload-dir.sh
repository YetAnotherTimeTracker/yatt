#!/usr/bin/env bash

# transfers whole yatt directory into /yatt folder of droplet

# cd to root folder from which /yatt is visible
cd ../../..

# secure copy to remote dir
scp -r /yatt root@188.226.181.58:/home/scptest/yatt
