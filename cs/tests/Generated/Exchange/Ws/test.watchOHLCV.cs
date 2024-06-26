using ccxt;
using ccxt.pro;
namespace Tests;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


public partial class testMainClass : BaseTest
{
    async static public Task testWatchOHLCV(Exchange exchange, object skippedProperties, object symbol)
    {
        object method = "watchOHLCV";
        object now = exchange.milliseconds();
        object ends = add(now, 15000);
        object timeframeKeys = new List<object>(((IDictionary<string,object>)exchange.timeframes).Keys);
        assert(getArrayLength(timeframeKeys), add(add(add(exchange.id, " "), method), " - no timeframes found"));
        // prefer 1m timeframe if available, otherwise return the first one
        object chosenTimeframeKey = "1m";
        if (!isTrue(exchange.inArray(chosenTimeframeKey, timeframeKeys)))
        {
            chosenTimeframeKey = getValue(timeframeKeys, 0);
        }
        object limit = 10;
        object duration = exchange.parseTimeframe(chosenTimeframeKey);
        object since = subtract(subtract(exchange.milliseconds(), multiply(multiply(duration, limit), 1000)), 1000);
        while (isLessThan(now, ends))
        {
            object response = null;
            try
            {
                response = await exchange.watchOHLCV(symbol, chosenTimeframeKey, since, limit);
            } catch(Exception e)
            {
                if (!isTrue(testSharedMethods.isTemporaryFailure(e)))
                {
                    throw e;
                }
                now = exchange.milliseconds();
                continue;
            }
            testSharedMethods.assertNonEmtpyArray(exchange, skippedProperties, method, response, symbol);
            now = exchange.milliseconds();
            for (object i = 0; isLessThan(i, getArrayLength(response)); postFixIncrement(ref i))
            {
                testOHLCV(exchange, skippedProperties, method, getValue(response, i), symbol, now);
            }
        }
    }

}