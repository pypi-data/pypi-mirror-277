#
# Copyright (c) 2022-present Didier Malenfant <didier@malenfant.net>
#
# This file is part of TraktorBuddy.
#
# TraktorBuddy is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TraktorBuddy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License along with TraktorBuddy. If not,
# see <https://www.gnu.org/licenses/>.
#

import pytest
import sys
import os

import xml.etree.ElementTree as ET

from typing import List

# -- We need to import from our parent folder here.
sys.path.append(os.path.join(sys.path[0], '..'))

from TraktorBuddy.folder import Folder           # noqa: E402
from TraktorBuddy.playlist import Playlist       # noqa: E402
from Tests.mock_tracklist import MockTrackList   # noqa: E402


# -- Tests
@pytest.fixture
def test_folder() -> Folder:
    return Folder(MockTrackList(), ET.fromstring('<NODE TYPE="FOLDER" NAME="Damien Plays Records"><SUBNODES COUNT="2"><NODE TYPE="FOLDER" NAME="Episodes"><SUBNODES COUNT="1"><NODE TYPE="PLAYLIST" NAME="Beach House Guestmix"><PLAYLIST ENTRIES="2" TYPE="LIST" UUID="83ac15cf29e1429ca9ac8e077f277ed5"><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Tweet It Forever (DBN Bootleg).mp3"></PRIMARYKEY></ENTRY><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Sunrise (Original Mix).mp3"></PRIMARYKEY></ENTRY></PLAYLIST></NODE></SUBNODES></NODE><NODE TYPE="PLAYLIST" NAME="My Other Playlist"><PLAYLIST ENTRIES="1" TYPE="LIST" UUID="83ac15cf29e1429ca9ac8e077f277ed5"><ENTRY><PRIMARYKEY TYPE="TRACK" KEY="Macintosh HD/:Users/:didier/:Music/:Gigs/:Sunrise (Original Mix).mp3"></PRIMARYKEY></ENTRY></PLAYLIST></NODE></SUBNODES></NODE>'))


def testName(test_folder):
    assert test_folder.name() == 'Damien Plays Records'


def testFolders(test_folder):
    folders: List[Folder] = test_folder.folders()
    assert len(folders) == 1
    assert folders[0].name() == 'Episodes'


def testFoldersFromBufferedValue(test_folder):
    # -- We call folders() twice so that the second time we get the buffered value.
    test_folder.folders()
    folders: List[Folder] = test_folder.folders()
    assert len(folders) == 1
    assert folders[0].name() == 'Episodes'


def testFolderPlaylists(test_folder):
    playlists: List[Folder] = test_folder.playlists()
    assert len(playlists) == 1
    assert playlists[0].name() == 'My Other Playlist'


def testFolderPlaylistsFromBufferedValue(test_folder):
    # -- We call folders() twice so that the second time we get the buffered value.
    test_folder.playlists()
    playlists: List[Folder] = test_folder.playlists()
    assert len(playlists) == 1
    assert playlists[0].name() == 'My Other Playlist'


def testFindForPlaylist(test_folder):
    playlist: Playlist = test_folder.find(['Episodes', 'Beach House Guestmix'])
    assert playlist is not None
    assert type(playlist) == Playlist
    assert playlist.name() == 'Beach House Guestmix'


def testFindForFolder(test_folder):
    folder: Folder = test_folder.find(['Episodes'])
    assert folder is not None
    assert type(folder) == Folder
    assert folder.name() == 'Episodes'


def testFindPlaylist(test_folder):
    playlist: Playlist = test_folder.findPlaylist(['Episodes', 'Beach House Guestmix'])
    assert playlist is not None
    assert playlist.name() == 'Beach House Guestmix'


def testFindUnknownPlaylist(test_folder):
    playlist: Playlist = test_folder.findPlaylist(['Epiwhat', 'Beach House Guestmix'])
    assert playlist is None


def testFindWrongTypePlaylist(test_folder):
    playlist: Playlist = test_folder.findPlaylist(['Episodes'])
    assert playlist is None


def testFindFolder(test_folder):
    folder: Folder = test_folder.findFolder(['Episodes'])
    assert folder is not None
    assert folder.name() == 'Episodes'


def testFindUnknownFolder(test_folder):
    folder: Playlist = test_folder.findFolder(['Epiwhat', 'Beach House Guestmix'])
    assert folder is None


def testFindWrongTypeFolder(test_folder):
    folder: Folder = test_folder.findFolder(['Episodes', 'Beach House Guestmix'])
    assert folder is None


def testFindUnknown(test_folder):
    playlist: Playlist = test_folder.find(['Episodes', 'Beach House Guestmix', 'test'])
    assert playlist is None
