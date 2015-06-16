.. quantdigger documentation master file, created by
   sphinx-quickstart on Sun May 17 16:47:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

quantdigger 文档
================

介绍
~~~~
QuantDigger目前是一个基于python的量化回测框架。作者最初是因为对数据处理和机器学习感兴趣而选择了这个行业，
接触了一些主流的期货交易软件，比如TB, 金字塔。他们的特点是语法比较简单，缺点是编程语言太封闭，有很多表达限制。
所以选择自己开发一个交易系统，做为交易和研究的工具，甚至尝试过商业化。最初选择c++做为实现语言，但是后面
发现开发效率太低，重要的是做为研究工具来说，其易用性和和扩展性都比不上基于python的回测框架。相比其它流行的
回测框架比如 zipline_ , pyalgotrade_ ，QuantDigger的策略语法更简单，类似MC，TB这些商业软件，但并不牺牲灵活性，保留了python这门通用语言的
所有功能。QuantDigger目前还是定位于研究工具，但是设计上还是会从实盘交易的角度考虑，将来也会接入交易接口。虽然有很多细节还有待完善， 
但是核心的设计和功能已经实现了。代码也比较简单，大家有兴趣的可以自己拓展。 如果大家有什么问题和建议，欢迎加入我们的QQ交流群--334555399，或者
联系发起者(yellowblue QQ:33830957) 。 在项目的推进过程中得到很多人的帮助, 在这表示感谢！
除了开发人员，还要特别感谢北京的 vodkabuaa_ 和国元证券的王林峰给出的意见， ongbe_ 帮忙修复代码bug， tushare_ 库的作者 Jimmy_ 和深大的邓志浩帮忙推荐
这个库，以及所有朋友的支持。

**代码主要贡献者:**
     deepfish_

     TeaEra_

     wondereamer_

     HonePhy_

版本
~~~~
**0.16版本 日期待定**

* 清理旧代码和数据文件
* 重新设计数据模块
* 改善UI, 补充UI文档
    
**0.15版本 2015-06-16**

* 夸品种的策略回测功能
* 简单的交互
* 指标，k线绘制

系统文件结构
~~~~~~~~~~~~

* quantdigger

  * kernel 核心功能代码

    * engine 交易引擎模块
    * datasource 数据模块
    * indicators 指标模块
    * datastruct.py 核心数据结构

  * widgets 交互界面
  * demo 示例
  * backup 待整理的代码
  * digger 待整理的代码

.. _pyalgotrade: https://github.com/gbeced/pyalgotrade
.. _zipline: https://github.com/quantopian/zipline
.. _TeaEra: https://github.com/TeaEra
.. _deepfish: https://github.com/deepfish
.. _wondereamer: https://github.com/wondereamer
.. _HonePhy: https://github.com/HonePhy
.. _ongbe: https://github.com/ongbe
.. _tushare: https://github.com/waditu/tushare
.. _Jimmy: https://github.com/jimmysoa
.. _vodkabuaa: https://github.com/vodkabuaa

目录:
~~~~~

.. toctree::
    
    tutorial
    documents



索引和表格
~~~~~~~~~~

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
