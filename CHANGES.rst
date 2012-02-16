Latest Changes
================================================================================


v0.8.1 -- 02/15/2012
--------------------------------------------------------------------------------

* Fixed an issue where the contents of local directories didn't get copied into
  remote directories if the remote directory existed and was empty.


v0.8 -- 02/05/2012
--------------------------------------------------------------------------------

* Added the `--anon` option.
* Added the `-m/--metadata` option.
* Switched from getopt to argparse for argument parsing.
* Changed `boto` dependency to >=2.2.1 (required for the `--anon` option).
