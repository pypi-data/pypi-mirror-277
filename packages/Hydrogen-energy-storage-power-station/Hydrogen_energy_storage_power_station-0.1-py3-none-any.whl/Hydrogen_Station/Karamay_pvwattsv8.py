import json
import PySAM.Pvwattsv8 as pv  # import the PVWatts module from PySAM
import TimeCalculation
import pandas as pd


def gen_calc():
    # create a new instance of the Pvwattsv8 module
    pv_model = pv.new()

    # get the inputs from the JSON file
    with open('Karamay_pvwattsv8_v2.json', 'r') as f:
        pv_inputs = json.load(f)

    # iterate through the input key-value pairs and set the module inputs
    for k, v in pv_inputs.items():
        try:
            # print(k)
            if k != 'number_inputs':
                pv_model.value(k, v)
        except Exception as e:
            # print("error is :" + str(e))
            pass

    # run the module
    pv_model.execute()
    system_gen = pv_model.Outputs.gen
    system_gen = pd.DataFrame(system_gen)

    system_gen_year = pv_model.Outputs.annual_energy
    # print(system_gen_year)
    return system_gen


def output_power_year(year):
    power = gen_calc()
    date_year = TimeCalculation.generate_timestamps_for_year(year)

    # drop leap year
    date_year_length = date_year.size
    if date_year_length == 8784:
        for i in range(1416, 1440):
            date_year = date_year.drop(i)
        # reset index
        date_year = date_year.reset_index(drop=True)

    merged_date = pd.concat([date_year, power], axis=1)
    merged_date.columns = ['Datetime', 'Output Power']
    return merged_date


def output_power():
    # time select
    raw_data_density = input("请输入时间密度如“day”,“hour”,“30min”,“15min”,“min”,“sec”:")
    raw_data = input("请输入年月日格式如2023-11-12：")
    raw_hour = input("请输入24小时时间格式如13：23：19: ")
    year, month, day = raw_data.split("-")
    hour, min, sec = raw_hour.split(":")

    data_density = TimeCalculation.data_density(raw_data_density)

    if data_density == 1:
        time = TimeCalculation.calc_day(year, month, day)
    elif data_density == 2:
        time = TimeCalculation.calc_hour(year, month, day, hour)
    elif data_density == 3:
        time = TimeCalculation.calc_30min(year, month, day, hour, min)
    else:
        print("data density error")
        exit()
    power_all = output_power_year(year)
    power = power_all.iloc[time - 1]
    print(power)


# if __name__ == '__main__':
#     # Output_Power()
#     power = Output_Power_Year(2024)
#     power.to_csv("D:/MJC/源网荷储/01-系统仿真/01-Python/test.csv", index=True, header=True)

