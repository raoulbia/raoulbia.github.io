Title: Software
Date: 2017-11-07
Category: Linux
Slug: linux software
Summary: Software


### R and RStudio

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
wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.3.1056-amd64.>
sudo gdebi rstudio-1.3.1056-amd64.deb
rm rstudio-1.3.1056-amd64.deb
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

```
$ wget https://download.jetbrains.com/python/pycharm-community-2018.3.4.tar.gz
$ tar xvzf pycharm-community-2018.3.4.tar.gz
$ cd pycharm-community-2018.3.4/bin
$ . pycharm.sh
```

* [about setting environment variable e.g. DATA_HOME](https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm)
  
<br>

### Jupyter (via Docker)

* [How to Setup Your JupyterLab Project Environment](https://towardsdatascience.com/how-to-setup-your-jupyterlab-project-environment-74909dade29b)

<br>

### GloVe for Python

* `-e git+git@github.com:maciejkula/glove-python.git#egg=glove`
* dependencies
* `pip install Cython`
* `sudo apt-get install python3-dev`


#### RoboMongo

    cd /opt
    sudo wget https://download.robomongo.org/1.0.0/linux/robomongo-1.0.0-linux-x86_64-89f24ea.tar.gz
    sudo tar -zxvf robomongo-1.0.0-linux-x86_64-89f24ea.tar.gz
    sudo rm robomongo-1.0.0-linux-x86_64-89f24ea.tar.gz
    robomongo

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

#### Misc. 

to view a .gv GraphViz file (will crate a pdf)

    f = Source.from_file('file-name.gv')
    f.render()
