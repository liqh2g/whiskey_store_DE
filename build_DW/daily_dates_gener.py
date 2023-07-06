import pymysql
import pandas as pd
connection = pymysql.connect(host='localhost', 
                             port= 3306, 
                             user='root',passwd='liqh_root2805', 
                             db = 'dwh_whiskey_shop')

cursor = connection.cursor()

start_date = pd.to_datetime('1990-01-02').date()
end_date = pd.to_datetime('2100-01-01').date()

dates = pd.date_range(start_date, end_date,)

dates_df = pd.DataFrame(dates, columns=['Date'])

dates_df['DateId'] = 1000 * dates_df.Date.dt.year + 100 * dates_df.Date.dt.month + 10 *dates_df.Date.dt.day + dates_df.index

dates_df['Day'] = dates.day_name()

month_dict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',
              5:'May',6:'Jun',7:'Jul',8:'Aug',
              9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

dates_df['Month'] = dates_df['Date'].dt.month
dates_df.Month.replace(month_dict,inplace=True) 

dates_df['Year'] = dates_df.Date.dt.year

assert len(dates_df['DateId'].unique()) == len(dates_df['Date'])

dates_df = dates_df.reindex(columns=['DateId','Date','Day','Month','Year'])

query = '''drop table if exists dwh_date;'''

cursor.execute(query)

query = '''Create Table dwh_date (
    dateId int primary key,
    dates date not null,
    day_name varchar(30) not null,
    month_name varchar(30) not null,
    year_name varchar(30) not null
);'''

cursor.execute(query)

records = dates_df.to_records(index=False)

result = tuple(records)

for data in range(0, len(result)):
    query = '''insert into dwh_date (dateId, dates, day_name, month_name, year_name) 
                values {}    
            '''.format(result[data])
    
    cursor.execute(query)

connection.commit()
