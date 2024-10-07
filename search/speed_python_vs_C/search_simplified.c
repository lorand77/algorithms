#define N 100000000
#include <stdio.h>

int main() {
    static int x[N];
    for (int i=0; i<N; i++) {
        x[i] = i;
    }

    static int ix;
    for (int i=0; i<N; i++) {
        if (x[i] == N/2) {
            ix = i;
            break;
        }
    }

    printf("%d\n",ix);
}