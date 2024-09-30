cmake_minimum_required(VERSION 3.24)
project(AdvancedMathematics)

set(CMAKE_CXX_STANDARD 20)

include(FetchContent)
set(FETCHCONTENT_QUIET FALSE)

# Fetch SDL2
FetchContent_Declare(
    SDL2
    GIT_REPOSITORY https://github.com/libsdl-org/SDL.git
    GIT_TAG release-2.26.3
    GIT_SHALLOW TRUE
    GIT_PROGRESS TRUE
)

# Fetch SDL2_image
FetchContent_Declare(
    SDL2_image
    GIT_REPOSITORY https://github.com/libsdl-org/SDL_image.git
    GIT_TAG release-2.6.3
    GIT_SHALLOW TRUE
    GIT_PROGRESS TRUE
)

# Optionally, set these variables before making available
set(BUILD_SHARED_LIBS OFF)  # Change to ON if you want shared libraries
set(SDL2IMAGE_INSTALL ON)

# Make available
FetchContent_MakeAvailable(SDL2 SDL2_image)

# Add executable
add_executable(main Week1_Calc/main.cpp)

# Link against SDL2 and SDL2_image libraries
target_link_libraries(main PRIVATE SDL2::SDL2-static SDL2_image::SDL2_image-static SDL2main)

# If you need to define main handling, uncomment this line
# add_definitions(-DSDL_MAIN_HANDLED)
