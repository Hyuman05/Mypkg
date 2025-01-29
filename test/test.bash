#!/bin/bash
# SPDX-FileCopyrightText: 2025 hyuta sasaki
# SPDX-License-Identifier: BSD-3-Clause

res=0

dir=~
[ "$1" != "" ] && dir="$1"

sudo apt -y install python3-pip
pip3 install requests

cd $dir/ros2_ws
colcon build

source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash

timeout 20 ros2 launch mypkg weather_chiba.launch.py &> /tmp/weather_data.log

sleep 20
echo TESTLOG
cat /tmp/weather_data.log

exit $res
