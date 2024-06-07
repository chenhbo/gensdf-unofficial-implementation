cmake_minimum_required(VERSION 3.16)
project(sdf_gen)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# Libigl
option(LIBIGL_WITH_OPENGL            "Use OpenGL"         ON)
option(LIBIGL_WITH_OPENGL_GLFW       "Use GLFW"           ON)
option(LIBIGL_WITH_CGAL              "Use CGAL"           ON)
include(libigl)

# Add your project files
file(GLOB SRC_FILES sdf_gen.cpp)
add_executable(${PROJECT_NAME} ${SRC_FILES})
target_link_libraries(${PROJECT_NAME} PUBLIC igl::core igl::opengl_glfw igl::cgal stdc++fs)


# cmake_minimum_required(VERSION 3.16)
# project(sdf_gen)

# list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# # set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# # Libigl
# option(LIBIGL_WITH_OPENGL            "Use OpenGL"         ON)
# option(LIBIGL_WITH_OPENGL_GLFW       "Use GLFW"           ON)
# # option(LIBIGL_WITH_CGAL              "Use CGAL"           ON)

# include(libigl)
# # # libigl
# # option(LIBIGL_WITH_OPENGL            "Use OpenGL"         ON)
# # option(LIBIGL_WITH_OPENGL_GLFW       "Use GLFW"           ON)
# # option(LIBIGL_WITH_CGAL              "Use CGAL"           ON)

# # find_package(LIBIGL REQUIRED QUIET)

# # Add your project files
# file(GLOB SRCFILES sdf_gen.cpp)
# add_executable(${PROJECT_NAME} ${SRCFILES})
# # target_link_libraries(${PROJECT_NAME} PUBLIC igl::core igl::opengl_glfw igl::cgal)
# target_link_libraries(${PROJECT_NAME} PUBLIC igl::core igl::opengl_glfw)
