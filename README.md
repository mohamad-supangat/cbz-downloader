# CBZ Comic Downloader

Download comics from the web and save them as CBZ files for reading. Ideal for loading up a tablet and offline reading.

CBZ Downloader is a lightly extensible comic downloader, that can assemble comic pages by chapter into CBZ files for use in comic readers, available for [desktop](https://lifehacker.com/5858906/five-best-desktop-comic-book-readers) and [mobile](https://thedroidguy.com/2018/01/5-best-comic-book-reader-apps-android-device-2018-1069923).

## Features

* Extensible base to operate on many web comic hosting sites
	* base object's API provides a number of convenience functions for parsing HTML source
* Creates standardized ZIP/deflate-based CBZ files for individual chapters
* Suport for installation and use on [Termux](https://termux.com/) GNU/Linux environment for Android

### Supported sites

This is the list of sites cbzdl knows how to download from.

* Mangakakalot (including manganelo.com)
* MangaFox (fanfox.net)
* MangaHere (mangahere.cc)
* Manga-Here.io (similar name to above, but different site)
* MangaReader.net

## Installing

You will need [Python 3](https://www.python.org/) and `pip3`

### Linux, Mac

On *nix systems, run

	./install.sh

and the `cbzdl` command will be available to you.

### Windows

These are instructions for setting up a CygWin *nix compatbility layer and installing `cbzdl` to that. Using native Windows python and creating a globally usable command is beyond this author's knowledge.

Install [cygwin](https://www.cygwin.com/) with the following packages

* python3
* pip/setup tools
* git

Then open a cygwin session and run

	git clone https://github.com/taikedz/cbz-downloader
	cd cbz-downloader
	./install.sh

You should now be able to use `cbzdl` from the cygwin command line, whilst in any folder.

## Using

Simply provide a URL to download from - e.g.

	cbzdl http://mangakakalot.com/manga/acaria

To you can specify a start chapter, and end chapter (both optional, as ints or floats)

	cbzdl URL -s START -e END [-d DELAY] [-v]

By default, `cbzdl` will wait 1 second between fetching two images (some sites throttle heavy downloaders). You can affect the delay by providing a `-d DELAY` argument.

If the `-v` option is specified, debug output is printed

## Extending

See [module writing notes](writing_modules.md)
