Title: C++
Date: 2018-02-19
Modified: 2010-12-04 19:30
Category: C++
Slug: C++
Summary: C++


### Useful C++ snippets

#### useful headers
```
#include <iostream>
#include <string>
#include <typeinfo>
#include <math.h> # to use fabs() to get the absolute value of a double
#include <Rcpp.h>
using namespace Rcpp ;
using std::cout ;
```

#### ensure that R Studio console prints out decimals
```
cout.precision(4) ;
cout.setf(std::ios::fixed) ;
```

#### print statement
```
cout << "x is of type: "<< typeid(x).name() << std::endl ;
```

```
/*** R 
# Does the function give the same results as R's weighted.mean() function?
all.equal(weighted_mean_cpp(x, w), weighted.mean(x, w))
*/
```

#### Rcpp

* [High performance functions with Rcpp](http://adv-r.had.co.nz/Rcpp.html)
* [STL Data Structures](http://www.cplusplus.com/reference/stl/)
* [C++ <algorithm> header](http://www.cplusplus.com/reference/algorithm/)
* [Sets](http://www.cplusplus.com/reference/set/set/)
* [Boost C++ libraries](https://www.boost.org/doc/)


### Rcpp, C++ and Visual Studio Code

* Including the header Rcpp.h only works if the code is executed / compiled from RStudio
* Compiling a pure cpp file without Rcpp export does NOT require an Rcpp header include. If you do yo will get 
an error: `Rcpp.h: No such file or directory`.

#### `task.json`
```
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "label": "build",
      "command": "g++",
      "args": [
        "./MCQ/mcq1.cpp",
        "-o",
        "${workspaceFolderBasename}"
      ],
      "problemMatcher": []
    },
    {
      "type": "shell",
      "label": "run",
      "command": "./${workspaceFolderBasename}",
      "dependsOn": [
        "build"
      ],
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```


#### C++ related Help Files

* `?cxxfunction`


#### Links

* [C++ Reference](http://www.cplusplus.com/reference/)
* [Locating/downloading header files R.h and Rmath for C interfacing with R](https://stackoverflow.com/questions/31339853/locating-downloading-header-files-r-h-and-rmath-for-c-interfacing-with-r)
* [Data structures and algorithms problems in C++ using STL](https://medium.com/techie-delight/data-structures-and-algorithms-problems-in-c-using-stl-7900a6ddb1d4)
* [STL Containers in C++](https://medium.com/sisgrammers/stl-containers-in-c-a95d0b0aa45a)