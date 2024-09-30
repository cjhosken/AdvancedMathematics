mkdir build
cd build
cmake .. -DInstallRoot="../SDL2"
cmake --build . -j $(nproc)
rm -rf build