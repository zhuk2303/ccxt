# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import math
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import RequestTimeout
from ccxt.base.precise import Precise


class coinex(Exchange):

    def describe(self):
        return self.deep_extend(super(coinex, self).describe(), {
            'id': 'coinex',
            'name': 'CoinEx',
            'version': 'v1',
            'countries': ['CN'],
            'rateLimit': 1000,
            'has': {
                'cancelOrder': True,
                'createOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchDeposits': True,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTrades': True,
                'fetchWithdrawals': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1min',
                '3m': '3min',
                '5m': '5min',
                '15m': '15min',
                '30m': '30min',
                '1h': '1hour',
                '2h': '2hour',
                '4h': '4hour',
                '6h': '6hour',
                '12h': '12hour',
                '1d': '1day',
                '3d': '3day',
                '1w': '1week',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87182089-1e05fa00-c2ec-11ea-8da9-cc73b45abbbc.jpg',
                'api': {
                    'public': 'https://api.coinex.com',
                    'private': 'https://api.coinex.com',
                    'perpetualPublic': 'https://api.coinex.com/perpetual',
                    'perpetualPrivate': 'https://api.coinex.com/perpetual',
                },
                'www': 'https://www.coinex.com',
                'doc': 'https://github.com/coinexcom/coinex_exchange_api/wiki',
                'fees': 'https://www.coinex.com/fees',
                'referral': 'https://www.coinex.com/register?refer_code=yw5fz',
            },
            'api': {
                'public': {
                    'get': [
                        'common/currency/rate',
                        'common/asset/config',
                        'market/info',
                        'market/list',
                        'market/ticker',
                        'market/ticker/all',
                        'market/depth',
                        'market/deals',
                        'market/kline',
                    ],
                },
                'private': {
                    'get': [
                        'balance/coin/deposit',
                        'balance/coin/withdraw',
                        'balance/info',
                        'future/account',
                        'future/config',
                        'future/limitprice',
                        'future/loan/history',
                        'future/market',
                        'margin/account',
                        'margin/config',
                        'margin/loan/history',
                        'margin/market',
                        'order',
                        'order/deals',
                        'order/finished',
                        'order/finished/{id}',
                        'order/pending',
                        'order/status',
                        'order/status/batch',
                        'order/user/deals',
                        'sub_account/balance',
                        'sub_account/transfer/history',
                    ],
                    'post': [
                        'balance/coin/withdraw',
                        'future/flat',
                        'future/loan',
                        'future/transfer',
                        'margin/flat',
                        'margin/loan',
                        'margin/transfer',
                        'order/batchlimit',
                        'order/ioc',
                        'order/limit',
                        'order/market',
                        'sub_account/transfer',
                    ],
                    'delete': [
                        'balance/coin/withdraw',
                        'order/pending/batch',
                        'order/pending',
                    ],
                },
                'perpetualPublic': {
                    'get': [
                        'ping',
                        'time',
                        'market/list',
                        'market/limit_config',
                        'market/ticker',
                        'market/ticker/all',
                        'market/depth',
                        'market/deals',
                        'market/funding_history',
                        'market/user_deals',
                        'market/kline',
                    ],
                },
                'perpetualPrivate': {
                    'get': [
                        'asset/query',
                        'order/pending',
                        'order/finished',
                        'order/stop_pending',
                        'order/status',
                        'position/pending',
                        'position/funding',
                    ],
                    'post': [
                        'market/adjust_leverage',
                        'market/position_expect',
                        'order/put_limit',
                        'order/put_market',
                        'order/put_stop_limit',
                        'order/cancel',
                        'order/cancel_all',
                        'order/cancel_stop',
                        'order/cancel_stop_all',
                        'order/close_limit',
                        'order/close_market',
                        'position/adjust_margin',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'maker': 0.001,
                    'taker': 0.001,
                },
                'funding': {
                    'withdraw': {
                        'BCH': 0.0,
                        'BTC': 0.001,
                        'LTC': 0.001,
                        'ETH': 0.001,
                        'ZEC': 0.0001,
                        'DASH': 0.0001,
                    },
                },
            },
            'limits': {
                'amount': {
                    'min': 0.001,
                    'max': None,
                },
            },
            'precision': {
                'amount': 8,
                'price': 8,
            },
            'options': {
                'createMarketBuyOrderRequiresPrice': True,
            },
            'commonCurrencies': {
                'ACM': 'Actinium',
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetMarketInfo(params)
        #
        #     {
        #         "code": 0,
        #         "data": {
        #             "WAVESBTC": {
        #                 "name": "WAVESBTC",
        #                 "min_amount": "1",
        #                 "maker_fee_rate": "0.001",
        #                 "taker_fee_rate": "0.001",
        #                 "pricing_name": "BTC",
        #                 "pricing_decimal": 8,
        #                 "trading_name": "WAVES",
        #                 "trading_decimal": 8
        #             }
        #         }
        #     }
        #
        markets = self.safe_value(response, 'data', {})
        result = []
        keys = list(markets.keys())
        for i in range(0, len(keys)):
            key = keys[i]
            market = markets[key]
            id = self.safe_string(market, 'name')
            tradingName = self.safe_string(market, 'trading_name')
            baseId = tradingName
            quoteId = self.safe_string(market, 'pricing_name')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            if tradingName == id:
                symbol = id
            precision = {
                'amount': self.safe_integer(market, 'trading_decimal'),
                'price': self.safe_integer(market, 'pricing_decimal'),
            }
            active = None
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'taker': self.safe_number(market, 'taker_fee_rate'),
                'maker': self.safe_number(market, 'maker_fee_rate'),
                'info': market,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': self.safe_number(market, 'min_amount'),
                        'max': None,
                    },
                    'price': {
                        'min': math.pow(10, -precision['price']),
                        'max': None,
                    },
                },
            })
        return result

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_integer(ticker, 'date')
        symbol = None
        if market is not None:
            symbol = market['symbol']
        ticker = self.safe_value(ticker, 'ticker', {})
        last = self.safe_number(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(ticker, 'high'),
            'low': self.safe_number(ticker, 'low'),
            'bid': self.safe_number(ticker, 'buy'),
            'bidVolume': None,
            'ask': self.safe_number(ticker, 'sell'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_number_2(ticker, 'vol', 'volume'),
            'quoteVolume': None,
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        response = self.publicGetMarketTicker(self.extend(request, params))
        return self.parse_ticker(response['data'], market)

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetMarketTickerAll(params)
        data = self.safe_value(response, 'data')
        timestamp = self.safe_integer(data, 'date')
        tickers = self.safe_value(data, 'ticker')
        marketIds = list(tickers.keys())
        result = {}
        for i in range(0, len(marketIds)):
            marketId = marketIds[i]
            market = self.safe_market(marketId)
            symbol = market['symbol']
            ticker = self.parse_ticker({
                'date': timestamp,
                'ticker': tickers[marketId],
            }, market)
            ticker['symbol'] = symbol
            result[symbol] = ticker
        return self.filter_by_array(result, 'symbol', symbols)

    def fetch_order_book(self, symbol, limit=20, params={}):
        self.load_markets()
        if limit is None:
            limit = 20  # default
        request = {
            'market': self.market_id(symbol),
            'merge': '0.0000000001',
            'limit': str(limit),
        }
        response = self.publicGetMarketDepth(self.extend(request, params))
        return self.parse_order_book(response['data'], symbol)

    def parse_trade(self, trade, market=None):
        # self method parses both public and private trades
        timestamp = self.safe_timestamp(trade, 'create_time')
        if timestamp is None:
            timestamp = self.safe_integer(trade, 'date_ms')
        tradeId = self.safe_string(trade, 'id')
        orderId = self.safe_string(trade, 'order_id')
        priceString = self.safe_string(trade, 'price')
        amountString = self.safe_string(trade, 'amount')
        price = self.parse_number(priceString)
        amount = self.parse_number(amountString)
        marketId = self.safe_string(trade, 'market')
        symbol = self.safe_symbol(marketId, market)
        cost = self.safe_number(trade, 'deal_money')
        if cost is None:
            cost = self.parse_number(Precise.string_mul(priceString, amountString))
        fee = None
        feeCost = self.safe_number(trade, 'fee')
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'fee_asset')
            feeCurrencyCode = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        takerOrMaker = self.safe_string(trade, 'role')
        side = self.safe_string(trade, 'type')
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'id': tradeId,
            'order': orderId,
            'type': None,
            'side': side,
            'takerOrMaker': takerOrMaker,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        response = self.publicGetMarketDeals(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    def parse_ohlcv(self, ohlcv, market=None):
        #
        #     [
        #         1591484400,
        #         "0.02505349",
        #         "0.02506988",
        #         "0.02507000",
        #         "0.02505304",
        #         "343.19716223",
        #         "8.6021323866383196",
        #         "ETHBTC"
        #     ]
        #
        return [
            self.safe_timestamp(ohlcv, 0),
            self.safe_number(ohlcv, 1),
            self.safe_number(ohlcv, 3),
            self.safe_number(ohlcv, 4),
            self.safe_number(ohlcv, 2),
            self.safe_number(ohlcv, 5),
        ]

    def fetch_ohlcv(self, symbol, timeframe='5m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
            'type': self.timeframes[timeframe],
        }
        if limit is not None:
            request['limit'] = limit
        response = self.publicGetMarketKline(self.extend(request, params))
        #
        #     {
        #         "code": 0,
        #         "data": [
        #             [1591484400, "0.02505349", "0.02506988", "0.02507000", "0.02505304", "343.19716223", "8.6021323866383196", "ETHBTC"],
        #             [1591484700, "0.02506990", "0.02508109", "0.02508109", "0.02506979", "91.59841581", "2.2972047780447000", "ETHBTC"],
        #             [1591485000, "0.02508106", "0.02507996", "0.02508106", "0.02507500", "65.15307697", "1.6340597822306000", "ETHBTC"],
        #         ],
        #         "message": "OK"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        return self.parse_ohlcvs(data, market, timeframe, since, limit)

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetBalanceInfo(params)
        #
        #     {
        #       "code": 0,
        #       "data": {
        #         "BCH": {                    # BCH account
        #           "available": "13.60109",   # Available BCH
        #           "frozen": "0.00000"        # Frozen BCH
        #         },
        #         "BTC": {                    # BTC account
        #           "available": "32590.16",   # Available BTC
        #           "frozen": "7000.00"        # Frozen BTC
        #         },
        #         "ETH": {                    # ETH account
        #           "available": "5.06000",    # Available ETH
        #           "frozen": "0.00000"        # Frozen ETH
        #         }
        #       },
        #       "message": "Ok"
        #     }
        #
        result = {'info': response}
        balances = self.safe_value(response, 'data', {})
        currencyIds = list(balances.keys())
        for i in range(0, len(currencyIds)):
            currencyId = currencyIds[i]
            code = self.safe_currency_code(currencyId)
            balance = self.safe_value(balances, currencyId, {})
            account = self.account()
            account['free'] = self.safe_string(balance, 'available')
            account['used'] = self.safe_string(balance, 'frozen')
            result[code] = account
        return self.parse_balance(result)

    def parse_order_status(self, status):
        statuses = {
            'not_deal': 'open',
            'part_deal': 'open',
            'done': 'closed',
            'cancel': 'canceled',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        # fetchOrder
        #
        #     {
        #         "amount": "0.1",
        #         "asset_fee": "0.22736197736197736197",
        #         "avg_price": "196.85000000000000000000",
        #         "create_time": 1537270135,
        #         "deal_amount": "0.1",
        #         "deal_fee": "0",
        #         "deal_money": "19.685",
        #         "fee_asset": "CET",
        #         "fee_discount": "0.5",
        #         "id": 1788259447,
        #         "left": "0",
        #         "maker_fee_rate": "0",
        #         "market": "ETHUSDT",
        #         "order_type": "limit",
        #         "price": "170.00000000",
        #         "status": "done",
        #         "taker_fee_rate": "0.0005",
        #         "type": "sell",
        #     }
        #
        timestamp = self.safe_timestamp(order, 'create_time')
        price = self.safe_number(order, 'price')
        cost = self.safe_number(order, 'deal_money')
        amount = self.safe_number(order, 'amount')
        filled = self.safe_number(order, 'deal_amount')
        average = self.safe_number(order, 'avg_price')
        symbol = None
        marketId = self.safe_string(order, 'market')
        market = self.safe_market(marketId, market)
        feeCurrencyId = self.safe_string(order, 'fee_asset')
        feeCurrency = self.safe_currency_code(feeCurrencyId)
        if market is not None:
            symbol = market['symbol']
            if feeCurrency is None:
                feeCurrency = market['quote']
        remaining = self.safe_number(order, 'left')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        type = self.safe_string(order, 'order_type')
        side = self.safe_string(order, 'type')
        return self.safe_order({
            'id': self.safe_string(order, 'id'),
            'clientOrderId': None,
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'cost': cost,
            'average': average,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'trades': None,
            'fee': {
                'currency': feeCurrency,
                'cost': self.safe_number(order, 'deal_fee'),
            },
            'info': order,
        })

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        method = 'privatePostOrder' + self.capitalize(type)
        market = self.market(symbol)
        request = {
            'market': market['id'],
            'type': side,
        }
        # for market buy it requires the amount of quote currency to spend
        if (type == 'market') and (side == 'buy'):
            if self.options['createMarketBuyOrderRequiresPrice']:
                if price is None:
                    raise InvalidOrder(self.id + " createOrder() requires the price argument with market buy orders to calculate total order cost(amount to spend), where cost = amount * price. Supply a price argument to createOrder() call if you want the cost to be calculated for you from price and amount, or, alternatively, add .options['createMarketBuyOrderRequiresPrice'] = False to supply the cost in the amount argument(the exchange-specific behaviour)")
                else:
                    request['amount'] = self.cost_to_precision(symbol, amount * price)
            else:
                request['amount'] = self.cost_to_precision(symbol, amount)
        else:
            request['amount'] = self.amount_to_precision(symbol, amount)
        if (type == 'limit') or (type == 'ioc'):
            request['price'] = self.price_to_precision(symbol, price)
        response = getattr(self, method)(self.extend(request, params))
        data = self.safe_value(response, 'data')
        return self.parse_order(data, market)

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'id': id,
            'market': market['id'],
        }
        response = self.privateDeleteOrderPending(self.extend(request, params))
        data = self.safe_value(response, 'data')
        return self.parse_order(data, market)

    def fetch_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrder() requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'id': id,
            'market': market['id'],
        }
        response = self.privateGetOrder(self.extend(request, params))
        #
        #     {
        #         "code": 0,
        #         "data": {
        #             "amount": "0.1",
        #             "asset_fee": "0.22736197736197736197",
        #             "avg_price": "196.85000000000000000000",
        #             "create_time": 1537270135,
        #             "deal_amount": "0.1",
        #             "deal_fee": "0",
        #             "deal_money": "19.685",
        #             "fee_asset": "CET",
        #             "fee_discount": "0.5",
        #             "id": 1788259447,
        #             "left": "0",
        #             "maker_fee_rate": "0",
        #             "market": "ETHUSDT",
        #             "order_type": "limit",
        #             "price": "170.00000000",
        #             "status": "done",
        #             "taker_fee_rate": "0.0005",
        #             "type": "sell",
        #         },
        #         "message": "Ok"
        #     }
        #
        data = self.safe_value(response, 'data')
        return self.parse_order(data, market)

    def fetch_orders_by_status(self, status, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        if limit is None:
            limit = 100
        request = {
            'page': 1,
            'limit': limit,
        }
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['market'] = market['id']
        method = 'privateGetOrder' + self.capitalize(status)
        response = getattr(self, method)(self.extend(request, params))
        data = self.safe_value(response, 'data')
        orders = self.safe_value(data, 'data', [])
        return self.parse_orders(orders, market, since, limit)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_status('pending', symbol, since, limit, params)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_status('finished', symbol, since, limit, params)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        if limit is None:
            limit = 100
        request = {
            'page': 1,
            'limit': limit,
        }
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['market'] = market['id']
        response = self.privateGetOrderUserDeals(self.extend(request, params))
        data = self.safe_value(response, 'data')
        trades = self.safe_value(data, 'data', [])
        return self.parse_trades(trades, market, since, limit)

    def withdraw(self, code, amount, address, tag=None, params={}):
        self.check_address(address)
        self.load_markets()
        currency = self.currency(code)
        if tag:
            address = address + ':' + tag
        request = {
            'coin_type': currency['id'],
            'coin_address': address,  # must be authorized, inter-user transfer by a registered mobile phone number or an email address is supported
            'actual_amount': float(amount),  # the actual amount without fees, https://www.coinex.com/fees
            'transfer_method': 'onchain',  # onchain, local
        }
        response = self.privatePostBalanceCoinWithdraw(self.extend(request, params))
        #
        #     {
        #         "code": 0,
        #         "data": {
        #             "actual_amount": "1.00000000",
        #             "amount": "1.00000000",
        #             "coin_address": "1KAv3pazbTk2JnQ5xTo6fpKK7p1it2RzD4",
        #             "coin_type": "BCH",
        #             "coin_withdraw_id": 206,
        #             "confirmations": 0,
        #             "create_time": 1524228297,
        #             "status": "audit",
        #             "tx_fee": "0",
        #             "tx_id": ""
        #         },
        #         "message": "Ok"
        #     }
        #
        transaction = self.safe_value(response, 'data', {})
        return self.parse_transaction(transaction, currency)

    def parse_transaction_status(self, status):
        statuses = {
            'audit': 'pending',
            'pass': 'pending',
            'processing': 'pending',
            'confirming': 'pending',
            'not_pass': 'failed',
            'cancel': 'canceled',
            'finish': 'ok',
            'fail': 'failed',
        }
        return self.safe_string(statuses, status, status)

    def parse_transaction(self, transaction, currency=None):
        #
        # fetchDeposits
        #
        #     {
        #         "actual_amount": "120.00000000",
        #         "actual_amount_display": "120",
        #         "add_explorer": "XXX",
        #         "amount": "120.00000000",
        #         "amount_display": "120",
        #         "coin_address": "XXXXXXXX",
        #         "coin_address_display": "XXXXXXXX",
        #         "coin_deposit_id": 1866,
        #         "coin_type": "USDT",
        #         "confirmations": 0,
        #         "create_time": 1539595701,
        #         "explorer": "",
        #         "remark": "",
        #         "status": "finish",
        #         "status_display": "finish",
        #         "transfer_method": "local",
        #         "tx_id": "",
        #         "tx_id_display": "XXXXXXXXXX"
        #     }
        #
        # fetchWithdrawals
        #
        #     {
        #         "actual_amount": "0.10000000",
        #         "amount": "0.10000000",
        #         "coin_address": "15sr1VdyXQ6sVLqeJUJ1uPzLpmQtgUeBSB",
        #         "coin_type": "BCH",
        #         "coin_withdraw_id": 203,
        #         "confirmations": 11,
        #         "create_time": 1515806440,
        #         "status": "finish",
        #         "tx_fee": "0",
        #         "tx_id": "896371d0e23d64d1cac65a0b7c9e9093d835affb572fec89dd4547277fbdd2f6"
        #     }
        #
        id = self.safe_string_2(transaction, 'coin_withdraw_id', 'coin_deposit_id')
        address = self.safe_string(transaction, 'coin_address')
        tag = self.safe_string(transaction, 'remark')  # set but unused
        if tag is not None:
            if len(tag) < 1:
                tag = None
        txid = self.safe_value(transaction, 'tx_id')
        if txid is not None:
            if len(txid) < 1:
                txid = None
        currencyId = self.safe_string(transaction, 'coin_type')
        code = self.safe_currency_code(currencyId, currency)
        timestamp = self.safe_timestamp(transaction, 'create_time')
        type = 'withdraw' if ('coin_withdraw_id' in transaction) else 'deposit'
        status = self.parse_transaction_status(self.safe_string(transaction, 'status'))
        amount = self.safe_number(transaction, 'amount')
        feeCost = self.safe_number(transaction, 'tx_fee')
        if type == 'deposit':
            feeCost = 0
        fee = {
            'cost': feeCost,
            'currency': code,
        }
        # https://github.com/ccxt/ccxt/issues/8321
        if amount is not None:
            amount = amount - feeCost
        return {
            'info': transaction,
            'id': id,
            'txid': txid,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'address': address,
            'tag': tag,
            'type': type,
            'amount': amount,
            'currency': code,
            'status': status,
            'updated': None,
            'fee': fee,
        }

    def fetch_withdrawals(self, code=None, since=None, limit=None, params={}):
        if code is None:
            raise ArgumentsRequired(self.id + ' fetchWithdrawals() requires a currency code argument')
        self.load_markets()
        currency = self.currency(code)
        request = {
            'coin_type': currency['id'],
        }
        if limit is not None:
            request['Limit'] = limit
        response = self.privateGetBalanceCoinWithdraw(self.extend(request, params))
        #
        #     {
        #         "code": 0,
        #         "data": {
        #             "has_next": True,
        #             "curr_page": 1,
        #             "count": 10,
        #             "data": [
        #                 {
        #                     "coin_withdraw_id": 203,
        #                     "create_time": 1513933541,
        #                     "actual_amount": "0.00100000",
        #                     "actual_amount_display": "***",
        #                     "amount": "0.00100000",
        #                     "amount_display": "******",
        #                     "coin_address": "1GVVx5UBddLKrckTprNi4VhHSymeQ8tsLF",
        #                     "app_coin_address_display": "**********",
        #                     "coin_address_display": "****************",
        #                     "add_explorer": "https://explorer.viawallet.com/btc/address/1GVVx5UBddLKrckTprNi4VhHSymeQ8tsLF",
        #                     "coin_type": "BTC",
        #                     "confirmations": 6,
        #                     "explorer": "https://explorer.viawallet.com/btc/tx/1GVVx5UBddLKrckTprNi4VhHSymeQ8tsLF",
        #                     "fee": "0",
        #                     "remark": "",
        #                     "smart_contract_name": "BTC",
        #                     "status": "finish",
        #                     "status_display": "finish",
        #                     "transfer_method": "onchain",
        #                     "tx_fee": "0",
        #                     "tx_id": "896371d0e23d64d1cac65a0b7c9e9093d835affb572fec89dd4547277fbdd2f6"
        #                 }, /* many more data points */
        #             ],
        #             "total": ***,
        #             "total_page":***
        #         },
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data')
        if not isinstance(data, list):
            data = self.safe_value(data, 'data', [])
        return self.parse_transactions(data, currency, since, limit)

    def fetch_deposits(self, code=None, since=None, limit=None, params={}):
        if code is None:
            raise ArgumentsRequired(self.id + ' fetchDeposits() requires a currency code argument')
        self.load_markets()
        currency = self.currency(code)
        request = {
            'coin_type': currency['id'],
        }
        if limit is not None:
            request['Limit'] = limit
        response = self.privateGetBalanceCoinDeposit(self.extend(request, params))
        #     {
        #         "code": 0,
        #         "data": [
        #             {
        #                 "actual_amount": "4.65397682",
        #                 "actual_amount_display": "4.65397682",
        #                 "add_explorer": "https://etherscan.io/address/0x361XXXXXX",
        #                 "amount": "4.65397682",
        #                 "amount_display": "4.65397682",
        #                 "coin_address": "0x36dabcdXXXXXX",
        #                 "coin_address_display": "0x361X*****XXXXX",
        #                 "coin_deposit_id": 966191,
        #                 "coin_type": "ETH",
        #                 "confirmations": 30,
        #                 "create_time": 1531661445,
        #                 "explorer": "https://etherscan.io/tx/0x361XXXXXX",
        #                 "remark": "",
        #                 "status": "finish",
        #                 "status_display": "finish",
        #                 "transfer_method": "onchain",
        #                 "tx_id": "0x361XXXXXX",
        #                 "tx_id_display": "0x361XXXXXX"
        #             }
        #         ],
        #         "message": "Ok"
        #     }
        #
        data = self.safe_value(response, 'data')
        if not isinstance(data, list):
            data = self.safe_value(data, 'data', [])
        return self.parse_transactions(data, currency, since, limit)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        path = self.implode_params(path, params)
        url = self.urls['api'][api] + '/' + self.version + '/' + path
        query = self.omit(params, self.extract_params(path))
        if api == 'public' or api == 'perpetualPublic':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            nonce = self.nonce()
            query = self.extend({
                'access_id': self.apiKey,
                'tonce': str(nonce),
            }, query)
            query = self.keysort(query)
            urlencoded = self.rawencode(query)
            signature = self.hash(self.encode(urlencoded + '&secret_key=' + self.secret))
            headers = {
                'Authorization': signature.upper(),
                'Content-Type': 'application/json',
            }
            if (method == 'GET') or (method == 'DELETE'):
                url += '?' + urlencoded
            else:
                body = self.json(query)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return
        code = self.safe_string(response, 'code')
        data = self.safe_value(response, 'data')
        message = self.safe_string(response, 'message')
        if (code != '0') or (data is None) or ((message != 'Success') and (message != 'Succeeded') and (message != 'Ok') and not data):
            responseCodes = {
                # https://github.com/coinexcom/coinex_exchange_api/wiki/013error_code
                '23': PermissionDenied,  # IP Prohibited
                '24': AuthenticationError,
                '25': AuthenticationError,
                '34': AuthenticationError,  # Access id is expires
                '35': ExchangeNotAvailable,  # Service unavailable
                '36': RequestTimeout,  # Service timeout
                '107': InsufficientFunds,
                '600': OrderNotFound,
                '601': InvalidOrder,
                '602': InvalidOrder,
                '606': InvalidOrder,
            }
            ErrorClass = self.safe_value(responseCodes, code, ExchangeError)
            raise ErrorClass(response['message'])
