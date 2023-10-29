import pandas as pd

######################################
# Step 1: Monsoon data preprocessing #
######################################

### Sometimes the power provided is not stable so the experiment coule be interrupted
### So we separate the experiment into n sections
### The i loop is used to process the results from all the n sections.
### If you have 3 sections in total, set the range to (1, 4)
### If you have only 1 experiment section to get all things done
### (which means you only run the experiment runner for one time then you get all the results)
### Then please just keep the range as (1, 2)

for i in range(1, 2):
    read_file_name = f"HV Output{i}.csv"
    write_file_name = f"monsoon_data{i}(adding power and energy).csv"
    # Collect from monsoon monitor, replace the monsoon original data path here
    monsoon_original_data = pd.read_csv(read_file_name)
    monsoon_original_data = monsoon_original_data.rename(
        columns={monsoon_original_data.columns[0]: "Time(s)"}
    )

    # Calculate power (transform the measurement of current from mA to A)
    monsoon_original_data["Power(W)"] = (
        monsoon_original_data["Main(mA)"]
        * monsoon_original_data["Main Voltage(V)"]
        / 1000
    )

    # Calculate average power of each timestamp
    monsoon_original_data["Average Power(W)"] = monsoon_original_data.groupby(
        "Time(s)"
    )["Power(W)"].transform("mean")

    # Time interval(from ms measured to second measured)
    monsoon_original_data["Time Interval(s)"] = (
        monsoon_original_data["Time(s)"] - monsoon_original_data["Time(s)"].shift()
    )

    # Drop unused data
    columns_to_drop = ["USB(mA)", "Aux(mA)", "USB Voltage(V)", "Unnamed: 6", "Power(W)"]
    monsoon_original_data = monsoon_original_data.drop(columns=columns_to_drop)
    monsoon_original_data = monsoon_original_data[
        monsoon_original_data["Time Interval(s)"] != 0
    ]

    # Calculate each interval's Energy Consumption
    monsoon_original_data["Energy(J)"] = (
        monsoon_original_data["Average Power(W)"]
        * monsoon_original_data["Time Interval(s)"]
    )

    monsoon_original_data.to_csv(write_file_name, index=False)


##################################################
# Step 2: Merge monsoon data and experiment data #
##################################################
for i in range(1, 2):
    # The monsoon data after step 1 preprocessing
    monsoon_file_name = f"monsoon_data{i}(adding power and energy).csv"

    # Be aware of the path! you may need to manually change the names of folders or files for corect index
    experiment_file_pathname = f"experiments{i}/new_runner_experiment/run_table{i}.csv"

    # Set the output
    output_file_name = f"merged_result{i}.csv"

    # Monsoon data after initial processing
    monsoon_data = pd.read_csv(monsoon_file_name)

    # Collect from experiment runner
    experiment_data = pd.read_csv(experiment_file_pathname)

    for index1, row1 in experiment_data.iterrows():
        # Find the start/end timestamp of one program experiment
        start_time = row1["start_time"]
        end_time = row1["end_time"]
        start_time = float(row1["start_time"])
        end_time = float(row1["end_time"])

        # The index of the matching start/end timestamp in monsoon data
        idx_start = 0
        idx_end = 0
        # Used for matching timestamp
        last_current_time = 0
        # Iterate over the monsoon data, find the matching timestamp
        for index2, row2 in monsoon_data.iterrows():
            current_time = row2["Time(s)"]

            if start_time >= last_current_time and start_time <= current_time:
                idx_start = (
                    index2
                    if (start_time - last_current_time > current_time - start_time)
                    else index2 - 1
                )

            if end_time >= last_current_time and end_time <= current_time:
                idx_end = (
                    index2
                    if (end_time - last_current_time > current_time - end_time)
                    else index2 - 1
                )
            last_current_time = current_time

        monsoon_energy_sum = monsoon_data.iloc[idx_start : idx_end + 1][
            "Energy(J)"
        ].sum()
        monsoon_total_time = (
            monsoon_data.iloc[idx_end]["Time(s)"]
            - monsoon_data.iloc[idx_start]["Time(s)"]
        )

        experiment_data.at[index1, "total_energy(J)"] = monsoon_energy_sum
        experiment_data.at[index1, "monsoon_run_time(s)"] = monsoon_total_time
        experiment_data.at[index1, "average_power(W)"] = (
            monsoon_energy_sum / monsoon_total_time
        )

        experiment_data.to_csv(output_file_name, index=False)


### You can use the step 3 codes to merge all the results from different sections
### Only needed when you have more than 1 sections
### Similarly, if you have only one experiment section, keep the code as default

##################################################
# Step 3: Merge experiment result file           #
##################################################


# def merge_tables(file_list):
#     merged_df = pd.read_csv(file_list[0])
#     for file in file_list[1:]:
#         df = pd.read_csv(file)
#         merged_df = pd.concat([merged_df, df])
#     merged_df = merged_df.sort_values(by=["Algorithm", "Language", "GPT"])
#     return merged_df


# files = [
#     "merged_resultx.csv",
#     "merged_resulty.csv",
#     "merged_resultz.csv",
# ]

# merged_df = merge_tables(files)
# merged_df["__run_id"] = ["run_" + str(i) for i in range(1, len(merged_df) + 1)]
# merged_to_drop_column = "Repetitions"
# merged_df = merged_df.drop(columns=merged_to_drop_column)
# merged_df.to_csv("merged.csv", index=False)
