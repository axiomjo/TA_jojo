cmake_minimum_required(VERSION 3.8)

project(my_interfaces)

# Find CMake packages required by this package.
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(sensor_msgs REQUIRED) # Add this line

# Define custom messages, services, or actions here.
# For example, to define a message file 'MyMessage.msg' in the 'msg' directory:
# rosidl_generate_interfaces(${PROJECT_NAME}
#   "msg/ImageInfo.msg"
# )


# Configure the generation of interface files
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/ImageInfo.msg" # Replace with your message definitions
  "srv/SelectSource.srv" # Replace with your service definitions
  # "action/MyAction.action" # Uncomment and replace with your action definitions if you have any
  DEPENDENCIES sensor_msgs
)

# Install the generated interface files
install(TARGETS ${PROJECT_NAME}__rosidl_typesupport_c
  EXPORT export_${PROJECT_NAME}__rosidl_typesupport_c
  DESTINATION lib/${PROJECT_NAME}
)

install(TARGETS ${PROJECT_NAME}__rosidl_typesupport_cpp
  EXPORT export_${PROJECT_NAME}__rosidl_typesupport_cpp
  DESTINATION lib/${PROJECT_NAME}
)

install(EXPORT export_${PROJECT_NAME}__rosidl_typesupport_c
  FILE ${PROJECT_NAME}__rosidl_typesupport_cExport.cmake
  DESTINATION share/${PROJECT_NAME}/cmake
)

install(EXPORT export_${PROJECT_NAME}__rosidl_typesupport_cpp
  FILE ${PROJECT_NAME}__rosidl_typesupport_cppExport.cmake
  DESTINATION share/${PROJECT_NAME}/cmake
)

install(
  DIRECTORY msg
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY srv
  DESTINATION share/${PROJECT_NAME}
)


# this installs the python modules
ament_package()
