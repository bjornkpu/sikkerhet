cmake_minimum_required(VERSION 2.8)

project(oppg2_c)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

add_executable(oppg2_c main.c)
