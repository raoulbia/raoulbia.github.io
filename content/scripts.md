Title: Scripts
Date: 2017-05-25
Category: Scripts
Slug: scripts
Summary: Scripts



### Import GTFS data into postgres

```
#!/bin/bash

# init vars
workingFolder=${PWD}
unzip_dir="gtfs_files_unzipped"
fileName="feed_gtfs" 
dbName="gtfs_dublinbus"
user="postgres"
password="postgres"

# create dirs
if [ -d "$workingFolder/$unzip_dir" ]; then \rm -Rf $workingFolder/$unzip_dir; fi
mkdir "$workingFolder/$unzip_dir" > /dev/null 2>&1
# mkdir "$workingFolder/output_test" > /dev/null 2>&1    

# unzip the GTFS file
rm "$workingFolder/$unzip_dir"/*.csv > /dev/null 2>&1
rm "$workingFolder/$unzip_dir"/*.txt > /dev/null 2>&1
unzip -qq -o "$workingFolder/$fileName" -d "$workingFolder/$unzip_dir"

# create a CSV copy of the source txt GTFS files
cd "./$unzip_dir"
for file in *.txt
do
    cp "$file" "../$unzip_dir/${file%.txt}.csv"
done
cd ..

# import into postgres
for file in "$workingFolder/$unzip_dir/"*.csv
do
    filename=$(basename "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"

    ogr2ogr -f PostgreSQL PG:"user=$user dbname=$dbName password=$password" \
            "$workingFolder/$unzip_dir/$filename.csv" -nln "$filename" 
done

\rm "$workingFolder/$unzip_dir/"*.csv

echo "Done"
```

