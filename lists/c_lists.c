#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
    int *array;     // Pointer to the array of elements
    int size;       // Current number of elements
    int capacity;   // Maximum capacity of the array
} DynamicArray;

DynamicArray* createArray(int capacity) {
    DynamicArray *dynamicArray = (DynamicArray*)malloc(sizeof(DynamicArray));
    dynamicArray->array = (int*)malloc(capacity * sizeof(int));
    dynamicArray->size = 0;
    dynamicArray->capacity = capacity;
    return dynamicArray;
}

void resizeArray(DynamicArray *dynamicArray) {
    int newCapacity = dynamicArray->capacity * 2;
    dynamicArray->array = (int*)realloc(dynamicArray->array, newCapacity * sizeof(int));
    dynamicArray->capacity = newCapacity;
}

void append(DynamicArray *dynamicArray, int value) {
    if (dynamicArray->size == dynamicArray->capacity) {
        resizeArray(dynamicArray);
    }
    dynamicArray->array[dynamicArray->size] = value;
    dynamicArray->size++;
}

void insert(DynamicArray *dynamicArray, int index, int value) {
    if (index < 0 || index > dynamicArray->size) {
        printf("Index out of bounds\n");
        return;
    }
    if (dynamicArray->size == dynamicArray->capacity) {
        resizeArray(dynamicArray);
    }
    if (index < dynamicArray->size) {
        // Use memcpy to shift elements to the right
        memcpy(&dynamicArray->array[index + 1], &dynamicArray->array[index], 
               (dynamicArray->size - index) * sizeof(int));
    }
    dynamicArray->array[index] = value;
    dynamicArray->size++;
}

void delete(DynamicArray *dynamicArray, int index) {
    if (index < 0 || index >= dynamicArray->size) {
        printf("Index out of bounds\n");
        return;
    }
    if (index < dynamicArray->size - 1) {
        // Use memcpy to shift elements to the left
        memcpy(&dynamicArray->array[index], &dynamicArray->array[index + 1], 
               (dynamicArray->size - index - 1) * sizeof(int));
    }
    dynamicArray->size--;
}

int find(DynamicArray *dynamicArray, int value) {
    for (int i = 0; i < dynamicArray->size; i++) {
        if (dynamicArray->array[i] == value) {
            return i;
        }
    }
    return -1;
}

void measureTime() {
    DynamicArray *dynamicArray = createArray(1000000);
    for (int i = 0; i < 1000000; i++) {
        append(dynamicArray, i);
    }

    int value = 100;
    int index;
    clock_t start, end;

    // Measure average append time (10,000 times)
    start = clock();
    for (int i = 0; i < 10000; i++) {
        append(dynamicArray, i);
    }
    end = clock();
    printf("Average append time: %f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 10000) * 1000);

    // Measure average element access time (v = x[i]) (100,000 times)
    start = clock();
    for (int i = 0; i < 100000; i++) {
        int element = dynamicArray->array[i % dynamicArray->size];
    }
    end = clock();
    printf("Average element access time: %.9f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 100000) * 1000);

    // Measure average assignment time (x[i] = v) (100,000 times)
    start = clock();
    for (int i = 0; i < 100000; i++) {
        dynamicArray->array[i % dynamicArray->size] = value;
    }
    end = clock();
    printf("Average assignment time: %.9f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 100000) * 1000);

    // Measure average insert time at middle (1,000 times)
    start = clock();
    for (int i = 0; i < 1000; i++) {
        insert(dynamicArray, dynamicArray->size / 2, value);
    }
    end = clock();
    printf("Average insert time: %f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 1000) * 1000);

    // Measure average delete time from middle (1,000 times)
    start = clock();
    for (int i = 0; i < 1000; i++) {
        delete(dynamicArray, dynamicArray->size / 2);
    }
    end = clock();
    printf("Average delete time: %f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 1000) * 1000);

    // Measure average find time (1,000 times)
    start = clock();
    for (int i = 0; i < 1000; i++) {
        index = find(dynamicArray, 500000);  // Searching for an element in the middle
    }
    end = clock();
    printf("Average find time (for value 500000): %f ms\n", ((double)(end - start) / CLOCKS_PER_SEC / 1000) * 1000);

    free(dynamicArray->array);
    free(dynamicArray);
}

int main() {
    measureTime();
    return 0;
}



/*
                                                        vs Python
Average element access time: 0.000 003 ms                10x
Average assignment time: 0.000 002 ms

Average append time: 0.000 011 ms                         4x

Average insert time: 0.106805 ms                          4x (memcpy)
Average delete time: 0.102407 ms

Average find time (for value 500000): 1.166697 ms         5x

*/