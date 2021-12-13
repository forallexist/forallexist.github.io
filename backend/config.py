import os

class Config():

    base_dir_path = os.path.abspath(os.path.dirname(__file__))
    back_dir_path = os.path.join(base_dir_path, 'backend')
    front_dir_path = os.path.join(base_dir_path, 'frontend')
    
    if not os.path.exists(base_dir_path): os.makedirs(base_dir_path)
    if not os.path.exists(back_dir_path): os.makedirs(back_dir_path)
    if not os.path.exists(front_dir_path): os.makedirs(front_dir_path)

class ConfigBack(Config):

    data_dir_path = os.path.join(Config.back_dir_path, 'data')
    
    input_file_name = 'neurips21.csv'
    file_name = input_file_name.split('.')[0]

    output_csv_name = f'word_info_epi_{file_name}.csv'
    output_json_name = f'graph_{file_name}.json'

    columns = ['title', 'episode']

    node_num = 50
    weight_threshold = 1

    input_file_path = os.path.join(data_dir_path, input_file_name)
    output_csv_path = os.path.join(data_dir_path, output_csv_name)
    output_json_path = os.path.join(data_dir_path, output_json_name)

    if not os.path.exists(data_dir_path): os.makedirs(data_dir_path)



