# AsseticsMaker
Generate YML assets config file from an non-bundled view vendor
# Use
for all files in the current directory
```shell
cd vendor/acme
tree -fi | python3 ~/AsseticsMaker.py ${PWD##*/} > ../../app/config/config_assets.yml
```
for specified files in the current directory
```shell
cd vendor/acme
tree -fi -P "*.js|*.css|*.jpg|*.jpeg|*.gif|*.png|*.eot|*.svg|*.ttf|*.woff" | python3 ~/PycharmProjects/AsseticsMaker/AsseticsMaker.py ${PWD##*/} > ../../app/config/config_assets.yml
```
# Arguments
```shell
python3 ~/AsseticsMaker.py vendor_name
```
