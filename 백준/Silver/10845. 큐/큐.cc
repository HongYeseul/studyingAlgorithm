#include <stdio.h>
#include <queue>
#include <string.h>
using namespace std;

queue<int> q;

int main(void){
	int n;
	int num;
	char str[10]={0};
	scanf("%d",&n);
	
	for(int i=0; i<n; i++){
		scanf("%s", str);
		if(!strcmp(str,"push")){
			scanf("%d", &num);
			q.push(num);
		}else if(!strcmp(str,"pop")){
			if(q.size()>0){
				printf("%d\n", q.front());
				q.pop();
			}
			else
				printf("-1\n");
		}else if(!strcmp(str, "size")){
			printf("%d\n", q.size());
		}else if(!strcmp(str, "empty")){
			printf("%d\n",q.empty());
		}else if(!strcmp(str,"front")){
			if(q.size()>0)
				printf("%d\n",q.front());
			else
				printf("-1\n");
		}else if(!strcmp(str,"back")){
			if(q.size() > 0)
				printf("%d\n", q.back());
			else
				printf("-1\n");
		}
	}
	
	return 0;
}