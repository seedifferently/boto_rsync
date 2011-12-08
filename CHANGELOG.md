# Changelog #

## v0.5 -- 12/08/2011 ##

 * Added initial support for Google Storage.

## v0.4 -- 12/04/2011 ##

 * Refactored the callback to be more accurate (hopefully).
 * Added estimated time remaining / transfer duration to callback.
 * Fixed a bug where SIGINT might not exit properly.

## v0.3.1 -- 11/30/2011 ##

 * Fixed a bug where the beginning of file/key names were sometimes stripped.
 * Fixed a bug where directory downloads sometimes crashed.

## v0.3 -- 11/30/2011 ##

 * Added an ASCII spinner to help the user understand that the process hasn't
   hung.
 * Fixed bugs from the --ignore_empty and directory features that were added in
   v0.2.

## v0.2 -- 11/29/2011 ##

 * Added the --ignore_empty option.
 * Always assume that a key name ending in "/" is an S3 "directory."

## v0.1 -- 11/27/2011 ##

 * Initial release.
