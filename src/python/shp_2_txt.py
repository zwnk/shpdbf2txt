# OrderedDict([('FeatureId', None), ('DATA_DATE', '20190402'), ('DATA_SRCE', 'http://www.ngs.noaa.gov/cgi-bin/ds_mark.prl?PidBox=DF6866'),
# ('PID', 'DF6866'), ('NAME', '204 S'), ('HT_MOD', ''), ('CORS_ID', ''), ('PACS_SACS', ''), ('STATE', 'MA'),
# ('COUNTY', 'PLYMOUTH'), ('QUAD', ''), ('LATITUDE', '41 48 42.93229(N)'), ('LONGITUDE', '070 57 49.32872(W)'),
# ('DEC_LAT', ' 41.8119256361'), ('DEC_LON', ' -70.9637024222'), ('ELLIP_HT', ''), ('POS_DATUM', 'NAD 83'), ('DATUM_TAG', '(1996)'),
# ('POS_EPOCH', ''), ('POS_SRCE', 'ADJUSTED'), ('ORTHO_HT', '   18.5'), ('VERT_DATUM', 'NAVD 88'), ('VERT_EPOCH', ''), ('VERT_SRCE', 'VERTCON'),
# ('GEOID_HT', '-29.000'), ('GEOID_MOD', 'GEOID12B'), ('DYNAMIC_HT', ''), ('MODEL_GRAV', ''),
# ('N_ACC_HZ', ''), ('N_ACC_EH', ''), ('N_ACC_STDN', ''), ('N_ACC_STDE', ''), ('N_ACC_STDH', ''), ('N_ACC_CORR', ''),
# ('POS_ORDER', '2'), ('VERT_ORDER', ''), ('VERT_CLASS', ''), ('DIST_RATE', ''), ('ECEF_X', ''), ('ECEF_Y', ''), ('ECEF_Z', ''),
# ('SPC_ZONE', 'MA M'), ('SPC_NORTH', '840320.139'), ('SPC_EAST', '244562.406'), ('SPC_CONV', '+0 21 36.9'), ('SPC_CSF', '0.99998907'),
# ('UTM_ZONE', '19'), ('UTM_NORTH', '4630758.769'), ('UTM_EAST', '336889.228'), ('UTM_CONV', '-1 18 34.1'), ('UTM_CSF', '0.99992904'),
# ('STABILITY', 'C'), ('FIRST_RECV', '1972'), ('LAST_RECV', '1972'), ('LAST_COND', 'MONUMENTED'), ('LAST_RECBY', 'MAGS'), ('SAT_USE', ''),
# ('MARKER', 'DE = TRAVERSE STATION DISK'), ('SETTING', '7 = SET IN TOP OF CONCRETE MONUMENT'), ('STAMPING', '204 S')])

from dbfread import DBF

dbf_file = DBF("f:\\testing\\shp_2_txt\\MA.dbf", load=True, encoding='utf8')
txt_file = open("f:\\testing\\shp_2_txt\\MA.txt", 'w')

for idx, record in enumerate(dbf_file):
    txt_file.write(str(record['DEC_LON'] + record['DEC_LAT'] + record['ELLIP_HT'] + record['ORTHO_HT']) + '\n')

txt_file.close()
