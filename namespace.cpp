#include <iostream>
namespace first{
    int x = 1;
}
namespace seco{
    int x = 2;
}
int main(){
    using namespace std;
    using namespace first;
    //int x = 0;
    //version 4
    int a = 10 ; int b = 88 ; int c = 99;
    cout <<a+b+c << std:: endl;
    cout <<seco::x ;
    
    return 0;
}                                                                                                               