# SPDX-FileCopyrightText: 2025 Hyuta Sasaki
# SPDX-License-Indetifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weather_chiba = launch_ros.actions.Node(
        package = 'mypkg',
        executable = 'weather_chiba',
        )
    listener = launch_ros.actions.Node(
        package = 'mypkg',
        executable = 'listener',
        output = 'screen'
        )

    return launch.LaunchDescription([weather_chiba, listener])
