# 定义编译器和编译选项
CXX = g++
CXXFLAGS = -Wall -O2

# 定义源文件和目标文件列表
SRCS = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp, %.o, $(SRCS))
EXE = myprogram

# 定义编译规则
all: $(EXE)

$(EXE): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# 定义清理规则
clean:
	rm -f $(OBJS) $(EXE)