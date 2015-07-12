# unloved_tweets

This is a simple script to delete your tweets after a few minutes if nobody likes them.

Never face the embarrassment of a zero-starred tweet again!

## installation

install dependencies (modern python, tweepy)

## configuration

copy example_settings.py to settings.py and fill in the required twitter api keys

## running

by default it runs in DEBUG mode and DELETES NOTHING

Verify it's working reasonably with -

	$ python unloved_tweets.py

After that change DEBUG to false in your settings.py

you probably will want to put this in your crontab with something like

	*/5 * * * * python ~/src_to_script/unloved_tweets.py

## license

The MIT License (MIT)

Copyright (c) 2015 Adam Mathes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
