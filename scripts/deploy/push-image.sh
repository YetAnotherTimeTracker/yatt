#!/usr/bin/env bash

# builds bot image and pushes it to dockerhub

img_name="tp_bot"

cd ../..

echo "> Building bot image"
docker build -t $img_name .

echo "> Getting version"
cd scripts/deploy
source version.txt

echo "> Tagging image version: $BOT_VERSION"
docker tag $img_name yattbot/bots:$BOT_VERSION

#echo "> Logging in to Docker Hub"
#source credentials.txt
#docker login --username=$DOCKERHUB_LOGIN --password=$DOCKERHUB_PSW
#cat dockerhub_psw.txt | docker login --username $DOCKERHUB_LOGIN --password-stdin

#echo "> Pushing image"
#docker push yattbot/bots:$BOT_VERSION

#echo "> All done"
