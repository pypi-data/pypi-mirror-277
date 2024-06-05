#!/bin/bash
set -e
set -o pipefail
# If devopstestor is in a container, dockercontroller must be used without volume
sed -i "s/preset_name: saltstack_dockerincontainer/preset_name: saltstack_dockerincontainer_novolume/g" "$DEVOPSTESTOR_PATH/presets/logstash/config/machine.yml"

exit $?