# Mass delete of forked github repos from a certain source

This is a simple python (3) command line script that will check the parents of any forked repos for an unwanted string, and then ask you if you want to delete the listed repos.

It was created to delete repos from The Flatiron School (where every exercise you did clogged your github account with a new forked repository)

It takes two commmand line arguments, the first being the unwanted string and the second being a github api key with list and delete privileges.

For example:

`python . learn abcd-this-is-a-fake-token`