#include<iostream>
using namespace std;

int main()
{
int i,j;
int a[100][100];
for(int i=1;i<=3;i++){
    for(int j=1;j<=3;j++)
    {
        cout<<"\nEnter the elements a"<<i<<j<<":";
        cin>>a[i][j];
    }

}



for(int i=1;i<=3;i++){
    for(int j=1;j<=3;j++)
    {
        cout<<a[i][j]<<"\t";
    }
    cout<<endl;
}
    
};
