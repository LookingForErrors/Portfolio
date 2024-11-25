from sqlalchemy import insert, text, select, update, table, column
from database import sync_engine
from models import metadata_obj, currency_table
from banks_requests import get_date_value_generator
import csv


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3 UNION SELECT 4, 5, 6"))
        return (f"{res.first()=}")
    
class SyncCore:
    
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def full_parsing_to_table():
        date_value_holder = get_date_value_generator()
        with sync_engine.connect() as conn:
            for elem in date_value_holder:
                for date, val in elem[0].items():
                    stmt = table('currency_table',column('currency_from'), 
                                 column('currency_to'), column('value'), column('date')).insert().values(
                    [
                        # {'currency_from' : elem[1]},
                        # {'currency_to' : 'RUB'},
                        # {'value' : val},
                        # {'date' : date},
                        {'currency_from' : elem[1],
                        'currency_to' : 'RUB',
                        'value' : val,
                        'date' : date},
                    ]
                    )
                    conn.execute(stmt)
            
            conn.commit()

    @staticmethod
    def get_csv(path):
        with sync_engine.connect() as conn:
            result = conn.execute(select(currency_table))

            fh = open('currencies_parser/data.csv', 'w')
            outcsv = csv.writer(fh)

            outcsv.writerow(result.keys())
            outcsv.writerows(result)

            fh.close()

