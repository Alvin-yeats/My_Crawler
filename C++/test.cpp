#include "StdAfx.h"

#include <string>
#include <iostream>



//解析URL，解析出主机名，资源名  
bool ParseURL( const string & url, string & host, string & resource){  
    if ( strlen(url.c_str()) > 2000 ) {  
        return false;  
    }  
  
    const char * pos = strstr( url.c_str(), "http://" );  
    if( pos==NULL ) pos = url.c_str();  
    else pos += strlen("http://"); 

    if( strstr( pos, "/")==0 )  
        return false;

    char phost[100] = {'\0'};
	char presource[100] = {'\0'};

    sscanf_s( pos, "%[^/]%s", &pHost, 100, &pResource, 100);  
    host = pHost;  
    resource = pResource;  
    return true;  
}  

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{	
	const string url = "www.baidu.com";

	
	const char* pos = strstr( url.c_str(), "www.baidu.com");
	if( pos == NULL ) pos = url.c_str();
	else pos += strlen("http://");

	/*if( strstr( pos, "/") == NULL)
		return false;*/

	char phost[100] = {'\0'};
	char presource[100] = {'\0'};
	sscanf( pos, "%[^/]%s", phost, presource);
	string host(phost);
	string resource(presource);

	cout << host << "  ,  " << resource;
	return 0;
}
