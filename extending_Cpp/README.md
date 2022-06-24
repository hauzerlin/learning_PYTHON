reference website:
https://iter01.com/373609.html

呼叫c
不僅可以用於python，也可以用於其他java/perl/ruby/php/JavaScript/Go。

```
/* great_module.i */
%module great_module
%{
int great_function(int a) {
    return a + 1;
}
%}
int great_function(int a);
```

定義module名稱通常和檔名保持一致。
%{%}包裹的部分是c語言程式碼，這段程式碼會原封不動的複製到mymodule_wrap.c
欲匯出的函式簽名列表。直接從標頭檔案中複製過來即可

```
$ swig -c++ -python great_module.i
```

會生成對應的great_module_wrap.c和great_module.py檔案

再執行：

```
$ g++ -fPIC -shared great_class_wrap.cxx -o _great_class.so  -I/usr/include/python2.7/ -lpython2.7
```

生成對應的_great_module.so檔案，這時，我們就可以再python中直接呼叫了

```
from great_module import great_function

print great_function(9)

>>> 10
```

呼叫c++
定義一個標頭檔案，great_class.h

```
#ifndef GREAT_CLASS
#define GREAT_CLASS
class Great {
    private:
        int s;

    public:
        void setWall (int _s) {s = _s;};
        int getWall() {return s;};
};
#endif
```

再定義一個great_class.i的swig配置檔案，這裡不用再寫一遍SWIG的定義了，直接使用SWIG的%include指令；
在SWIG編譯時要加-c++這個選項，生成的副檔名為cxx。

```
/* great_class.h */

%module great_class
%{
#include "great_class.h"
%}
%include "great_class.h"
```

執行命令：

```
$ swig -c++ -python great_class.i
```

在Linux下，使用C++編譯器g++

```
$ g++ -fPIC -shared great_class_wrap.cxx -o _great_class.so  -I/usr/include/python2.7/ -lpython2.7
```

生成對應的_great_class.so檔案。現在可以直接在python中輸入

```
import great_class
c = great_class.Great()
c.setWall(10)
print c.getWall()

>>> 10
```

