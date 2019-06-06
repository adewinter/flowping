# Installation
* Download this repo to somewhere on your linux/mac based computer
* [Optional] create a symlink to the `flowping.py` file in `/usr/bin/`
* Create a crontab entry to run every 15 mins, it should execute 'flowping.py' (located in this repo).

```
# Create a symlink to flowping.py
sudo ln -s ~/PATH_TO_THIS_REPO/flowping/flowping.py flowping

# Open up a crontab for this specific user
crontab -e

# Enter this to run flowing every 15 minutes:
*/15 * * * * flowping

```

That's it!  A datafile containing your entries is located in `~/.flowping/data.csv`.
