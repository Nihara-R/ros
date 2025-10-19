<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="default">
    
    <include>
      <uri>model://ground_plane</uri>
    </include>

    <include>
      <uri>model://sun</uri>
    </include>

    <!-- Maze walls - 0.5m spacing as per requirements -->
    
    <!-- Outer walls -->
    <model name="wall_outer_1">
      <static>true</static>
      <pose>0 -2.5 0.15 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.5 0.5 0.5 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_outer_2">
      <static>true</static>
      <pose>0 2.5 0.15 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.5 0.5 0.5 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_outer_3">
      <static>true</static>
      <pose>-2.5 0 0.15 0 0 1.5708</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.5 0.5 0.5 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_outer_4">
      <static>true</static>
      <pose>2.5 0 0.15 0 0 1.5708</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.5 0.5 0.5 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <!-- Inner maze walls (customize based on your maze design) -->
    <model name="wall_inner_1">
      <static>true</static>
      <pose>-1.5 0 0.15 0 0 1.5708</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>2 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>2 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.7 0.3 0.3 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_inner_2">
      <static>true</static>
      <pose>-0.5 1 0.15 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.7 0.3 0.3 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_inner_3">
      <static>true</static>
      <pose>0.5 -1 0.15 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.7 0.3 0.3 1</ambient>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall_inner_4">
      <static>true</static>
      <pose>1.5 0.5 0.15 0 0 1.5708</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>1.5 0.1 0.3</size></box>
          </geometry>
          <material>
            <ambient>0.7 0.3 0.3 1</ambient>
          </material>
        </visual>
      </link>
    </model>

  </world>
</sdf>
