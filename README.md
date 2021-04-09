# Gentoo Livecheck

Inspired by the MacPorts `port` subcommand of the same name.

## Requirements

Requires `portage` library to be in the Python path. `import portage` must work
from the Python you run this package with (usually system).

## Heuristic update detection

This package can do automated lookups based on commonly used hosts. Currently:

* GitHub archives
* GitHub commit hashes
* GitHub releases
* JetBrains products
* PyPI

This works as long as the version system is usable with Portage's version
comparison function. For anything else, see [Package configuration](#aaa').

## Package configuration

For packages that will not work with currently heuristic checking, a configuration file named `livecheck.json` can be placed in the directory alongside the ebuild.

### Configuration keys

* `type` - `none`, `regex`, or `checksum`
* `branch` - The GitHub branch name to use for commits
* `no_auto_update` - boolean - Do not allow auto-updating of this package
* `transformation_fuction` - string - Function to use to transform the version
  string. Currently only `dotize` is supported. Others are for internal use.
* `url` - URL of the document to run regular expressions against
* `regex` - The regular expression to use
* `use_vercmp` - boolean - if `vercmp` from Portage should be used. Default: `true`.
