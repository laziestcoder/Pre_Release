#include<bits/stdc++.h>
using namespace std;

void QBSort(int A[1000], int n){
	bool k = false, m = 0, i = 0;
	for (i = 0, j = n-1; i <= j; i++, j--){
		if( A[i] > A[j] ){
			int t;
			t = A[i];
			A[i] = A[j];
			A[j] = t;
		}
	}

	for(i = 0, j = n-1; i <= j; i++, j-- ){
		if( A[i] <= A[i+1] && A[j] >= A[j-1] ){
			continue;
		}else{
			k = true;
		}
	}

	while( k ){
		k = false;
		for( i = 0; i < n-1; i++ ){
			if( A[i] > A[i+1] ){
				int t;
				t = A[i];
				A[i] = A[i+1];
				A[i+1] = t;
				k = true;
			}
		}
	}

	m++;
}

int main (){
	int n = 0, i, A[1000];
	cin >> n;
	for ( i = 0; i < n; i++ ){
		cin >> A[i];
	}

	QBSort(A, n);

	for (i = 0; i < n; i++ ){
		cout << A[i] << " " ;
	}


	return 0;
}
