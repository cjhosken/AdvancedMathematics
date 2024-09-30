# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-src"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-build"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/tmp"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/src/sdl2-populate-stamp"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/src"
  "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/src/sdl2-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/src/sdl2-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/run/media/s5605094/CJ_LabDrive/Studies/University/2nd/AdvancedMathematics/build/_deps/sdl2-subbuild/sdl2-populate-prefix/src/sdl2-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
