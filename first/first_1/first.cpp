#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <iostream>

using namespace std;

char * compare(int a[], int b[], int t);

int main(){
	int t;
	scanf("%d", &t);
	int a[t], b[t];
	int a_, b_;
	char r[t];
	int cnt;
	for(cnt = 0; cnt < t; cnt++){
		scanf("%d", &a_);
		a[cnt] = a_;
		scanf("%d", &b_);
		b[cnt] = b_;
		if(a[cnt] < b[cnt])
			r[cnt] = '<';
		else if(a[cnt] == b[cnt])
			r[cnt] = '=';
		else
			r[cnt] = '>';
	}
	for(cnt = 0; cnt < t; cnt++){
		printf("%c\n", r[cnt]);
	}
	
}
