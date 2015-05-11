# AsseticsMaker
Generate YML assets config file from an non-bundled view vendor
# Use
```shell
cd vendor/acme
tree -fi | python3 ~/AsseticsMaker.py ${PWD##*/} > ../../app/config/config_assets.yml
```
# Arguments
```shell
python3 ~/AsseticsMaker.py vendor_name
```
