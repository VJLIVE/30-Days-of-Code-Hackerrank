#include <iostream>
#include <map>
int main(){
    int n;
    std::cin>>n;
    std::map<std::string,int>phonebook;
    for (int i=0;i<n;++i){
        std::string name;
        int number;
        std::cin>>name>>number;
        phonebook[name]=number;
    }
    std::string query;
    while(std::cin>>query){
        if(phonebook.count(query)){
            std::cout<<query<<"="<<phonebook[query]<<std::endl;
        }else{
            std::cout<<"Not found"<<std::endl;
        }
    }
    return 0;
}
