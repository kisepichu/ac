#define _ENV_TQK_ //*20210208* after edit, update v/tqk.cpp and clear submit\auto\*
// %LocalAppdata%\Programs\Python\Python37\Lib\site-packages\atcodertools\tools\templates


//sub-BOF

// desktop
// author: Tqk

// #define _AOJ_
#define _C_INPUT_

#pragma region template

#pragma region basic
#define IN_FILE "./in.txt"
//#pragma GCC optimize ("O3")
#pragma warning(disable: 4455 4244 4067 4068 4996)
#pragma GCC target ("avx")
#pragma GCC diagnostic ignored "-Wliteral-suffix"
#define NOMINMAX
#ifdef _ENV_TQK_
#include <Windows.h>
#endif
#include "bits/stdc++.h"
using namespace std;
typedef int64_t lint;
typedef long double ld;
typedef string cs;
#define linf 1152921504606846976
#ifndef _AOJ_
inline lint operator""z(const unsigned long long n){ return lint(n); }
#endif
template<class T>inline T operator-(const vector<T>& a,const size_t&i){return a.at(i);}
#pragma endregion

#pragma region rep
#define _vcppunko3(tuple) _getname3 tuple
#define _vcppunko4(tuple) _getname4 tuple
#define _getname4(_1,_2,_3,_4,name,...) name
#define _getname3(_1,_2,_3,name,...) name
#define _trep2(tuple) _rep2 tuple
#define _trep3(tuple) _rep3 tuple
#define _trep4(tuple) _rep4 tuple
#define _rep1(n) for(lint i=0;i<n;++i)
#define _rep2(i,n) for(lint i=0;i<n;++i)
#define _rep3(i,a,b) for(lint i=a;i<b;++i)
#define _rep4(i,a,b,c) for(lint i=a;i<b;i+=c)
#define _tper2(tuple) _per2 tuple
#define _tper3(tuple) _per3 tuple
#define _tper4(tuple) _per4 tuple
#define _per1(n) for(lint i=n-1;i>=0;--i)
#define _per2(i,n) for(lint i=n-1;i>=0;--i)
#define _per3(i,a,b) for(lint i=b-1;i>=a;--i)
#define _per4(i,a,b,c) for(lint i=a+(b-a-1)/c*c;i>=a;i-=c)
#define rep(...) _vcppunko4((__VA_ARGS__,_trep4,_trep3,_trep2,_rep1))((__VA_ARGS__))
#define per(...) _vcppunko4((__VA_ARGS__,_tper4,_tper3,_tper2,_per1))((__VA_ARGS__))
#define _tall2(tuple) _all2 tuple
#define _tall3(tuple) _all3 tuple
#define _all1(v) v.begin(),v.end()
#define _all2(v,a) v.begin(),v.begin()+a
#define _all3(v,a,b) v.begin()+a,v.begin+b
#define all(...) _vcppunko3((__VA_ARGS__,_tall3,_tall2,_all1))((__VA_ARGS__))
#define each(c) for(auto &e:c)
#pragma endregion

#pragma region io
template<class T>
istream& operator>>(istream& is,vector<T>& vec);
template<class T,size_t size>
istream& operator>>(istream& is,array<T,size>& vec);
template<class T,class L>
istream& operator>>(istream& is,pair<T,L>& p);
template<class T>
ostream& operator<<(ostream& os,vector<T>& vec);
template<class T,class L>
ostream& operator<<(ostream& os,pair<T,L>& p);
template<class T>
istream& operator>>(istream& is,vector<T>& vec){ for(T& x: vec) is>>x;return is; }
template<class T,class L>
istream& operator>>(istream& is,pair<T,L>& p){ is>>p.first;is>>p.second;return is; }
template<class T,class L>
ostream& operator<<(ostream& os,pair<T,L>& p){ os<<p.first<<" "<<p.second;return os; }
template<class T>
ostream& operator<<(ostream& os,vector<T>& vec){ if(vec.size())os<<vec[0];rep(i,1,vec.size())os<<' '<<vec[i];return os; }
template<class T>
ostream& operator<<(ostream& os,deque<T>& deq){ if(deq.size())os<<deq[0];rep(i,1,deq.size())os<<' '<<deq[i];return os; }
template<class T>
ostream& operator<<(ostream& os,set<T>& s){ each(s)os<<e<<" ";return os; }

