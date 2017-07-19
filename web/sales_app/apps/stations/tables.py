'''
Datatable2 configurations
'''
import django_tables2 as tables
from stations.models import Station


class StationTable(tables.Table):
    '''
     Datatable2 configurations
    '''
    class Meta:
        '''
         Meta Data
        '''
        model = Station
        attrs = {'id': 'DataTables_Table_0_wrapper'}
