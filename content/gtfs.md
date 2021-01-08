Title: GTFS
Date: 2017-06-28
Category: GTFS
Slug: gtfs
Summary: General Transit Feed Specification

## General Transit Feed Specification

[GTFS Field Definitions](https://gtfs.org/reference/static/#field-definitions)

## GTFS Feeds

* [transitfeeds transport-for-ireland](http://transitfeeds.com/p/transport-for-ireland)

## TransitFeed

[github.com/google/transitfeed](https://github.com/google/transitfeed)

### Feed Validator

[/wiki/FeedValidator](https://github.com/google/transitfeed/wiki/FeedValidator)

`python feedvalidator.py dublin_bus_gtfs.zip`

Note: Written for Python 2. Make sure to create conda env with pyton 2.7!

### Schedule Viewer (Map)

`python schedule_viewer.py --feed_filename dublin_bus_gtfs.zip `

then go to `http://localhost:8765/`

Notes: 

* add API key to `/home/user/shared/transitfeed/gtfsscheduleviewer/files/index.html`
* and to `/home/user/shared/transitfeed/schedule_viewer.py` (TBC if this can be dropped)
* restrict API key - see [this SO post](https://stackoverflow.com/questions/46560859/expiredkeymaperror-on-newly-generated-api-key)


## GTFS Ready Set Go

[github.com/ondata/gtfsreadysetgo](https://github.com/ondata/gtfsreadysetgo)

[GTFS, pronti, partenza, via …](https://medium.com/tantotanto/gtfs-pronti-partenza-via-23aa4a42c48e)

`GTFS ready, set, go` is a **bash script** to 

* download a GTFS file, and 
* convert it to a spatialite file (stops and the routes tables)
* create report about the GTFS data
* export the stops and the routes tables in GeoJSON and KML formats

The files produced by this script can be imported int QGIS.

## GTFS Real Time (upcoming)

[github.com/seanrees/gtfs-upcoming](https://github.com/seanrees/gtfs-upcoming)

```
sudo kill -9 `sudo lsof -t -i:6824`
python main.py --config=config.ini --env=prod --port=6824 --promport=800
http://127.0.0.1:6824/upcoming.json
```

Notes:

* [NTA API Developer Portal](https://developer.nationaltransport.ie/)
* add API keys to `/home/user/shared/gtfs-upcoming/config.ini`


## GTFSDB

[github.com/OpenTransitTools/gtfsdb](https://github.com/OpenTransitTools/gtfsdb)

`bin/gtfsdb-load --database_url postgresql://postgres:user@localhost:5432 dublin_bus_gtfs.zip`

Notes:

* Must git clone inside root directory of VM (not the shared directory!)
* [installation with buildout](https://github.com/OpenTransitTools/gtfsdb#install-and-use-via-the-gtfsdb-source-tree)
* the database url must contain `username:password` e.g. `postgres:user`
* the port number can be found using `grep -H '^port' /etc/postgresql/*/main/postgresql.conf`


## Others (to be reviewed)

* [github.com/cbick/gtfs_SQL_importer](https://github.com/cbick/gtfs_SQL_importer)

