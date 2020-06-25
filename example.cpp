#include "bits/stdc++.h"
using namespace std;

int main(){
	string s; cin>>s;
	for(int i=0; i<3; ++i){
		if(s[0]>'Z'){cout<<'a'<<endl;return -1;}
		else cout<<"A"<<endl;
	}
	while(1);
}