/*
Chanon Panpila 5922793468
OS_Homework sec 2

SIIT Student

Editor VSCODE :: using CLI - Cygwin $sudo c++ fileName.cpp
Version :: Cpp 17
*/

// $sudo c++ fileName.cpp

#include <iostream>
#include <stdlib.h>
#include <thread>

using namespace std;

bool flag[2] = {0, 0};
int turn;
int counts = 0;

void _Counter(int process) {

  printf("Process In = : %d\n", process);

  flag[process] = 1;
  turn = 1 - process;

  while (flag[1 - process] == 1 && turn == 1 - process) {
  };

  for (int i = 0; i < 10000; i++)
    counts++;

  flag[process] = 0;
}

int main() {

  thread t1(_Counter, 0), t2(_Counter, 1);
  t1.join();
  t2.join();

  cout << "Counts ++ = " << counts;

  return 0;
}