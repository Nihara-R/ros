import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    
    pkg_slam_toolbox = get_package_share_directory('slam_toolbox')

    # SLAM launch
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_slam_toolbox, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'slam_params_file': os.path.join(
                get_package_share_directory('ie4060_asssignment2'), 
                'config', 
                'slam_toolbox_params.yaml' 
            )
        }.items(),
    )

    
    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'rviz_launch.py')
        )
    )

    return LaunchDescription([
        slam,
        rviz

    ])
