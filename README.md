# remove_connections_on_LI

I wrote a light Python script to help automate removing all of your LinkedIn contacts. I leveraged the keyboard and time Python modules to emulate keyboard strokes and to evenly send the keystrokes via the wait command. I wrote it in a way that demonstrates the basics of the `keyboard` Python module, and in a way that a novice programmer or even a non-programmer may be able to read it and understand. I may attempt a more elegant solution at a later time with APIs and less reliance on the client/frontend UI aspect of it.

INSTRUCTIONS:

1. Make sure you have `keyboard` and `time` Python modules installed and working properly.
2. Log into your LI account and go to the connections page (.com/mynetwork/invite-connect/connections/).
3. You will then see a list of your contacts. Left click the light grey background (on either sides of the website) in order to reset the sequencing for the script, as the script will be going through a series of tabs to iterate through the fields.
4. Press TAB 4 times to highlight/circle the first portrait on top of that connections list.
5. Open the code and adjust `x` on `line 8` to whichever numeric value you need. I left it at one for testing purposes.
6. Execute the `remove_connections_on_LI.py` from your command line.
7. Press the `q` key on your keyboard to start the script. You may adjust this key in the code on `line 11`.

Please note the sequencing will be off if you do not start off with highlighting the very first connection's portrait by left clicking the light grey background, then pressing the TAB button 4 times.
