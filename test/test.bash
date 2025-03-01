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

sleep 2
echo TESTLOG
cat /tmp/weather_data.log

serch_string="Listen: 場所: 千葉県千葉市
【今日の天気】 天気: 晴れ　時々　くもり　所により　昼過ぎ　から　雨　で　雷を伴う, 最低気温: -°C, 最高気温: 12°C
【明日の天気】天気: 晴れ, 最低気温: 5°C, 最高気温: 10°C"
if grep -F "$search_string" /tmp/weather_data.log; then
    echo "成功"
else
    echo "失敗"
    res=1
fi


exit $res
