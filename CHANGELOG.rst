================================================================================
Changelog
================================================================================


v0.8 -- 02/05/2012
================================================================================

* Added the `--anon` option.
* Added the `-m/--metadata` option.
* Switched from getopt to argparse for argument parsing.
* Changed `boto` dependency to >=2.2.1 (required for the `--anon` option).


v0.7 -- 01/09/2012
================================================================================

* Added the `--glob` option.
* Added the `--endpoint` option.
* Long form options were renamed from `--long_name` to `--long-name`.
* Made the creation of remote "directory keys" the default behavior and added
  the `--skip-dirkeys` option.
* Fixed issue with `--long-option` arguments not being parsed correctly.


v0.6 -- 12/11/2011
================================================================================

* Added the `--no_recurse` option.
* Fixed an issue where output on Windows was improperly formatted.


v0.5.1 - v0.5.3 -- 12/08/2011 - 12/10/2011
================================================================================

* Added info on boto's advanced configuration options.
* Fixed boto's version requirement. The "encrypt_key" option requires boto v2.1
  or greater.
* Fixed issues with PyPI.
* Fixed/updated setup script.


v0.5 -- 12/08/2011
================================================================================

* Added initial support for Google Storage.


v0.4 -- 12/04/2011
================================================================================

* Refactored the callback to be more accurate (hopefully).
* Added estimated time remaining / transfer duration to callback.
* Fixed a bug where SIGINT might not exit properly.


v0.3 - v0.3.1 -- 11/30/2011
================================================================================

* Added an ASCII spinner to help the user understand that the process hasn't
  hung.
* Fixed bugs from the `--ignore_empty` and directory features that were added in
  v0.2.
* Fixed a bug where the beginning of file/key names were sometimes stripped.
* Fixed a bug where directory downloads sometimes crashed.


v0.2 -- 11/29/2011
================================================================================

* Added the `--ignore_empty` option.
* Always assume that a key name ending in "/" is an S3 "directory."


v0.1 -- 11/27/2011
================================================================================

* Initial release.
