import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    pkg_ie4060_asssignment2 = get_package_share_directory('ie4060_asssignment2')
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')

    nav2_params_path = os.path.join(pkg_ie4060_asssignment2, 'config', 'nav2_params.yaml')

    map_file_path = os.path.join(pkg_ie4060_asssignment2, 'maps', 'maze.yaml') 

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_nav2_bringup, 'launch', 'navigation_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
                'params_file': nav2_params_path,
                'map': map_file_path
            }.items(),
        ),

        # RViz for navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_nav2_bringup, 'launch', 'rviz_launch.py')
            ),
             launch_arguments={
                'rviz_config': os.path.join(pkg_nav2_bringup, 'rviz', 'nav2_default_view.rviz')
            }.items(),
        )

    ])
