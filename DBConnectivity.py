'''
Created on Jul 29, 2015

@author: Sara
'''
import cx_Oracle

def create_connection():
    return cx_Oracle.Connection('T762208/T762208@10.123.79.57/georli02')

def create_cursor(con):
    return cx_Oracle.Cursor(con)