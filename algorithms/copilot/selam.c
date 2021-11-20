#include <stdio.h>

int main() {
    // write a program that gets mouse clicks and prints the x and y coordinates of the click

    int x, y;
    while (1) {
        getmouse(&x, &y);
        printf("%d %d\n", x, y);
    }

}

void getmouse(int *x, int *y) {
    // get mouse click
    // x and y are pointers to integers
    // x and y are the coordinates of the mouse click
    // return nothing
    //
    // example:
    // int x, y;
    // getmouse(&x, &y);
    // printf("%d %d\n", x, y);
}