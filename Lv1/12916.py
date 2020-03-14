#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int i;
    int p=0;
    int y=0;
    for (i=0; i<s.size(); i++){
        s[i]=tolower(s[i]);
        if (s[i]=='p'){
            p++;
        }
        else if(s[i]=='y'){
            y++;
        }
    }
    
    if (p!=y){
        answer = false;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    //cout << "Hello Cpp" << endl;

    return answer;
}