#ifdef _ENV_TQK_
/*
ifstream infile(IN_FILE);
template<class T>
ifstream& operator>>(ifstream& is,vector<T>& vec);
template<class T,size_t size>
ifstream& operator>>(ifstream& is,array<T,size>& vec);
template<class T,class L>
ifstream& operator>>(ifstream& is,pair<T,L>& p);
template<class T>
ifstream& operator>>(ifstream& is,vector<T>& vec){ for(T& x: vec) is>>x;return is; }
template<class T,class L>
ifstream& operator>>(ifstream& is,pair<T,L>& p){ is>>p.first;is>>p.second;return is; }
inline void fin(){}
template <class Head,class... Tail>
inline void fin(Head&& head,Tail&&... tail){ infile>>head;fin(move(tail)...); }
*/
//#include<Windows.h>
HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
inline void in(){ SetConsoleTextAttribute(hConsole,10); }
template <class Head,class... Tail>
inline void in(Head&& head,Tail&&... tail){
	SetConsoleTextAttribute(hConsole,15);
	cin>>head;in(move(tail)...);
}
#else
inline void in(){}
template <class Head,class... Tail>
inline void in(Head&& head,Tail&&... tail){ cin>>head;in(move(tail)...); }
#endif

inline bool out(){ return(cout<<'\n',0); }
template <class T>
inline bool out(T t){ return(cout<<t<<'\n',0); }
template <class Head,class... Tail>
inline bool out(Head head,Tail... tail){ cout<<head<<' ';out(move(tail)...);return 0; }
template <class T>
inline void alloc(T &c,lint s){ rep(c.size())c[i].resize(s); }
#define alc alloc
#ifdef _ENV_TQK_
inline bool deb(){ SetConsoleTextAttribute(hConsole,10); return(cout<<'\n',0); }
template <class T>
inline bool deb(T t){ return(SetConsoleTextAttribute(hConsole,12),cout<<t<<'\n',SetConsoleTextAttribute(hConsole,10),0); }
template <class Head,class... Tail>
inline bool deb(Head head,Tail... tail){
	SetConsoleTextAttribute(hConsole,12);
	cout<<head<<' ';deb(move(tail)...);return 0;
}
#define dsp(ex) sp(ex)
#define dno(ex) no(ex)
#define look(v) SetConsoleTextAttribute(hConsole,12),cout<<#v<<": ",deb(v);
#else
#define deb(...) 0
#define dsp(ex) 0
#define dno(ex) 0
#define look(v) 0
#endif

#pragma endregion

#pragma region TA
#define lin(...) lint __VA_ARGS__;in(__VA_ARGS__)
#define stin(...) string __VA_ARGS__;in(__VA_ARGS__)
#define vin(type,name,size) vector<type> name(size);in(name)
#define pb push_back
#define fi e.first
#define se e.second
#define YES(c) cout<<((c)?"YES\n":"NO\n"),0
#define Yes(c) cout<<((c)?"Yes\n":"No\n"),0
#define POSSIBLE(c) cout<<((c)?"POSSIBLE\n":"IMPOSSIBLE\n"),0
#define Possible(c) cout<<((c)?"Possible\n":"Impossible\n"),0
#define o(p) cout<<p<<endl,0
#define sp(p) cout<<p<<" ",0
#define no(p) cout<<p,0
#define st(v) sort(all(v))
#define psort(l,r) if(l>r)swap(l,r);
#define fn(ty1,ty2,ex) [&](ty1 l,ty2 r){ return(ex); }
#define lfn(ex) [&](lint l,lint r){ return(ex); }

