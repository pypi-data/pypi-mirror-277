# Traktor Buddy

[![GPL-v3.0](https://img.shields.io/badge/license-GPL--3.0-orange)](https://spdx.org/licenses/GPL-3.0-or-later.html) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/TraktorBuddy.svg)](https://python.org) [![PyPI - Version](https://img.shields.io/pypi/v/TraktorBuddy.svg)](https://pypi.org/project/TraktorBuddy)

A helping hand for managing **Traktor** collections.

### Installation

**Traktor Buddy** is a pure Python project. It requires at least [Python](https://python.org) 3.8.

You can install **Traktor Buddy** by typing the following in a terminal window:

```console
pip install TraktorBuddy
```

### Usage from the command line

**Traktor Buddy** supports various commands, sometimes with one or more extra arguments:

```console
tktbud <options> <command> <arguments>
```

The following commands are supported:

```console
help <topic>       - Show a help message. topic is optional (use 'help topics' for a list).
version            - Print the current version.
tag <arguments>    - Add or remove tags (use 'help tag' for a list of arguments).
purge              - Purge all collection backups apart from the most recent.
```

The following options are supported:

```console
--test/-t          - Run in test mode. Affected tracks are printed out. No changes are saved.
--all/-a           - Apply command to all tracks instead of just ones in a playlist/folder.
```

Always keep backups. **Traktor Buddy** creates a backup of your collection in the `Backup` folder of Traktor before modifying anything but it's best to have your own too just in case.

### What is a tag?

Tags are words used to add custom properties or information to tracks. They can then be used to sort tracks more efficiently in smart playlists.

Tags are either single word, which describe a on/off type of value, or can use a `name:value` format which allows for sorting tracks based on a given value.

Most people will use playlists for sorting tracks in their collections but doing this requires manual upkeep. If you wanted to automatically sort your tracks based on, for example, the spot at which those tracks work in your set, you could add tags like `settime:early`,  `settime:late`, etc.. and create smart playlists in Traktor that automatically filter for `Comments2 contains settime:early`.

Another example is, since Traktor doesn't let you create smart playlists based on Playlist membership, you can tag all the tracks in a playlist and then create smart playlists to filter tracks that are in a given playlist and other criterias.

The possibilities are endless.

### Usage as a module

You can use **Traktor Buddy** in your own **Python** scripts to read and modify **Traktor** collections.

```
import TraktorBuddy

collection = TraktorBuddy.Collection()

for track in collection.tracks():
    print(track.title())
```

The module exposes classes for **Collection**, **Folder**, **Playlist**, **Track**, etc...

### License

**TraktorBuddy** is distributed under the terms of the [GPLv3.0](https://spdx.org/licenses/GPL-3.0-or-later.html) or later license.
