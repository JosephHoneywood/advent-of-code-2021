import pandas

def register_column_mode(dataframe, col_num, mode_config):
   
    if mode_config == 'most common':
        col_mode = dataframe.iloc[:, col_num].mode()
        return 1 if len(col_mode) >1 else col_mode

    elif mode_config == 'least common':
        col_mode = dataframe.iloc[:, col_num].mode()

        if len(col_mode) > 1: return 0
        return 1 if int(col_mode) == 0 else 0

def drop_by_condition(dataframe, condition, col_number):

    for row_index, row_values in dataframe.iterrows():

        if int(row_values[col_number]) == int(condition): pass
        else: dataframe.drop(row_index, inplace=True)