================================================================================
boto rsync v0.7
================================================================================

| Copyright: (c) 2011 Seth Davis
| http://github.com/seedifferently/boto_rsync


Synopsis
================================================================================

boto-rsync is a rough adaptation of boto's s3put script which has been
reengineered to more closely mimic rsync. Its goal is to provide a familiar
rsync-like wrapper for boto's S3 and Google Storage interfaces.

By default, the script works recursively and differences between files are
checked by comparing file sizes (e.g. rsync's --recursive and --size-only
options). If the file exists on the destination but its size differs from
the source, then it will be overwritten (unless the -w option is used).


Installation
================================================================================

To install, simply::

    pip install boto_rsync

* You'll need to have `Python`_ 2.5+ and `pip`_ installed.
* You might have to be root (or use sudo) for pip to install the script into a
  globally executable directory in your $PATH.
* pip should automatically install boto for you, but the advanced user can find
  it here: http://github.com/boto/boto/

.. _Python: http://www.python.org
.. _pip: http://www.pip-installer.org


Usage
================================================================================

::

    boto-rsync [OPTIONS] SOURCE DESTINATION

SOURCE and DESTINATION can be:

* A local path to a directory or specific file
* A custom S3 or GS URI to a directory or specific key in the format of
  s3://bucketname/path/or/key
* A S3 to S3 transfer using two S3 URIs
* A GS to GS transfer using two GS URIs


Examples
================================================================================

::

    boto-rsync [OPTIONS] /local/path/ s3://bucketname/remote/path/

or::

    boto-rsync [OPTIONS] gs://bucketname/remote/path/or/key /local/path/

or::

    boto-rsync [OPTIONS] s3://bucketname/ s3://another_bucket/


Options
================================================================================

::

    -a/--access-key <key>       Your Access Key ID. If not supplied, boto will
                                look for an environment variable or a
                                credentials file.
    -s/--secret-key <secret>    Your Secret Key. If not supplied, boto will look
                                for an environment variable or a credentials
                                file.
    --endpoint <host>           Specify a specific S3 endpoint to connect to via
                                boto's "host" connection argument (S3 only).
    -g/--grant <policy>         A canned ACL policy that will be granted on each
                                file transferred to S3/GS. The value provided
                                must be one of the "canned" ACL policies
                                supported by S3/GS: private, public-read,
                                public-read-write (S3 only), or
                                authenticated-read
    -r/--reduced                Enable reduced redundancy on files copied to S3.
    -e/--encrypt-keys           Enable server-side encryption on files copied
                                to S3 (only applies when S3 is the destination).
    -p/--preserve-acl           Copy the ACL from the source key to the
                                destination key (only applies in S3/S3 and GS/GS
                                transfer modes).
    -w/--no-overwrite           No files will be overwritten, if the file/key
                                exists on the destination it will be kept. Note
                                that this is not a sync--even if the file has
                                been updated on the source it will not be
                                updated on the destination.
    --glob                      Interpret the tail end of SOURCE as a filename
                                pattern and filter transfers accordingly.
                                Note: If globbing a local path, make sure that
                                your CLI's automatic filename expansion is
                                disabled (typically accomplished by enclosing
                                SOURCE in quotes, e.g. "/path/*.zip").
    --no-recurse                Do not recurse into directories.
    --skip-dirkeys              When syncing to S3 or GS, skip the creation of
                                keys which represent "directories" (an empty
                                key ending in "/" for S3 or "_$folder$" for GS).
    --ignore-empty              Ignore empty (0-byte) keys/files/directories.
                                This will skip the transferring of empty
                                directories and keys/files whose size is 0.
                                Warning: S3/GS often uses empty keys with
                                special trailing characters to specify
                                directories.
    --delete                    Delete extraneous files from destination dirs
                                after the transfer has finished (e.g. rsync's
                                --delete-after).
    -n/--dry-run                No files will be transferred, but informational
                                messages will be printed about what would have
                                happened.
    -v/--verbose                Print additional informational messages.
    -d/--debug <level>          Level 0 means no debug output (default), 1 means
                                normal debug output from boto, and 2 means boto
                                debug output plus request/response output from
                                httplib.


Advanced Configuration Options
--------------------------------------------------------------------------------

boto supports the option to read access/secret keys from the environment or from
a credentials file. Set the AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY or
GS_ACCESS_KEY_ID/GS_SECRET_ACCESS_KEY environment variables or use boto's
advanced configuration options to set up a credentials file.

More information on boto's advanced configuration options can be found here:
http://code.google.com/p/boto/wiki/BotoConfig


Known Issues and Limitations
================================================================================

* Differences between keys/files are assumed *only* by checking the size.
* Due to the nature of how directories work in S3/GS, some non-standard folder
  structures might not transfer correctly. Empty directories may also be
  overlooked in some cases. When in doubt, use "-n" first.
* Simple "globbing" (e.g. ``/path/*.zip``) is supported but may behave strangely
  on some systems. See the "--glob" option's help text for more info.
* At this time, the script does not take advantage of boto's "multipart"
  transfer methods. (pull requests welcome!)
* The release version of boto as of this writing (2.1.1) seems to be buggy when
  attempting to perform GS to GS transfers. Use the latest boto github source
  if you need this functionality.


Disclaimers and Warnings
================================================================================

This is Alpha software--always remember to use the "-n" option first!

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
