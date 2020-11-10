import json
import pandas as pd
from flask import render_template
import pymysql
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from . import main

pymysql.install_as_MySQLdb()
md = MetaData()
eng = create_engine('mysql://root:Cyukurena13@localhost:3306/bigdata?charset=utf8', echo=True)
session = Session(eng)
daily_data = Table('daily_data', md, autoload=True, autoload_with=eng)
with eng.connect() as conn, conn.begin():
    df = pd.read_sql_table('daily_data', conn)
df = df.sort_values(by='stat_date')
inner_df = df[df.mt == 'inner']
external_df = df[df.mt == 'external']
wechat_df = df[df.mt == 'wechat']
inner_time = list(inner_df['stat_date'].to_numpy())
inner_cost = list(inner_df['cost'].to_numpy())
external_time = list(external_df['stat_date'].to_numpy())
external_cost = list(external_df['cost'].to_numpy())
wechat_time = list(wechat_df['stat_date'].to_numpy())
wechat_cost = list(wechat_df['cost'].to_numpy())


@main.route('/', methods=['GET', 'POST'])
def index():
    new_date = [str(i)[:10] for i in inner_time]
    language = ['python', 'java', 'c', 'c++', 'c#', 'php']
    value = ['100', '150', '100', '90', '80', '90']
    data = {'language': language, 'value': value}
    data_json = json.dumps(data)
    return render_template('main/index.html', data_json=data_json, language=language, value=value,
                           new_date=new_date, inner_cost=inner_cost, external_cost=external_cost, wechat_cost=wechat_cost)
