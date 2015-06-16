安装
====
pip安装 (推荐)
   
  ::
       
      python install_pip.py  (如果已经安装了pip,略过这一步。)
      pip install QuantDigger
      python install_dependency.py

或者克隆github代码后本地安装
   
  ::
       
      git clone https://github.com/QuantFans/quantdigger.git
      python install.py  (会根据情况安装pip, 及依赖包)


**依赖库**

* Python 
* pandas 
* python-dateutil 
* matplotlib 
* numpy
* TA-Lib
* logbook
* pyqt (可选)
* tushare_ (可选, 一个非常强大的股票信息抓取工具)

.. _tushare: https://github.com/waditu/tushare
