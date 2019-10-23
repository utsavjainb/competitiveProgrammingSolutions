#include <iostream>
#include <algorithm>

using namespace std;


int phrases(int k, int j) {
    if (k == 0 || j == 0)
        return 0;
    //return (k+j)/3;
    int lesser = min(k, j);
    int bigger = max(k, j);
    int count = 0;
    
    while( bigger >= 2 && lesser >= 1){
        bigger -= 2;
        lesser -= 1;
        count++;
    }
    
    while( lesser >= 2 && bigger >= 1){
        lesser -= 2;
        bigger -= 1;
        count++;
    }
    return count;
    
}

int main() {
    int k;
    int j;
    cin >> k >> j;
    int answer = phrases(k, j);
    cout << answer;
    return 0;
}