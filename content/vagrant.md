Title: Vagrant VM
Date: 2017-12-03
Category: Linux
Slug: Vagrant VM
Summary: Vagrant VM setup

#### Useful Links

* [Ubuntu 20.04 ISO](https://releases.ubuntu.com/20.04/)
* [Building a Vagrant Box from Start to Finish](https://blog.engineyard.com/building-a-vagrant-box)
* [Creating a new Vagrant base box from an existing VM](https://www.abhishek-tiwari.com/creating-a-new-vagrant-base-box-from-an-existing-vm/)


#### Pre-requisites

* [Git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04)
* [Vagrant](http://docs.vagrantup.com/v2/installation/index.html) 
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads).


#### Shared Folders 

Assuming you want to share the directory in which `Vagrantfile` is located and that directory is named `vmtest`. 

* In `Vagrantfile`

    `config.vm.synced_folder "../vmtest", , "/home/vagrant/vmtest", nfs: true`

* In `~/.profile`add

    `sudo mount -t vboxsf vmtest /home/vagrant/vmtest/`

* Set directory permissions on the **HOST** machine

    `chmod 777 -R vmtest/` 


#### Increase Vagrant Box Size

Note: it may be easier to just grab a box that has a large size. See above.

1. Clone & Resize

    on Linux

        VBoxManage clonehd "/home/user/VirtualBox VMs/my_box/box.vmdk" "/home/baba/VirtualBox VMs/my_box/box.vdi" --format vdi
        VBoxManage modifyhd "/home/user/VirtualBox VMs/my_box/box.vdi" --resize 131072
        VBoxManage clonehd "/home/user/VirtualBox VMs/my_box/box.vdi" "/home/baba/VirtualBox VMs/my_box/box-resized.vmdk" --format vmdk

    on Window: same steps as below but first run this:

        set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"


2. Allocate space

    The newly created disk space is unallocated at this stage. Follow these steps next:

    * [getting Gparted](http://www.gitshah.com/2013/05/how-to-fix-out-of-space-problem-for.html?m=1)

    * [changing partitions using Gparted (Video)](https://www.youtube.com/watch?v=cDgUwWkvuIY)

see also [Resize a Hard Disk for a Virtual Machine](https://gist.github.com/christopher-hopper/9755310)

#### Create Global Variable for use in Python Scripts

In `~/.profile`add

```
export TOMOE_DATA_HOME=/home/vagrant/ownCloud/tomoe-data
export KG_OUTPUT_DIR=/home/vagrant/vmtest/tomoe/wp-tomoe-playground/local-data/kg
```

   
#### Useful Vagrant commands

* `vagrant global-status`
* `set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"`
* `vboxmanage list vms`


#### Misc. Links

* [Warning: Authentication failure. Retrying... " after packaging box](https://github.com/hashicorp/vagrant/issues/5186)
* [vagrant-synced-folders-permissions](https://jeremykendall.net/2013/08/09/vagrant-synced-folders-permissions/)
* [vagrant-synced-folders-permissions SO](https://stackoverflow.com/questions/35807568/vagrant-synced-folder-permissions)