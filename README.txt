resizR is a daemon written in python, which monitors the directory $HOME/resizR
and automatically resizes all images copied into that directory to a
configured, arbitrary list of sizes. It is based on pyinotify [0] and PIL [1].
By default resizR creates a directory called "resizR" in your $HOME directory.
This is configurable in the config file, which will be explained later.

The first time you start it (resizR), it will create a directory structure like this:

$ tree resizR/
$HOME/resizR/
|-- 1024x768
|-- 1280x1024
|-- 1600x1200
`-- 800x600

As soon as you copy a new image into the resizR directory it will create a resized image for
all listed formats.

$ cp foo.png ~/resizR
$ tree resizR/
resizR/
|-- 1024x768
|   `-- foo.png
|-- 1280x1024
|   `-- foo.png
|-- 1600x1200
|   `-- foo.png
|-- 800x600
|   `-- foo.png
`-- foo.png

Since the underlying technology uses the inotify facilities of the linux
kernel, resizR will work with every program be it commandline or graphical.

resizR will also create a directory in your $HOME called .resizR with a file
called resizRconfig.py in it. In that file you can adjust the directory and the
sizes that it will use. Next to that you can also enable automatic cleaning of
the resizR directory on startup. This setting is disabled by default. Please
note that the config file is python code itself and resizR will execute
anything in the global namespace of the config file on startup, so be sure what
you are doing, if you change the file beyond the settings that are provided by
default.

You can run resizR from the checked out git repo or you can run the setup.py
program to install it locally into /usr/bin + its modules in the site-packages
directory of your python installation. The easiest way to use resizR is to put
it in the autostart facilities of your desktop environment or windowmanager,
upon every login is ready to resize any file for you.

I hope you find it useful to some extend and if you change it, please send me
patches!

Author: André Kelpe <efeshundertelf at googlemail dot com>
License: GPLv3 [2]

--
[0] http://trac.dbzteam.org/pyinotify
[1] http://www.pythonware.com/products/pil/
[2] http://www.gnu.org/licenses/gpl-3.0.html
