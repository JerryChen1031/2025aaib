///week03-4.cpp
///M90H044
#include <stdio.h>
int main()
{
	int ans = 0;
	///迴圈前面ans是0
	int N;///有一個整數N
	scanf("%d", &N);///讀入 N 
	///人類的迴圈從0開始
	for(int i=1; i<=N; i++){
		ans += i;///迴圈中間修改ans
	}
	printf("%d", ans);
}///迴圈後面,印出ans
