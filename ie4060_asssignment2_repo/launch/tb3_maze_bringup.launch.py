import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Set the TurtleBot3 model
    os.environ['TURTLEBOT3_MODEL'] = 'burger'

    # Get paths
    pkg_ie4060_asssignment2 = get_package_share_directory('ie4060_asssignment2')
    pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    # Path to your custom world file
    world_file_name = 'maze.world'
    world_path = os.path.join(pkg_ie4060_asssignment2, 'worlds', world_file_name)

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_turtlebot3_gazebo, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_path}.items(),
    )

    # Robot state publisher
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_turtlebot3_gazebo, 'launch', 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': 'true'}.items(),
    )

    # Spawn the robot
    spawn_turtlebot3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_turtlebot3_gazebo, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        # Spawn at (1.25, 0.25) which is a free space at the bottom center
        launch_arguments={
            'x_pose': '1.25',
            'y_pose': '0.25',
            'z_pose': '0.01',
            'use_sim_time': 'true'
        }.items(),
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_turtlebot3,
    ])