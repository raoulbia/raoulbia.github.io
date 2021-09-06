Title: Software
Date: 2017-11-25
Category: Linux
Slug: software
Summary: Software


### PostgreSQL

[Download PostgreSQL](https://www.postgresql.org/download/linux/ubuntu/)

[Install pgAdmin](https://linuxhint.com/best_gui_clients_postgresql_ubuntu/#:~:text=pgAdmin,Windows%20and%20Mac%20OS%20X.)

#### Running multiple versions of PostgreSQL

Check the config files to see which version is on which port:

`grep -H '^port' /etc/postgresql/*/main/postgresql.conf`

sample output:

```
/etc/postgresql/10/main/postgresql.conf:port = 5432	
/etc/postgresql/13/main/postgresql.conf:port = 5433	

```

#### Restart Postgres

```
sudo /etc/init.d/postgresql reload
sudo /etc/init.d/postgresql start
```
#### Hostname

PostgreSQL, what is the hostname address of my default database?

If you're connecting from the same machine, use localhost

#### Connection String

You can provide your username and password directly in the connection URI provided to psql:

`psql postgresql://username:password@localhost:5432/mydb`

#### Useful Commands

* To establish a connection : `sudo su - postgres`
* To open a postgress prompt using the command: `psql`
* To see details of the connection: `\conninfo`
* To view the databases in our PostgreSQL instance: `\list`
* `CREATE DATABASE dbname;`
* `DROP DATABASE dbname;`



### R and RStudio

#### Uninstall previous R installation

```
sudo R --no-save
pkgList <- installed.packages(priority='NA')
remove.packages(pkgList)
q()
sudo apt-get remove --purge r-cran* r-base*
```

#### Install on Ubuntu 20.04 (Focal Fossa)

Save and run the script below ([source](https://gist.github.com/mGalarnyk/41c887e921e712baf86fecc507b3afc7)).

```
# Install R + RStudio on Ubuntu 20 Focal
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DF>
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal>
sudo apt update
sudo apt -y install r-base r-base-dev gdebi-core

# next line required for kableExtra
sudo apt -y install libcurl4-openssl-dev openssl libssl-dev openssh-client libxml2-dev 

# next line required for RcppArmadillo
sudo apt -y install liblapack-dev 

# install Latex for RMarkdown
sudo apt -y install texlive texstudio texlive-latex-recommended texlive-latex-extra

# Download and Install RStudio
wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.4.1103-amd64.deb
sudo gdebi rstudio-1.4.1103-amd64.deb
rm rstudio-1.4.1103-amd64.deb
```
#### List of Useful Packages

`install.packages((c("tidyverse", "ggplot2", "ggthemes", "kableExtra", "rbenchmark", "inline", "data.table", "RcppArmadillo"))`


### Docker

* [Install Docker on Ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)
* [Docker Mastery: The Complete Toolset From a Docker Captain](https://www.udemy.com/docker-mastery/):

Docker

  * get relevant `curl` line from [here](https://get.docker.com/).
    Note: this will figure out which version to get for your particular Linux OS
  * run shell script (next line in the above link)
  * `sudo usermod -aG docker vagrant`
  * `docker version` to test

Docker Machine

  * get the lines from [https://github.com/docker/machine/releases](https://github.com/docker/machine/releases)

Docker Compose

  * get lines for latest release [here](https://github.com/docker/compose/releases)
  * `sudo -i` then paste the lines
  * `docker-compse version` to test

<br>

### Pycharm

#### Install
```
$ wget https://download.jetbrains.com/python/pycharm-community-2018.3.4.tar.gz
$ tar -xvf pycharm-community-2018.3.4.tar.gz
$ cd pycharm-community-2018.3.4/bin
$ . pycharm.sh
```

#### pytest

Edit Configuration >> Additional arguments >> `-p no:logging -s`

#### environment variables

* [about setting environment variable e.g. DATA_HOME](https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm)
  
<br>

### Jupyter (via Docker)

* [How to Setup Your JupyterLab Project Environment](https://towardsdatascience.com/how-to-setup-your-jupyterlab-project-environment-74909dade29b)

<br>

### RoboMongo

* [Install MongoDB Community Edition on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
* [Robo 3T: the hobbyist GUI](https://robomongo.org/download)
* [Install Robo3t On Ubuntu 18.04](https://gist.github.com/abdallahokasha/37911a64ad289487387e2d1a144604ae)
* `mongoimport --db naptan --collection naptan --file test.json --jsonArray`


### NodeJS

* npm install xml-stream, xml2js
* node myfile.js

#### NodeJS XML to JSON

```
var fs = require('fs');
var xml2js = require('xml2js');
var util = require('util');

var parser  = new xml2js.Parser();

fs.readFile('NaPTAN_2018_11_08.xml', function(err,data){
    parser.parseString(data, function(err, result){
        
        // console.log(util.inspect(result, false, null, true));

        // fs.writeFile("test", result.toString(), function(err) {
        //     if(err) {
        //         return console.log(err);
        //     }
        //     console.log("The file was saved!");
        // });

        // convert it to a JSON string
        const json = JSON.stringify(result, null, 4);

        // save JSON in a file
        fs.writeFileSync('test.json', json);

    });
});
```

#### 
### GloVe for Python

* `-e git+git@github.com:maciejkula/glove-python.git#egg=glove`
* dependencies
* `pip install Cython`
* `sudo apt-get install python3-dev`



<br>

#### Jena

    wget http://mirrors.whoishostingthis.com/apache/jena/binaries/apache-jena-3.1.1.tar.gz
    tar -zxvf

<br>

#### Fuseki 2 (requires JDK 8)

    wget http://mirrors.whoishostingthis.com/apache/jena/binaries/apache-jena-fuseki-2.4.1.tar.gz
    tar -zxvf
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer

To test fuseki server

    ~/apache-jena-fuseki-2.4.1/fuseki-server --update --loc=angioexplain /angioexplain

Open browser and got to `localhost:3030`

<br>

#### Miniconda3

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

then add below line to `.bashrc`, restart terminal and check installation with `conda -V`.

```export PATH="/home/username/miniconda3/bin:$PATH"```

#### Misc. 

* `sudo apt-get install terminator`

* VSCode Run(Compile): Shit+Ctrl+B 

* to view a .gv GraphViz file (will crate a pdf)

    f = Source.from_file('file-name.gv')
    f.render()
