import pandas as pd
import os
import json
import logging as log

from src.pipeline.pipeline import Pipeline

from src.utils.projects_paths import CONFIG_FILE, BASE_PATH

class IngestionPipeline(Pipeline):

    def __init__(self) -> None:
        super().__init__()

        with open(CONFIG_FILE,'r') as f:
            config = json.load(f) 

        self.input_folder_path = config['input_folder_path']
        self.output_folder_path = config['output_folder_path']

        output_filepath = os.path.join(BASE_PATH, self.output_folder_path)
        if not os.path.exists(output_filepath):
            os.makedirs(output_filepath)


    def merge_multiple_dataframe(self):
        """Check for datasets, 
            compile them together, 
            and write to an output file.
        """    
        df_list = pd.DataFrame(columns=['corporation', 'lastmonth_activity', 'lastyear_activity', 'number_of_employees', 'exited'])

        filenames = os.listdir(os.path.join(BASE_PATH, self.input_folder_path))

        for each_filename in filenames:
            df1 = pd.read_csv(os.path.join(BASE_PATH, self.input_folder_path+each_filename))
            df_list=df_list.append(df1)

        data_list = []
        for filename in filenames:
            log.info(f'Ingesting file: {filename}')
            data_list.append(pd.read_csv(os.path.join(BASE_PATH, self.input_folder_path, filename), index_col = None))
        df = pd.concat(data_list, axis = 0, ignore_index = True)

        df.drop_duplicates(inplace = True)

        log.info(f'Saving finaldata.csv and ingestedfiles.txt in : {os.path.join(BASE_PATH, self.output_folder_path)} folder')
        df.to_csv(os.path.join(BASE_PATH, self.output_folder_path, 'finaldata.csv'), index  = False)
        
        ingested_files_pth = os.path.join(BASE_PATH, self.output_folder_path, 'ingestedfiles.txt')
        with open(ingested_files_pth, 'w' ) as file:
            file.write(json.dumps(filenames))

    def run(self):
        self.merge_multiple_dataframe()
