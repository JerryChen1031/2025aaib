///week03-4.cpp
///M90H044
#include <stdio.h>
int main()
{
	int ans = 0;
	///�j��e��ans�O0
	int N;///���@�Ӿ��N
	scanf("%d", &N);///Ū�J N
	///�H�����j��q0�}�l
	for(int i=1; i<=N; i++){
		ans += i;///�j�餤���ק�ans
	}
	printf("%d", ans);
}///�j��᭱,�L�Xans
