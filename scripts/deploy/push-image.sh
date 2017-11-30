#!/usr/bin/env bash
# builds bot image and pushes it to dockerhub

img_name="tp_bot"

cd ../..

echo "> Building bot image"
docker build -t $img_name .

echo "> Getting version"
cd scripts/deploy
typeset -i bot_version=$(cat version.txt)

echo "> Tagging image version: $bot_version"
docker tag "$img_name" yattbot/bots:"$bot_version"

echo "> Logging in to Docker Hub"
source cred/credentials.txt
cat cred/dockerhub_psw.txt | docker login --username "$DOCKERHUB_LOGIN" --password-stdin

echo "> Pushing image"
docker push yattbot/bots:"$bot_version"

((bot_version=bot_version + 1))
echo "> Updating version to: $bot_version"
echo "$bot_version" > version.txt


echo "All done!"
