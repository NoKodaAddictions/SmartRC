DEL Temp
DEL Version

timeout 2

git fetch --all
git checkout -b backup-master
git reset --hard origin/main

timeout 2
git pull origin main

timeout 2

git rev-parse HEAD > Version
