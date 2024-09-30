cmake_minimum_required(VERSION 3.2)
project(SDL2_build)
include(ExternalProject)

set(InstallRoot ./SDL2 CACHE FILEPATH "Install root for dependencies")

ExternalProject_Add(
    SDL2
    URL https://www.libsdl.org/release/SDL2-2.30.7.tar.gz
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS 
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DBUILD_SHARED_LIBS=OFF
)

set(CHAIN SDL2)

ExternalProject_Add(
    SDL2_image
    URL https://github.com/libsdl-org/SDL_image/releases/download/release-2.8.2/SDL2_image-2.8.2.tar.gz
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DBUILD_SHARED_LIBS=OFF
        -DSDL2_DIR=<INSTALL_DIR>
    DEPENDS ${CHAIN}
)
    
set (CHAIN SDL2_image)