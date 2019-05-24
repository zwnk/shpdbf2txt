/*
http://shapelib.maptools.org/dbf_api.html

basic funtionality taken from dbfdump.c
path to libshp.dll has to be added as a PATH var

*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

#include "shapefil.h"

int main(int argc, char const *argv[])
{   string dbf_filename;
    string txt_filename;
    if (argc == 1)
    {
        // no arguments given, print help
        cout << "No input and output files defined!" << endl;
        cout << "example: shp_2_txt -i MA.dbf -o MA.txt" << endl;
        return 0;
    }

    // parse arguments
    for (int i = 1; i < argc; i++)
    {
        if (argv[i][0] == '\0')
        {
            continue;
        }
        else if (strcmp(argv[i],"-i") == 0)
        {
            dbf_filename = argv[i + 1];
      
        }
        else if (strcmp(argv[i],"-o") == 0 )
        {
            txt_filename = argv[i + 1];
        }
    }

    DBFHandle dbfh;
    int     i, iRecord;
    char    szTitle[12];

    cout << dbf_filename << " " << txt_filename << endl;

    // open textfile and dbf handle
    ofstream txt_file(txt_filename);
    dbfh = DBFOpen(dbf_filename.c_str(), "rb");

    // check 
    if (dbfh <= 0)
    {
        throw string("File " + dbf_filename + " not found");
    }
    else
    {
        // loop over dbf records 
        for( iRecord = 0; iRecord < DBFGetRecordCount(dbfh); iRecord++ )
        {
            // loop over fields of record
            for( i = 0; i < DBFGetFieldCount(dbfh); i++ )
            {
                // DBFFieldType    eType;
                // eType = DBFGetFieldInfo( dbfh, i, szTitle, &nWidth, &nDecimals );
                string dec_lat = "DEC_LAT";
                string dec_lon = "DEC_LON";
                string ellip_h = "ELLIP_HT";
                string ortho_h = "ORTHO_HT";
                string str(szTitle);
                string line;

                // parse for lat, lon in degrees and orhto height
                if (szTitle == dec_lat or szTitle == dec_lon  or szTitle == ortho_h)
                {
                    txt_file << DBFReadStringAttribute( dbfh, iRecord, i );
                    txt_file << " ";
                }
            }
            txt_file << endl;
           }
        // close dbf handle and textfile
        DBFClose( dbfh );
        txt_file.close();
        cout << "Done." << endl;
    }

    return 0;
}