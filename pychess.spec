%define istestbuild 0

Name: pychess
Summary: Chess client
License: GPL3
URL: https://pychess.github.io
%define appid io.github.pychess.pychess


# Version: major-minor
%define vermajor 1.0
%define verminor 3
Version: %{vermajor}.%{verminor}


# Release: pkgrel[.extraver][.snapinfo].DIST[.minorbump]
%define _pkgrel 2
%if %{istestbuild}
  %define _pkgrel 1.2
%endif
%define minorbump .taw
BuildArch: noarch
%if ! %{istestbuild}
Release:         %{_pkgrel}%{?dist}%{minorbump}
%else
Release:         %{_pkgrel}.testing%{?dist}%{minorbump}
%endif


Source0: https://github.com/pychess/pychess/archive/%{version}/%{name}-%{version}.tar.gz


AutoReqProv: no

%if 0%{?suse_version:1}
  %{error: "==== OpenSUSE builds cannot be supported. Missing build requirements and running dependencies: python3-gobject, goject-introspection."}
  exit 1
  #BuildRequires: desktop-file-utils appstream-glib
  #BuildRequires: gtk3 librsvg2 gettext sed
  #BuildRequires: python3-devel python-gtk
  #BuildRequires: python3-pexpect python3-SQLAlchemy python3-gobject
  #Requires: python3-pexpect python3-SQLAlchemy python3-gobject python3-psutil
  #Requires: python3-websockets python3-cairo
  #Requires: gobject-introspection glib2 gtk3 pango gdk-pixbuf gtksourceview
  #Requires: gstreamer gstreamer-plugins-good
%endif

%if 0%{?rhel:1}
  %{error: "==== CentOS Stream and EL builds cannot be supported. Missing build requirements and running dependencies: python-gobject (EL8), pyton-pexpect (EL8), python-sqlalchemy (EL8,9)."}
  exit 1
%endif

%if 0%{?fedora:1}
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: gtk3 librsvg2 gettext sed

BuildRequires: python3-devel
BuildRequires: python-pexpect python-sqlalchemy python-gobject

Requires: python-pexpect python-sqlalchemy python-gobject python-psutil
Requires: python-websockets python-cairo python-gstreamer1
Requires: gobject-introspection glib2 gtk3 pango gdk-pixbuf2 gtksourceview3
Requires: gstreamer1 gstreamer1-plugins-base 
#Requires: stockfish
%else
  %{error: "==== Uknown OS platform. Builds can not be supported."}
  exit 1
%endif


%description
PyChess is a chess client for playing and analyzing chess games. It is
intended to be usable both for those totally new to chess as well as
advanced users who want to use a computer to further enhance their play.

PyChess has a builtin python chess engine and auto-detects most
popular chess engines (Stockfish, Rybka, Houdini, Shredder, GNU Chess,
Crafty, Fruit, and many more). These engines are available as opponents,
and are used to provide hints and analysis. PyChess also shows analysis
from opening books and Gaviota end-game tablebases.

When you get sick of playing computer players you can login to FICS (the
Free Internet Chess Server) and play against people all over the world.
PyChess has a built-in Timeseal client, so you won't lose clock time during
a game due to lag. PyChess also has pre-move support, which means you can
make (or start making) a move before your opponent has made their move.

PyChess has many other features including:
- CECP and UCI chess engine support with customizable engine configurations
- Polyglot opening book support
- Hint and Spy move arrows
- Hint, Score, and Annotation panels
- Play and analyze games in separate game tabs
- 18 chess variants including Chess960, Suicide, Crazyhouse, Shuffle, Losers, Piece Odds, and Atomic
- Reads and writes PGN, EPD and FEN chess file formats
- Undo and pause chess games
- Move animation in games
- Drag and drop chess files
- Optional game move and event sounds
- Chess piece themes with 40 built-in piece themes
- Legal move highlighting
- Direct copy+paste pgn game input via Enter Game Notation open-game dialog
- Internationalised text and Figurine Algebraic Notation (FAN) support
- Translated into 38 languages (languages with +5% strings translated)
- Easy to use and intuitive look and feel


%prep
%setup -q -n %{name}-%{version}


%build
/usr/bin/python3 setup.py build


%install
/usr/bin/python3 setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES
# patch the metainfo.xml and then validate it
sed -i -e '{s/<desktop-application>/<component type="desktop-application">/}' %{buildroot}%{_metainfodir}/*.metainfo.xml
sed -i -e '{s:</desktop-application>:</component>:}' %{buildroot}%{_metainfodir}/*.metainfo.xml
sed -i -e '{s:<licence>GFDL</licence>:<project_license>GFDL</project_license>\n <metadata_license>GFDL</metadata_license>:}' %{buildroot}%{_metainfodir}/*.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files -f INSTALLED_FILES
%defattr(-,root,root)


# Credit, original developer: Thomas Dybdahl Ahle <pychess-people@googlegroups.com>
# https://www.chessprogramming.org/Thomas_Dybdahl_Ahle
# The upstream project's RPM build sets the deprecated Vendor. RPM no longer
# uses that value, therefore it was removed. Credit, though, where credit is due.

# TODO
# Resolve this dialog that pops up when you run the program for the first time:
# Some PyChess features require further permission in order to download external components
# [] database querying needs scoutfish https://github.com/pychess/scoutfish
# [] database opening tree needs chess_db https://github.com/pychess/chess_db
# [] ICC lag compensation needs timestamp http://download.chessclub.com/timestamp/
# [] Don't show this dialog on startup.
#                              [OK]


%changelog
* Tue Aug 24 2021 Todd Warner <t0dd@protonmail.com> 1.0.3-2.taw
* Tue Aug 24 2021 Todd Warner <t0dd@protonmail.com> 1.0.3-1.2.testing.taw
  - BuildRequires cleanup
  - upstream metainfo.xml doesn't validate. I patch that and validate it
  - stubbed-out stanzas for potential SUSE and CentOS support

* Sun Aug 15 2021 Todd Warner <t0dd@protonmail.com> 1.0.3-1.taw
* Sun Aug 15 2021 Todd Warner <t0dd@protonmail.com> 1.0.3-0.2.testing.taw
  - The specfile Group tag is no longer used. You define that kind of stuff in the pychess.desktop file.
  - The specfile clean section is no longer used.
  - fixed the Release string building logic
  - Not pulling in the python-websockets Requires for some reason. I blame AutoReqProv  
    read: https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/  
    read: https://stackoverflow.com/questions/16598201/disable-rpmbuild-automatic-requirement-finding

* Fri Aug 13 2021 Todd Warner <t0dd@protonmail.com> 1.0.3-0.1.testing.taw
  - https://github.com/pychess/pychess/releases/tag/1.0.3
  - Doesn't completely cleanly. Some error when building the opening book (eco?) database (I think).  
    Several of these in the build: "Unable to init server: Could not connect: Connection refused"  
    What server? I don't know.

