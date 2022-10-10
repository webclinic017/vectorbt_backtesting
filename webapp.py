from email.policy import default
import streamlit as st
import pandas_ta as ta
import pandas as pd
import inspect
from pandas_ta_utils import list_ind
from strategy import calc_ind
from candle_fetcher import get_candles


def main():
    st.header("Data Downloader")

    col1, col2 = st.columns([2, 5])
    # container: will be used by callback function calc_ind to populate the page
    cont = st.container()
    cont.write("")
    with col1:
        # ticker
        ticker = st.text_input("Ticker", "BTC-USD")
        amount_of_candles = st.number_input("Amount of candles", 100, 100000, 1000)
        timeframe = st.selectbox("Timeframe", ["1m", "5m", "15m", "1h", "4h", "1d", "1w"], index=3)
        # List of all indicators
        indicators = list_ind()
        select_ind = st.multiselect("Choose indicators to apply to data", indicators)

        args_dicts = {} #multi indicator
        ind_functions = [getattr(ta, ind) for ind in select_ind]

        for ind_function in ind_functions:
            # get the arguments of the indicator function
            args = inspect.getfullargspec(ind_function).args
            # remove the first argument (dataframe)
            args.pop(0)
            # create a dict with the arguments as keys and empty values
            args_dict = {arg: "" for arg in args}
            # create a dict with the arguments as keys and the values from the user
            args_dict = st.sidebar.form(key=ind_function.__name__).form_data
            # add the indicator function name as a key and the args_dict as value to the args_dicts dict
            args_dicts[ind_function.__name__] = args_dict

        # st.sidebar.write(ind_function.__doc__)

        # #list indicator parameter boxes
        # for ind_function in ind_functions:
        #     args = inspect.getfullargspec(ind_function).args #get all params needed
        #     args_dict = {}
        #     for argument in args:
        #         param_box = f"{argument}input" #name the input box
                
        #         # toggle type of input according to variable. Data will be automatically added, no need to enter infos
        #         input_box_unique_id = ind_function.__name__+'_'+argument
        #         data_set = {"open_", "high", "low", "close", "volume"}
        #         text_set = {"mamode"}
        #         if argument in text_set:
        #             param_box = st.text_input(argument, key=input_box_unique_id)
        #         elif argument == "talib":
        #             param_box = False
        #         elif argument == 'offset':
        #             param_box = 0
        #         elif argument not in data_set:
        #             param_box = st.number_input(argument, step=1, key=input_box_unique_id)
        #         args_dict[argument] = param_box
        #     args_dicts[ind_function.__name__] = args_dict #multi indicator
        
        filename = ticker + "_" + str(amount_of_candles) + "_candles"

        def get_final_dataframe():
            candles_dataframe = get_candles(ticker, timeframe, amount_of_candles)
            calc_ind(filename, candles_dataframe, col2, args_dicts)
        st.button("Go Go Go", on_click=get_final_dataframe)
        


