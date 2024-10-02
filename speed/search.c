#define N 100000000
#include<stdio.h>
#include <time.h>


int find(int x[], int n, int v) {
    for (int i=0; i<n; i++) {
        if (x[i] == v) {
            return(i);
        }
    }
    return(-1);
}


int main() {
    static int x[N];
    for (int i=0; i<N; i++) {
        x[i] = i;
    }

    static int ix = -1;
    clock_t start, end;

    start = clock();
    ix = find(x, N, N/2);
    end = clock();

    double elapsed = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("%d  %f\n",ix,elapsed);
}