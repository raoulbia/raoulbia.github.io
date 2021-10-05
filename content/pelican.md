Title: Pelican How To
Date: 2018-04-25
Category: Python
Slug: pelican
Summary: Pelican How To

[Pelican](https://blog.getpelican.com/) is a static site generator, written in Python, that requires no database or server-side logic.

### Environment Setup

1. Create a public repository on github e.g. username.github.io

2. Create a project directory for your blog and save the `requirements.txt` file in that directory. See the links in the
   Resources section below for examples of what the file should contain.

3. Setup a virtual environment

        conda create --name myblog python=3.5
        conda activate myblog
        pip install -r requirements.txt
        pelican-quickstart
        git clone https://github.com/getpelican/pelican-plugins.git


4. Connect to repo

        git remote add origin git@github.com:raoulbia/raoulbia.github.io.git

    To test run `git remote -v`. You should see your repo listed.

5. Create a new branch for hosting the pelican source code.

        git checkout -b pelican

6. Install IPython notebook

        mkdir plugins && cd plugins
        git submodule add git://github.com/danielfrg/pelican-ipynb.git ipynb
        git submodule add https://github.com/barrysteyn/pelican_plugin-render_math.git render_math
        

7. In order to activate the plugin, add these lines at the bottom of `pelicanconf.py`:

        MARKUP = ('md', 'ipynb')
        PLUGIN_PATH = './plugins'
        PLUGINS = ['ipynb.markup', 'render_math']

7. Fetch ``.gitignore` from [here](https://github.com/getpelican/pelican-blog/blob/master/.gitignore) - save it to root


### Pelican Themes

The installation of themes proved to be rather tricky. It is possible to add all existing Pelican themes to your
development repository. However in my experience they are not straightforward to install or don't work. I may have done
something wrong when trying to do so but in the end I settled for the [blue-penguin](https://github.com/jody-frankowski/blue-penguin)
theme. It should be noted that the default Pelican theme may suffice to some users in which case this section can be
skipped.

To add all existing Pelican themes to your development repository

    git clone --recursive https://github.com/getpelican/pelican-themes ./pelican-themes

To install one of the downloaded themes

    pelican-themes --install ./pelican-themes/name-of-theme --verbose

Alternatively you can just get the one theme you want to use

    git clone https://github.com/jody-frankowski/blue-penguin.git ./pelican-themes


#### Config Files

Now to the part that took me a while to figure out: 
the theme of choice must be specified in **both** `publishconf.py` and `pelicanconf.py`!


* in `publishconf.py` add the following line: `THEME = "blue-penguin"`

* in `pelicanconf.py` add the following line: `THEME = "./pelican-themes/blue-penguin"`


### Local Testing

Note: First, activate your virtual environment e.g. `$ source activate venv-name`

1. start Localhost : `make devserver`

1. add/remove/modify page(s)

4. preview `localhost:8000/` in your browser

    To stop localhost type `Ctrl + c` then run below command twice

        kill -9 $(lsof -i TCP:8000 | grep LISTEN | awk '{print $2}')


### Deploy to Github

Note: First, activate your virtual environment e.g. `$ source activate venv-name`

There are two sides to Pelican publishing on Github: publishing the blog pages (master branch) and pushing the
project source code (pelican branch). To publish either run the code below.

---
**NOTE**
  IMPORTANT RUN THIS FROM THE PELICAN BRANCH!
---

#### Publish Blog pages

    pelican content -o output -s pelicanconf.py &&
    ghp-import output -r origin -b master &&
    git push origin master

#### Push Source Code

    git add -A &&
    git commit -a -m "Update" &&
    git push -u origin pelican


### Finally ...

Try visiting your page e.g. <http://raoulbia.github.io> -- you should see your blog!


#### Useful Links

* (Pelican and ipynb error)[http://marohn-public.site44.com/Marohn-20171011-102214--Pelican-and-ipynb.html]
* <http://anotherdatum.com/pelican-and-github-pages-workflow.html> (Excellent!)
* <http://www.christianlong.com/blog/more-on-pelican-themes.html>
* <https://rasor.github.io/using-pelican-blog-on-github-pages.html>
* <http://jamesnewbrain.com/how-to-host-pelican-github-vps-blog.html#ii-use-pelicans-simple-dev-server-to-preview-posts-in-browser-as-you-edit>
* <http://docs.getpelican.com/en/3.3.0/getting_started.html>
* <http://docs.getpelican.com/en/3.6.3/content.html#syntax-highlighting>
* <http://jamesgregson.ca/using-the-pelican-static-website-generator.html> (change CSS)

#### Change Blog CSS

`C:\Users\USER\vmtest\myblog\pelican-themes\blue-penguin\static\css`
