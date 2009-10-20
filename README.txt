resizR is a daemon written in python, which monitors the directory $HOME/resizR
and automatically resizes all images copied into that directory to multiple
sizes. It is based on pyinotify [0] and PIL [1].

The first time you start it (resizR.py), it will create a directory structure like this:

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

It will also create a directory in your $HOME called .resizR with a file
called config.py in it. In that file you can adjust the directory and the
sizes that resizR will use. 

Author: André Kelpe <efeshundertelf at googlemail dot com>
License: GPLv3 [2]
--
[0] http://trac.dbzteam.org/pyinotify
[1] http://www.pythonware.com/products/pil/
[2] http://www.gnu.org/licenses/gpl-3.0.html