#pragma endregion

#pragma region func
inline constexpr lint gcd(lint a,lint b){ while(b){ lint c=b;b=a%b;a=c; }return a; }
inline constexpr lint lcm(lint a,lint b){ return a/gcd(a,b)*b; }
template<typename T>
inline constexpr bool chmin(T &mn,const T &cnt){ if(mn>cnt){ mn=cnt;return 1; } else return 0; }
template<typename T>
inline constexpr bool chmax(T &mx,const T &cnt){ if(mx<cnt){ mx=cnt;return 1; } else return 0; }
template <class F>
inline void srt(F f){  }
template <class F,class Head,class... Tail>
inline void srt(F f,Head&& head,Tail&&... tail){
	vector<int>a(head.size());
	iota(all(a),0);
	sort(all(a),f);
	auto res=head;
	rep(head.size())res[i]=head[a[i]];
	head=res;
	srt(f,move(tail)...);
}
auto smaller(vector<lint>&a){
	return [&](int i,int j){return a[i]<a[j];};
}
auto larger(vector<lint>&a){
	return [&](int i,int j){return a[i]>a[j];};
}
#pragma endregion

#pragma region P

class P{ public:lint f,s; P(lint a,lint b):f(a),s(b){}; P():f(0),s(0){}; };
istream& operator>>(istream& os,P& p){ os>>p.f>>p.s;return os; }
inline constexpr bool operator<(const P& l,const P& r){ return(l.f-r.f?l.f<r.f:l.s<r.s); }
inline constexpr bool operator>(const P& l,const P& r){ return(l.f-r.f?l.f>r.f:l.s>r.s); }
inline constexpr bool operator==(const P& l,const P& r){ return(l.f==r.f&&l.s==r.s); }
inline constexpr bool operator!=(const P& l,const P& r){ return(l.f!=r.f||l.s!=r.s); }
inline P operator+(const P& l,const P& r){return P(l.f+r.f,l.s+r.s);}
inline P operator-(const P& l,const P& r){return P(l.f-r.f,l.s-r.s);}
inline P operator-(const P& r){return P(-r.f,-r.s); }
inline P operator*(const lint& l,const P& r){return P(l*r.f,l*r.s); }
inline P operator/(const P& l,const lint& r){return P(l.f/r,l.s/r); }
inline ld abs(P p){return sqrtl(p.f*p.f+p.s*p.s);}
inline ld mabs(P p){return abs(p.f)+abs(p.s);}
inline ld mht(P x,P y){return mabs(x-y);}

#pragma endregion

#pragma region start
struct Start{
	Start(){
#ifndef _C_INPUT_
		cin.tie(0),cout.tie(0);
		ios::sync_with_stdio(0);
#endif
		cout<<fixed<<setprecision(16);
	}
} __start;
#pragma endregion

#pragma endregion

#pragma region const
#define mod 1000000007
const ld pi=acos(-1);
const ld tau=(1.+sqrtl(5))/2.;
P d4[4]={P(1,0),P(0,1),P(-1,0),P(0,-1)};
P d8[8]={P(1,0),P(1,1),P(0,1),P(-1,1),P(-1,0),P(-1,-1),P(0,-1),P(1,-1)};
const cs AUTO_YES = "Yes";
const cs AUTO_NO = "No";
int cho(bool c,cs yes=AUTO_YES,cs no=AUTO_NO){
	return out((c?yes:no));
}
#pragma endregion

#pragma region solve

int solve(lint a, lint b){
	out(b+(a-b)/3.);
	return 0;
}

#pragma endregion

#pragma region main

int main(){
	lint A;
	scanf("%lld",&A);
	lint B;
	scanf("%lld",&B);
	solve(A, B);
	return 0;
}

#pragma endregion

//sub-EOF
