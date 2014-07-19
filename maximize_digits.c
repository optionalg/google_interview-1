#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Twitter
//maximize a number by re-arrganging its digits. e.g. 3515 -> 5531

int main() {
  //negative?
  int N = 30515, r=0;
  int cnt[10];
  memset(cnt,0,sizeof(cnt));//sz=40
  while(N>0) {
    cnt[N%10]++;
    N/=10;
  }
  //for(int i=0;i<10;i++) printf("%d\n", cnt[i]);
  for(int i=9;i>=0;i--) {
    while(cnt[i]>0) {
      r=r*10+i;
      --cnt[i];
    }
  }
  printf("%d\n", r);
  return 0;
}
