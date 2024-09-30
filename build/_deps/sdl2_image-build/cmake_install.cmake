# Install script for directory: /run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/opt/rh/gcc-toolset-13/root/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64" TYPE STATIC_LIBRARY FILES "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/libSDL2_image.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/SDL2" TYPE FILE FILES "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-src/SDL_image.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image" TYPE FILE FILES
    "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/SDL2_imageConfig.cmake"
    "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/SDL2_imageConfigVersion.cmake"
    "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-src/cmake/Findlibjxl.cmake"
    "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-src/cmake/Findwebp.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "devel" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image/SDL2_image-static-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image/SDL2_image-static-targets.cmake"
         "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/CMakeFiles/Export/723896c40bdfd110868cf92dd39b8a12/SDL2_image-static-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image/SDL2_image-static-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image/SDL2_image-static-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image" TYPE FILE FILES "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/CMakeFiles/Export/723896c40bdfd110868cf92dd39b8a12/SDL2_image-static-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/SDL2_image" TYPE FILE FILES "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-build/CMakeFiles/Export/723896c40bdfd110868cf92dd39b8a12/SDL2_image-static-targets-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "library" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/licenses/SDL2_image" TYPE FILE FILES "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2_image-src/LICENSE.txt")
endif()

