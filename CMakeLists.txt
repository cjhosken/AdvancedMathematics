# We will always try to use a version > 3.1 if available
cmake_minimum_required(VERSION 3.2)

project(AdvancedMathematics)

# Set the C++ standard to use
set(CMAKE_CXX_STANDARD 17)

# Add target executable and the file it is built from
add_executable(main Week1_Calc/main.cpp)

# Include directories for fmt and SDL2 (handled by vcpkg)
include_directories("/public/devel/24-25/vcpkg/installed/x64-linux/include")

# Find SDL2 using vcpkg and link it to the executable
find_package(SDL2 REQUIRED)
target_link_libraries(main SDL2::SDL2 SDL2::SDL2main)

find_package(SDL2_image REQUIRED)
target_link_libraries(main SDL2_image::SDL2_image)

# Link libraries (in case additional directories are needed)
link_libraries("/public/devel/24-25/vcpkg/installed/x64-linux/lib")
