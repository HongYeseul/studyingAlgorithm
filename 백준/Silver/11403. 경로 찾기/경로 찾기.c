#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES	100	
#define INF	1000000	/* 무한대 (연결이 없는 경우) */


typedef struct GraphType {
	int n;	// 정점의 개수
	int weight[MAX_VERTICES][MAX_VERTICES];
} GraphType;
GraphType g;
int A[MAX_VERTICES][MAX_VERTICES];
void input(){
	scanf("%d",&g.n);
	int i,j;
	for(i=0; i<g.n ; i++)
		for(j=0 ; j<g.n ; j++)
			scanf("%d",&g.weight[i][j]);
}
void floyd()
{
	int i, j, k;
	for (i = 0; i<g.n; i++){
		for (j = 0; j<g.n; j++){
			if(g.weight[i][j] == 0) 
				A[i][j] = INF;
			else A[i][j] = g.weight[i][j];
		}
	}
	for (k = 0; k<g.n; k++) {
		for (i = 0; i<g.n; i++)
			for (j = 0; j<g.n; j++)
				if (A[i][k] + A[k][j] < A[i][j])
					A[i][j] = A[i][k] + A[k][j];
	}
}

void print_dap(){
	int i,j;
	for(i=0 ; i<g.n ; i++){
		for(j=0 ; j<g.n ; j++){
			if(A[i][j] == INF) printf("0 ");
			else printf("1 ");
		} printf("\n");
	}
}

int main(void)
{
	input();
	floyd();
	print_dap();
	return 0;
}
