# Tools

In addition to the data, this folder provides the necessary means for search and querying:

- [`teitok/`](teitok): TEITOK corpus manager for local installation. Note that this is a third-party tool. No guarantees wrt. functionality, security and performance. Currently not recommended for server installation.
- [`core.tei.xml`](../../release/v.0.1/data/core.tei.xml): TEI/XML edition of the core corpus, for processing with TEITOK

While this is recommended for local installation, we also develop components for the
integration of ETCSANS data into CDLI Framework. However, at the moment, their integration
is on-going.

- `pre-annotation/` (external sub-module): when entering morphologically annotated text, this will automatically provide a vanilla annotation for manual correction
- `view/` (external sub-module): visualize and edit ETCSANS annotations
- `query/` (external sub-module): query and visualize ETCSANS annotations
- [`convert/`](convert): export ETCSANS annotations to TEI
