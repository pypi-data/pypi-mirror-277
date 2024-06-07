from generated.IndicatorRequest import IndicatorRequest
from generated.FBBacktest import FBBacktest
from generated.InputSeries import InputSeries
from generated.FBArray import FBArray


def deserialize_arr(buffer):
    byte_data = bytes(buffer)

    fbb_arr = FBArray.GetRootAsFBArray(byte_data, 0)

    return [fbb_arr.V(j) for j in range(fbb_arr.VLength())]


def deserialize_indicator_request(buffer):
    byte_data = bytes(buffer)

    fbb_indicator = IndicatorRequest.GetRootAsIndicatorRequest(byte_data, 0)

    values = {}

    data_kvp_length = fbb_indicator.DataLength()

    for i in range(data_kvp_length):
        kvp = fbb_indicator.Data(i)

        key = kvp.Key().decode()
        values[key] = [kvp.Value(j) for j in range(kvp.ValueLength())]

    return {
        "name": fbb_indicator.Name().decode(),
        "values": values,
        "parameters": {
            fbb_indicator.Parameters(j)
            .Key()
            .decode(): fbb_indicator.Parameters(j)
            .Value()
            .decode()
            for j in range(fbb_indicator.ParametersLength())
        },
    }


def deserialize_backtest(buffer):
    backtest = {}
    byte_data = bytes(buffer)

    fbb_backtest = FBBacktest.GetRootAsBacktest(byte_data, 0)

    indicators_length = fbb_backtest.IndicatorsLength()

    indicators = {}
    for i in range(indicators_length):
        kvp = fbb_backtest.Indicators(i)

        key = kvp.Key().decode()
        values = [kvp.Values(j) for j in range(kvp.ValuesLength())]

        indicators[key] = values
    backtest["indicators"] = indicators

    portfolio_length = fbb_backtest.PortfolioLength()
    portfolio = {}
    for i in range(portfolio_length):
        kvp = fbb_backtest.Portfolio(i)

        key = kvp.Key().decode()
        values = [kvp.Values(j) for j in range(kvp.ValuesLength())]

        portfolio[key] = values
    backtest["portfolio"] = portfolio

    action_length = fbb_backtest.ActionsLength()
    actions = {}
    for i in range(action_length):
        kvp = fbb_backtest.Actions(i)

        key = kvp.Key().decode()
        values = [kvp.Values(j) for j in range(kvp.ValuesLength())]

        actions[key] = values
    backtest["actions"] = actions

    backtest["cash"] = [fbb_backtest.Cash(j) for j in range(fbb_backtest.CashLength())]
    backtest["nv"] = [fbb_backtest.Nv(j) for j in range(fbb_backtest.NvLength())]
    backtest["pv"] = [fbb_backtest.Pv(j) for j in range(fbb_backtest.PvLength())]

    return backtest


def deserialize_input_series(buffer):
    input_series = {}
    series_data = {}

    byte_data = bytes(buffer)

    fbb_input_series = InputSeries.GetRootAsInputSeries(byte_data, 0)

    data_length = fbb_input_series.DataLength()

    for i in range(data_length):
        kvp = fbb_input_series.Data(i)

        key = kvp.Key().decode()
        values = [kvp.Values(j) for j in range(kvp.ValuesLength())]

        series_data[key] = values

    input_series["dates"] = [
        fbb_input_series.Dates(j).decode()
        for j in range(fbb_input_series.DatesLength())
    ]
    input_series["data"] = series_data

    return input_series
