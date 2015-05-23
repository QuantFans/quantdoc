# -*- coding: utf8 -*-

class QAPI(object):
    """ 交易接口类 """
    def __init__(self):
        pass
    
    def qlogon(broker_id, user_id, password, api_type='ctp'):
        """ 登录交易帐号。

           :param str broker_id: 经纪商
           :param str user_id: 用户ID
           :param str password: 密码
           :param str api_type: 交易接口类型
           :return: 用户标识, 用户后续交易。如果失败则返回负数，为错误编码。成功返回'登录id'。
           :rtype: int
        """ 
        pass

    def qlogout(logon_id):
        """ 退出帐号。
        
           :param int logon_id: 登录id
           :return: 如果失败则返回负数，为错误编码。成功返回0。
           :rtype: int
        """ 
        pass

    def qorder(contract, trade_side, price, quantity, order_type='LMT', hedge_type='SPEC', logon_id=None, syn=True):
        """ 委托下单。  
        
           :param str contract: 合约编号，如：'600000.SH'。 
           :param str trade_side: 交易动作，可取：1/'BUY'，2/'SHORT'，3/'COVER'，4/'SELL'， 5/'COVERTODAY'， 6/'SELLTODAY'。
           :param str price: 价格， 只对价单有用。
           :param str quantity:  数目。
           :param str order_type:  订单成交类型， 可取：0/'LMT' - 限价单， 1/'MKT' - 市价单。
           :param str hedge_type:  交易类型， 可取：0/'SPEC' - 投机(默认值)，1/'HEDG' - 套保。
           :param int logon_id: 只有一个交易登录时，可以不输入logon_id， 否则一定需要输入。
           :param bool syn: 是否同步调用。如果取True，则会在订单成交后返回。否则函数会立即返回，并在成交后调用回调函数。
           :return: 返回字典，字段：'error_code' 错误编码，0表示成功； 如果是同步调用，还返回：'price' 成交价格，'datetime' 成交时间..
           :rtype: dict
        """
        pass

    def qcancel_order(order_id, logon_id=None, syn=True):
        """ 取消委托。
        
           :param int order_id: 订单编号。
           :param int logon_id: 只有一个交易登录时，可以不输入logon_id， 否则一定需要输入。
           :param bool syn: 是否同步调用。如果取True，则会在成功后返回。否则函数会立即返回，并在成功后调用回调函数。
           :return: 返回字典，字段：'error_code' 错误编码，0表示成功；
           :rtype: dict
        """
        pass

    def qquery(qrycode, logon_id=None, request_id=None, order_id=None, contract=None, syn=True):
        """ 查询资金，持仓，委托情况等。
        
           :param str qrycode: qrycode 可取:0/'CAPITAL' 资金查询；1/'POSITION' 持仓查询； 2/'ORDER' 今日委托查询；3/'TRADE'  今日成交查询。
           :param int logon_id: 只有一个交易登录时，可以不输入logon_id， 否则一定需要输入。
           :param int request_id: 委托编号，委托查询的时候使用。
           :param int order_id: 订单编号，查询特定订单的成交信息。
           :param str contract: 合约编号，持仓查询的时候使用。
           :param bool syn: 是否同步调用。如果取True，则会在成功后返回。
                            否则函数会立即返回，并在成功后调用回调函数。
           :return: 返回字典，字段：'error_code' 错误编码，0表示成功； 如果是同步调用且

                    是资金查询：还返回：'cash' 当前权益

                    是持仓查询：还返回：'price' 成交价格，'datetime' 成交时间..
           :rtype: dict
        """
        pass

    def qreqdata(contract, syn=True):
        """ 数据订阅, 成功后每隔一定的时间callback函数会被调用。
        
           :param str contract: 合约编号。
           :param bool syn: 是否同步调用。如果取True，则会在接收到数据后返回。
           :return: 如果失败则返回负数，为错误编码。成功返回0。
           :rtype: int
        """
        pass

    def qcancel_data(contract):
        """ 取消价格数据订阅。
        
           :param str contract: 合约编号。
           :return: 如果失败则返回负数，为错误编码。成功返回0。
           :rtype: int
        """
        pass

    def qreqdata_now(contract):
        """ 获取当前价格数据,一次性同步订阅。
        
           :param str contract: 合约编号。
           :return: 当前数据
           :rtype: object
        """
        pass

    def on_tickprice(self, tick):
        """ tick数据回调函数
        
           :param TickData tick: tick数据信息。字段包括：

                                 price: 当前价格。

                                 buy1: 买一

                                 sell1: 卖一
        """
        pass

    def on_orderstatus(self, order):
        """ 委托成交回调函数。
        
           :param Order order: 订单成交信息。字段包括：

                                 price: 当前价格。

                                 buy1: 买一

                                 sell1: 卖一
        """
        pass


