#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <iostream>

using namespace std;

int main(){
	int t;
	scanf("%d\n", &d);
	int b[t], b_;
	int min = 100000, max = 0, i1 = 0, i2 = 0;
	int r[t];
	int i = 0;
	while(i < t){
		for(int cnt = 0; cnt < t; cnt++){
			scanf("%d", b_);
			b[cnt] = b_;
			if(b[cnt] < min){
				min = b[cnt];
				i1 = cnt;
			}
			if(b[cnt] > max){
				max = b[cnt];
				i2 = cnt;
			}
		}
		for(int cnt = 0; cnt < t; cnt++){
			r[t] = 0;
			if((b[cnt] < max) && (b[cnt] > min)){
				rt = b[cnt];
			}else{
				if((b[cnt] <= max) && (b[cnt] >= min)){
					rt = b[cnt];
				}
			}
		}
	}
	
}
