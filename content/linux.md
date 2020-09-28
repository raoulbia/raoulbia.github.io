Title: Linux
Date: 2017-12-02
Category: Linux
Slug: Linux
Summary: Linux


#### Useful Commands

* `sudo tar xzvf package_file.tar.gz`
* `sudo dpkg -i package_file.deb`
* `cat /etc/*release`
* `echo $XDG_CURRENT_DESKTOP`
* `sudo find ~/ -name rdflib`
* `sudo find / -name "*.cls"`
* ``` sudo kill -9 `sudo lsof -t -i:8888` ```

#### Handy Tools

   * [Fish](https://fishshell.com/): `sudo apt-get install fish`
   * [Tmux](https://linuxize.com/post/getting-started-with-tmux/): `sudo apt-get install tmux`
   

#### Pip install problems 

```
sudo apt-get install aptitude
sudo aptitude install ...
```

#### tmux Sessions

* `tmux new -s session_name` new session
* `tmux a -t session_name` attach
* `ctrl + b` then `d` detach
* `ctrl + b` then 'x' terminate session
* `ctrl + b` then `(` move between sessions
* `ctrl + b` the 'c` to make a new tab in an existing session
* `ctrl + b` then the number of the tab e.g. `0` or `1` to move between tab
* `htop` + Enter to see running processes (create new tab inside session)

#### File Handling

* `tar xzvf archive_name.tar.gz` to uncompress tar.gz file
* `tar xjvf archive_name.tar.bz2` to uncompress tar.bz2 file
* `less file.csv` to open file
* `q + enter` to close and exit
* `zcat file.tsv.gz | more` to view fcompressed gz file
* `zcat file.tsv.gz | grep "pattern match"` to find string
* `cat -vet file` to see hidden chars
* `uniq -d file.txt` to get duplicate lines
* `cat gene2refseq | awk '{if ($1==6239) print $0}' | head`

#### Packages

* To see packages and their size `conda clean --all`
* To clean up `du -sh */`
* To remove package

        sudo apt-get remove r-base
        sudo apt-get purge texlive*

* To reinstall package

        sudo apt-get install --reinstall package_name

* `dpkg -l | grep miktex` to see what's installed
* `dpkg -L package-name` to list files installed by some package
* `dpkg -l | grep package_name` to see if package is installed


#### Show git branch name in Terminal

Add this to `.bashrc`:

    :::python
    force_color_prompt=yes
    color_prompt=yes
    parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
    }
    if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
    else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
    fi
    unset color_prompt force_color_prompt

<br>

#### `apt-get` vs. `pip install` vs. `conda install`

* `apt-get` installs a (python) package/module system-wide.
* `pip` installs module in venv only.
* If using `pip install` after activating the venv, module will be installed into that venv only.
* `pip` installs a package/module within any environment.
* `conda` installs module/package within conda environments.

#### Pip Cache

* `pip config set global.cache-dir false`
* `pip install NAME --no-cache-dir` e.g. `pip --no-cache-dir install scipy`
* `sudo rm -R ~/.cache/pipenv` and `sudo rm -R ~/.cache/pip`

#### Misc.

* `df -h` check disk space
* [kill process](https://itsfoss.com/how-to-find-the-process-id-of-a-program-and-kill-it-quick-tip/)
* `rm file` to remove file
* `rm -r dirName` to remove directory
* `ln -s /opt/robomongo/bin/robomongo ~/robomongo_lnk` to make a shortcut/alias
* `pip list --local` to list installed packages in a given venv
* about the double dash `--`
    * Almost all short options have a corresponding long option; `rm -f` is equivalent to `rm --force`.
    * Many long options, though, have no corresponding short option.
* [About the usr/bin directory](http://askubuntu.com/questions/739297/how-to-install-robomongo-ubuntu-system-please-let-me-know/781793)
* [Increase Digitalocean memory](https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-18-04)

