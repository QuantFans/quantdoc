指标示例
========

算术平均指标类
~~~~~~~~~~~~~~

.. code:: py

    class MA(IndicatorBase):
        """ 移动平均线指标。 """
        @create_attributes
        def __init__(self, tracker, prices, n, name='MA', color='y', lw=1, style="line"):
            super(MA, self).__init__(tracker, name)
            # self.value为任何支持index的数据结构。
            self.value = self._moving_average(prices, n)

        def _moving_average(self, data, n):
            """ 向量化运行的均值函数。 """
            data = transform2ndarray(data)
            return talib.SMA(data, n)

        def plot(self, widget):
            self.widget = widget
            self.plot_line(self.value, self.color, self.lw, self.style)

所有的指标都继承与IndicatorBase类。IndicatorBase定义了很多转化函数，使指标对象能像时序变量一样被使用。
此指标使用了TA-Lib库函数，向量化运行后赋值给value属性，任何指标类都必须定义这个属性。

plot函数负责在参数widget上绘制指标线。plot_line函数负责画线，定义于IndicatorBase的父类。它会根据
widget类型做相应的绘图操作，widget可以是任何绘图设备，比如matplotlib的Axes, 或者pyqt的QFrame(只实现了接口)。
如果用户不需要绘制指标，那么无需定义plot函数。

算术平均线绘制
~~~~~~~~~~~~~~~

.. code:: py

    # -*- coding: utf8 -*-
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    from quantdigger.kernel.indicators.common import MA
    from quantdigger.kernel.datasource.data import csv2frame

    # 创建画布
    fig, ax = plt.subplots()
    # 加载数据
    price_data = csv2frame("IF000.SHFE-10.Minute.csv")
    # 创建平均线指标
    ma10 = MA(None, price_data.close, 10, 'MA10', 'y', 2)
    ma20 = MA(None, price_data.close, 60, 'MA10', 'b', 2)
    # 绘制指标
    ma10.plot(ax)
    ma20.plot(ax)
    plt.show()

.. image:: _static/plot_ma.png
 :width: 500px


非向量化运行的指标函数
~~~~~~~~~~~~~~~~~~~~~~
如果你觉的这个指标类太复杂了，那么可以这样定义和使用指标函数。

.. code:: py

    def ma(series, n):
        """ 算术平均指标函数。

        series (NumberSeries): 序列变量
        n (int): 周期
        """ 
        sum_ = 0
        try:
            for i in range(0, n):
                sum_ += series[i]
            return sum_ / n
        except IndexError:
            return 0

    class DemoStrategy(TradingStrategy):
        """ 策略实例 """
        def __init__(self, exe):
            super(DemoStrategy, self).__init__(exe)
            # 创建时序变量，用来保存指标值。
            self.ma10 = NumberSeries(self)

        def on_bar(self):
            # 更新时序变量的最新值。
            self.ma10.append(ma(self.open, 10))
            print self.ma10

