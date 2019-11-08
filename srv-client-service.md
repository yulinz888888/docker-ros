# create srv directory and file
```
cd ~/catkin_ws/src/beginner_tutorials
mkdir srv
touch AddTwoInts.srv
```

# in AddTwoInts.srv, the code is:
```
int64 a
int64 b
---
int64 sum
```


# modifiy Packages.xml
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

# Modify CMakeLists.txt
Do not just add this line to your CMakeLists.txt, modify the existing line

```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
```

```
add_service_files(
  FILES
  AddTwoInts.srv
)
```

```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

# execute the following code to compile
```
roscd beginner_tutorials
cd ../..
catkin_make
catkin_make install
source devel/setup.bash
```