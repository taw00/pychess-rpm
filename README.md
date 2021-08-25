# PyChess — an open-source desktop chess application and engine

_.&nbsp;.&nbsp;.&nbsp;packaged for Fedora Linux (CentOS and OpenSUSE builds not currently functional)_

**PyChess . . .**  
PyChess is a full-featured desktop chess gaming application designed primarily
for the GNOME desktop application (Linux/UNIX) framework. With PyChess you can
play offline wagainst another human or computer (using just about any chess
engine installed on your system—[I recommend
Stockfish](https://github.com/taw00/stockfish-rpm)). PyChess also supports
playing online players from around the world via the
[FICS](http://www.freechess.org/) or [ICC](https://www.chessclub.com/) chess
servers.

PyChess aims to be a clean, well-designed, interface, and I personally think it
is the best overall chess client for the Linux desktop.

_**What is this GitHub Repository?**_

The purpose of this repository is to store all the bits and pieces needed to
build and package this application for various RPM flavors of Linux. The binary
(installable and runnable) packages are then built via the [Fedora Project's
COPR build system](https://copr.fedorainfracloud.org/coprs/taw/pychess/).

I store all *my* contributions needed to enable building and packaging PyChess
in this repository. Upstream code—for example, `pychess-1.0.3.tar.gz`—will not
be redundantly stored here. Those can be found ...
[upstream](https://github.com/pychess/pychess). If you know your way around
building RPMs, you will know how to work with the specfile and other
contributions found here.

## tl;dr&nbsp;.&nbsp;.&nbsp;.

### I just want to play chess!

#### [Fedora only for now]

**Prep&nbsp;.&nbsp;.&nbsp;.**
```bash
sudo dnf install -y dnf-plugins-core distribution-gpg-keys
sudo dnf copr enable taw/pychess
```

**Install&nbsp;.&nbsp;.&nbsp;.**
```bash
sudo dnf install -y pychess --refresh
```

### I installed it, now I want to play a game!

1. Browse your software menus
2. Applications --> Games
3. Choose PyChess
4. Play chess!

## More about&nbsp;.&nbsp;.&nbsp;.

* [PyChess](https://pychess.github.io/) — desktop - the PyChess upstream
  project website for this software. <https://pychess.github.io/>  
  But to install my build:  
  `sudo dnf copr enable taw/pychess`  
  `sudo dnf install pychess --refresh -y`
* [Stockfish](https://stockfishchess.org/) — engine - currently, the top chess
  engine on the planet, and it is open-source. My build of the Stockfish chess
  engine (install this version) can be found here:
  <https://github.com/taw00/stockfish-rpm>  
  `sudo dnf copr enable taw/stockfish`  `sudo dnf install stockfish --refresh -y`
* [Gnome Chess](https://wiki.gnome.org/Apps/Chess) — desktop - another great
  open-source chess frontend. It has a particularly clean and simple interface,
  but is a bit less versatile as compared to PyChess.  
  `sudo dnf install gnome-chess --refresh -y`
* [GNU Chess](https://www.gnu.org/software/chess/) — engine - a common chess
  engine that often is installed on Linux systems. It's not anywhere close to
  being as strong as Stockfish, but it's still stronger than you are at chess.  
  `sudo dnf install gnuchess --refresh -y`
* [LiChess.org Server](https://lichess.org/) — server - an open-source and
  modern online chess server.  This is, IMHO, the best chess server out there.
  It's web interface is spectacular. It does not plug into the various desktop
  clients though (to avoid cheaters using chess hinting, etc). Some mobile
  applications plug in though.
* [Free Internet Chess Server (FICS)](https://www.freechess.org/) — server -
  one of the oldest and most popular chess servers. The web interface is awful
  and all play is done through an external client. Its default client is a Java
  Applet though, but since Java Applets are a thing of the past, setting up and
  managing your account is challenging to say the least. Once your account is set
  up, though, some clients, like PyChess, plug right in.
* [PyChess Variants Server](https://www.pychess.org) — server - written by the
  same guy, but not the same software. This is a chess server modeled after
  LiChess.org, but with focus on all the weird and wacky chess variants out there.

## Disclaimer

PyChess already ships with Fedora and most other Linux distributions, but those
vendor-supplied versions are usually woefully out of date (Fedora ships a version
of PyChess from 2016!, for example). Therefore, I offer this build for your own
convenience. I make no guarantee that it works as it should. Buyer beware. :) I am
in no way affiliated with the developers of PyChess, but I do thank them and
the larger PyChess community who have created an incredible chess application.

The upstream project makes an RPM available, but (a) it isn't available in a
convenient repository, and (b) it doesn't build in a sanitized build environment (ala
COPR). My binary RPM build exists for these reasons.

## Questions or comments&nbsp;.&nbsp;.&nbsp;.

Contact: **t0dd_at_protonmail.com** or find me at **@t0dd:matrix.org** in the [Matrix](https://github.com/taw00/element-rpm) social medias.
