import Exchange from './abstract/btcex.js';
import { Int } from './base/types.js';
export default class btcex extends Exchange {
    describe(): any;
    fetchMarkets(params?: {}): Promise<any[]>;
    parseTicker(ticker: any, market?: any): import("./base/types.js").Ticker;
    fetchTicker(symbol: string, params?: {}): Promise<import("./base/types.js").Ticker>;
    fetchOrderBook(symbol: string, limit?: Int, params?: {}): Promise<import("./base/types.js").OrderBook>;
    parseOHLCV(ohlcv: any, market?: any): number[];
    fetchOHLCV(symbol: string, timeframe?: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").OHLCV[]>;
    parseTrade(trade: any, market?: any): import("./base/types.js").Trade;
    fetchTrades(symbol: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").Trade[]>;
    signIn(params?: {}): Promise<string>;
    parseBalance(response: any): import("./base/types.js").Balances;
    fetchBalance(params?: {}): Promise<import("./base/types.js").Balances>;
    parseOrderStatus(status: any): string;
    parseTimeInForce(timeInForce: any): string;
    parseOrder(order: any, market?: any): any;
    fetchOrder(id: any, symbol?: string, params?: {}): Promise<any>;
    createOrder(symbol: string, type: any, side: any, amount: any, price?: any, params?: {}): Promise<any>;
    cancelOrder(id: any, symbol?: string, params?: {}): Promise<any>;
    cancelAllOrders(symbol?: string, params?: {}): Promise<any>;
    fetchOpenOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").Order[]>;
    fetchClosedOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").Order[]>;
    fetchOrderTrades(id: any, symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").Trade[]>;
    fetchMyTrades(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<import("./base/types.js").Trade[]>;
    parsePosition(position: any, market?: any): any;
    fetchPosition(symbol: string, params?: {}): Promise<any>;
    fetchPositions(symbols?: string[], params?: {}): Promise<any>;
    parseTransactionStatus(status: any): string;
    parseTransaction(transaction: any, currency?: any): {
        info: any;
        id: string;
        txid: string;
        timestamp: number;
        datetime: string;
        network: any;
        addressFrom: any;
        address: any;
        addressTo: any;
        tagFrom: any;
        tag: any;
        tagTo: any;
        type: any;
        amount: number;
        currency: any;
        status: string;
        updated: number;
        fee: any;
    };
    fetchDeposits(code?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    fetchWithdrawals(code?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    fetchWithdrawal(id: any, code?: string, params?: {}): Promise<{
        info: any;
        id: string;
        txid: string;
        timestamp: number;
        datetime: string;
        network: any;
        addressFrom: any;
        address: any;
        addressTo: any;
        tagFrom: any;
        tag: any;
        tagTo: any;
        type: any;
        amount: number;
        currency: any;
        status: string;
        updated: number;
        fee: any;
    }>;
    fetchLeverage(symbol: string, params?: {}): Promise<number>;
    fetchMarketLeverageTiers(symbol: string, params?: {}): Promise<any[]>;
    parseMarketLeverageTiers(info: any, market?: any): any[];
    fetchLeverageTiers(symbols?: string[], params?: {}): Promise<{}>;
    parseLeverageTiers(response: any, symbols?: string[], marketIdKey?: any): {};
    setMarginMode(marginMode: any, symbol?: string, params?: {}): Promise<any>;
    setLeverage(leverage: any, symbol?: string, params?: {}): Promise<any>;
    fetchFundingRates(symbols?: string[], params?: {}): Promise<any>;
    fetchFundingRate(symbol: string, params?: {}): Promise<{
        info: any;
        symbol: any;
        markPrice: any;
        indexPrice: number;
        interestRate: any;
        estimatedSettlePrice: any;
        timestamp: any;
        datetime: any;
        fundingRate: number;
        fundingTimestamp: number;
        fundingDatetime: string;
        nextFundingRate: any;
        nextFundingTimestamp: any;
        nextFundingDatetime: any;
        previousFundingRate: any;
        previousFundingTimestamp: any;
        previousFundingDatetime: any;
    }>;
    parseFundingRate(contract: any, market?: any): {
        info: any;
        symbol: any;
        markPrice: any;
        indexPrice: number;
        interestRate: any;
        estimatedSettlePrice: any;
        timestamp: any;
        datetime: any;
        fundingRate: number;
        fundingTimestamp: number;
        fundingDatetime: string;
        nextFundingRate: any;
        nextFundingTimestamp: any;
        nextFundingDatetime: any;
        previousFundingRate: any;
        previousFundingTimestamp: any;
        previousFundingDatetime: any;
    };
    transfer(code: string, amount: any, fromAccount: any, toAccount: any, params?: {}): Promise<{
        info: any;
        id: string;
        timestamp: any;
        datetime: any;
        currency: any;
        amount: any;
        fromAccount: any;
        toAccount: any;
        status: any;
    }>;
    parseTransfer(transfer: any, currency?: any): {
        info: any;
        id: string;
        timestamp: any;
        datetime: any;
        currency: any;
        amount: any;
        fromAccount: any;
        toAccount: any;
        status: any;
    };
    fetchOpenInterest(symbol: string, params?: {}): Promise<{
        info: any;
        symbol: any;
        baseVolume: number;
        quoteVolume: any;
        openInterestAmount: number;
        openInterestValue: any;
        timestamp: any;
        datetime: any;
    }>;
    parseOpenInterest(interest: any, market?: any): {
        info: any;
        symbol: any;
        baseVolume: number;
        quoteVolume: any;
        openInterestAmount: number;
        openInterestValue: any;
        timestamp: any;
        datetime: any;
    };
    sign(path: any, api?: string, method?: string, params?: {}, headers?: any, body?: any): {
        url: string;
        method: string;
        body: any;
        headers: any;
    };
    handleErrors(code: any, reason: any, url: any, method: any, headers: any, body: any, response: any, requestHeaders: any, requestBody: any): void;
}
