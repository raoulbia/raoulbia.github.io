Title: SSH Keys
Date: 2017-12-01
Category: Linux
Slug: ssh_keys
Summary: SSH Keys


#### Checking for existing keys

    ls -al ~/.ssh

#### Generating a new key

    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

or
       
    ssh-keygen -t rsa -C "some name" -b 4096

#### Adding a key

    eval $(ssh-agent -s)
    ssh-add ~/.ssh/id_rsa

####  Copy the contents of the SSH key to your clipboard

    clip < ~/.ssh/id_rsa.pub
