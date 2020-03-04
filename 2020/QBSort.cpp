#include<bits/stdc++.h>
using namespace std;

int*  QBSort(int A[1000], int n){
	bool k = false;
	int m = 0, i = 0, j = 0;
	for (i = 0, j = n-1; i <= j; i++, j--){ // This loop runs 'n-1' time . So we can consider it as 'n' times
		if( A[i] > A[j] ){
			int t;
			t = A[i];
			A[i] = A[j];
			A[j] = t;
		}
	}

	for(i = 0, j = n-1; i <= j; i++, j-- ){   // This loop also runs 'n' time
		if( A[i] <= A[i+1] && A[j] >= A[j-1] ){
			continue;
		}else{
			k = true;
		}
	}

	while( k ){ // This can be iterate at max 'm' times
		k = false;
		for( i = 0; i < n-1; i++ ){ // This loop also runs 'n' time
			if( A[i] > A[i+1] ){
				int t;
				t = A[i];
				A[i] = A[i+1];
				A[i+1] = t;
				k = true;
			}
		}
		m++;

		//So this while loop can iterate 'm' times and for loop 'n' times
		//the relation between while and for loop is => while * for
		//So the Complexity is m*n, and we can consider m=n, so it will become n*n=> n^2 [n square] 
	}

	return A;
}

/*	We will cosider the highest value. So the highest value is 'n^2' and the complexity is 
*	O(n*n)=O(n^2) , it is called 'Big-O-n-square'. It means the time complexity is 'n^2' and depends on value of 'n'.
*
*/
int main (){
	int n = 0, i, A[1000];
	cin >> n;
	for ( i = 0; i < n; i++ ){
		cin >> A[i];
	}

	int *B = QBSort(A, n);

	for (i = 0; i < n; i++ ){
		cout << B[i] << " " ;
	}


	return 0;
}
