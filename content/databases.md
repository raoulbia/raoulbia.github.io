Title: Databases
Date: 2017-11-24
Category: Databases
Slug: databases
Summary: Databases


### Postgres

#### install postgres and postgis

$  sudo apt install postgis postgresql-13-postgis-3
$ sudo -u postgres psql
postgres=# \password postgres
postgres=# \q

check installed version(s): `dpkg -l | grep postgres`


#### postgres user authentication error

```sudo nano /etc/postgresql/13/main/pg_hba.conf```

CHANGE FROM

```local   all     postgres     peer```

TO

```local   all      postgres    trusted```

then 
sudo service postgresql restart


#### run in pgadmin4

```CREATE EXTENSION postgis;```


* http://www.orbital.co.ke:8080/opengeo-docs/dataadmin/pgGettingStarted/shp2pgsql.html

* test: `psql -U postgres -d <DBNAME> -c "SELECT postgis_version()"`

* syntax: `shp2pgsql -I -s <SRID> <PATH/TO/SHAPEFILE> <SCHEMA>.<DBTABLE> | psql -U postgres -d <DBNAME>`

* example: `shp2pgsql -I -s 4326  dublinbus/Dublin_Bus.shp  shp_dublinbus | psql -U postgres -d dublinbus`




### Utilities: ogr2ogr

* https://gis.stackexchange.com/questions/65917/can-i-append-to-different-tables-using-ogr2ogr
* https://www.bostongis.com/PrinterFriendly.aspx?content_name=ogr_cheatsheet
* https://www.mankier.com/1/ogr2ogr

#### geojson to shp

```ogr2ogr -f "ESRI Shapefile" destination_data.shp "dcc_public_bin_locations.geojson"```




