def map_config(config):
    return {
        'ENV': config['default']['ENVIRONMENT'],
        'DEBUG': config['default']['DEBUG'],
        'PORT': int(config['default']['PORT']),
        'PE_NUMBER_CSV_URL': config['default']['PE_NUMBER_CSV_URL'],
        'SQLALCHEMY_DATABASE_URI': config['default']['DATABASE_URI'],
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
