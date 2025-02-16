import os
import wbgapi as wb

CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_FILE_DIR)
DYNAMIC_DATA_DIR = os.path.join(PARENT_DIR, 'dynamic')

def run():
    series_info = wb.series.info(q='GDP growth')
    file_name = 'business_cycle_info.md'
    with open(os.path.join(DYNAMIC_DATA_DIR, file_name), 'w') as f:
        f.write(str(series_info))

    gdp_growth_df = wb.data.DataFrame('NY.GDP.MKTP.KD.ZG',
            ['USA', 'ARG', 'GBR', 'GRC', 'JPN'], 
            labels=True)
    file_name = 'business_cycle_data.csv'
    gdp_growth_df.to_csv(os.path.join(DYNAMIC_DATA_DIR, file_name))

    series_metadata = wb.series.metadata.get('NY.GDP.MKTP.KD.ZG')
    file_name = 'business_cycle_metadata.md'
    with open(os.path.join(DYNAMIC_DATA_DIR, file_name), 'w') as f:
        f.write(str(series_metadata))


if __name__ == '__main__':
    run()
