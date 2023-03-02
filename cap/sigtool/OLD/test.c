#include <stdio.h>

int main(){
    int i;
    for (i=0; i<256; i++){
        printf("%x,%c,\n", i, i);
    }
}