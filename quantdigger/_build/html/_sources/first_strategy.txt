
一个简单的策略
==============

策略代码
~~~~~~~~

.. code:: py

    from quantdigger.kernel.engine.execute_unit import ExecuteUnit
    from quantdigger.kernel.indicators.common import MA, BOLL
    from quantdigger.kernel.engine.strategy import TradingStrategy
    from quantdigger.util import  pcontract
    import plotting

    class DemoStrategy(TradingStrategy):
        """ 策略实例 """
        def __init__(self, exe):
            super(DemoStrategy, self).__init__(exe)
            # 创建平均线指标和布林带指标。其中MA和BOLL表示指标函数类。
            # 它们返回序列变量。
            # 'ma20'：指标名. 'b'画线颜色. ‘1‘: 线宽。如果无需
            # 绘图，则这些参数不需要给出。
            self.ma20 = MA(self, self.close, 20,'ma20', 'b', '1')
            self.ma10 = MA(self, self.close, 10,'ma10', 'y', '1')
            self.b_upper, self.b_middler, self.b_lower = BOLL(self, self.close, 10,'boll10', 'y', '1')

        def on_bar(self):
            """ 策略函数，对每根Bar运行一次。""" 
            if self.ma10[1] < self.ma20[1] and self.ma10 > self.ma20:
                self.buy('long', self.open, 1, contract = 'IF000.SHFE') 
            elif self.position() > 0 and self.ma10[1] > self.ma20[1] and self.ma10 < self.ma20:
                self.sell('long', self.open, 1) 

            # 输出pcon1的当前K线开盘价格。
            print(self.open)

            # 夸品种数据引用
            # pcon2的前一根K线开盘价格。
            print(self.open_(1)[1])

    if __name__ == '__main__':
        try:
            # 策略的运行对象周期合约
            pcon1 = pcontract('IF000.SHFE', '10.Minute')
            pcon2 = pcontract('IF000.SHFE', '10.Minute')
            # 创建模拟器，这里假设策略要用到两个不同的数据，比如套利。
            simulator = ExecuteUnit([pcon1, pcon2]);
            # 创建策略。
            algo = DemoStrategy(simulator)
            # 运行模拟器，这里会开始事件循环。
            simulator.run()

            # 显示回测结果
            plotting.plot_result(simulator.data[pcon], algo._indicators,
                                algo.blotter.deal_positions, algo.blotter)
    
        except Exception, e:
            print(e)

示例策略代码很简单，其中TradingStrategy是策略的基类，实现了策略的接口，比如下单，持仓查询等。
模拟器负责加载数据，你可以通过它同时运行一个或多个策略(创建多个策略实例)。也就是数据和策略间
一对多的关系。 如果要在数据和策略间做多对多的回测，则要运行多个模拟器实例。 模拟器的run()函数
会启动事件循环，核心代码如下：

.. code:: py

        # 遍历每根Bar数据，运行所有策略。
        bar_index = 0
        while bar_index < self._data_length:
            .....
            # 遍历每个策略。
            for algo in self._strategies:
                # 更新策略的当前Bar索引
                bar = algo.update_curbar(bar_index)
                # 更新模拟交易所的当前时间。
                algo.exchange.update_datetime(bar.datetime)
                # 更新订单器的当前时间和最新的Bar数据。
                algo.blotter.update_datetime(bar.datetime)
                latest_bars[algo._main_contract] = bar
                algo.blotter.update_bar(latest_bars)
                # 对新的Bar运行一步策略。
                algo.execute_strategy()
                # 根据这一步的运行结果，比如是否开仓，可能
                # 会引发一系列的事件。
                while True:
                    try:
                        # 获取可能的事件。
                        event = algo.events_pool.get()
                    except Queue.Empty:
                        # 没有待处理事件，退出。
                        break
                    except IndexError:
                        # 索引错误，退出。
                        break
                    else:
                        if event is not None:
                            # 订单管理器处理策略开平仓导致的信号事件。
                            if event.type == Event.SIGNAL:
                                algo.blotter.update_signal(event)
                            # 模拟交易所处理订单管理产生的下单事件。
                            elif event.type == Event.ORDER:
                                algo.exchange.update_order(event)
                            # 订单管理器处理模拟交易所返回的委托成交事件。
                            elif event.type == Event.FILL:
                                algo.blotter.update_fill(event)
                    # 模拟交易所的价格戳和。
                    algo.exchange.make_market(bar)
        bar_index += 1


策略结果
~~~~~~~~

* k线和交易信号线

  .. image:: _static/figure_signal.png
     :width: 500px

* 资金曲线。
  
  .. image:: _static/figure_money.png
     :width: 500px
图片的纵坐标表示价格，横坐标应该表示时间，目前只是表示Bar坐标，有待完善：P   
k线显示使用了系统自带的一个联动窗口控件，由蓝色的滑块控制显示区域，你也可以通过
上下方向键来进行缩放。 关于联动窗口，后面会介绍。 下一节介绍指标函数。
