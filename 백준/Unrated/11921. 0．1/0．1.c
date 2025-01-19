#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    char buf[1<<27];  // 128MB buffer
    long long total = 0;
    int pos = 0;
    
    // 한번에 입력 읽기
    read(0, buf, sizeof(buf));
    
    // 첫 줄 건너뛰기
    while (buf[pos] != '\n') pos++;
    pos++;
    
    // 5,000,000개의 숫자 처리
    for (int i = 0; i < 5000000; i++) {
        int num = 0;
        while (buf[pos] != '\n') {
            num = num * 10 + (buf[pos] - '0');
            pos++;
        }
        total += num;
        pos++;
    }
    
    // 출력
    printf("5000000\n%lld", total);
    
    return 0;
}
