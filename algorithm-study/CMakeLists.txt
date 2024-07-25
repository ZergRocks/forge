# CMake 프로그램의 최소 버전
cmake_minimum_required(VERSION 3.11)

# 프로젝트 정보
project(
  ModooCode
  VERSION 0.1
  DESCRIPTION "algorithm-study"
  LANGUAGES CXX)

# 소스 파일 자동 검색
file(GLOB SOURCES "src/*.cpp")

# 실행 파일 생성
# 각 실행 파일 이름은 "program1", "program2", ... 로 설정합니다.
foreach(source_file ${SOURCES})
    # 파일의 이름을 가져옵니다.
    get_filename_component(file_name ${source_file} NAME_WE)

    # "program"이라는 접두사를 붙여 실행 파일 이름을 설정합니다.
    set(executable_name "program_${file_name}")

    # 실행 파일을 생성합니다.
    add_executable(${executable_name} ${source_file})
endforeach()
