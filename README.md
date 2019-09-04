# applausequery
Package to perform some standard queries to APPLAUSE [1] using PyVO [2].

## About
Archives of Photographic PLates for Astronomical USE (APPLAUSE) is an effort to
digitize and publish astronomical photographic plates including its
metadata. While easy data access is provided by the service's web interface,
for many tasks a scripted access makes life easier, especially when working
with other data analysis packages. For such an access, APPLAUSE provides
a TAP service.

applausequery accesses the TAP interface using the PyVO package. Its main
intention is to provide scripted data access for tasks common to APPLAUSE.

## Notes
Although we also provide submodules for the first two data releases, only
queries for DR3 are implemented for now. 

## References
[1] APPLAUSE: https://www.plate-archive.org/applause

[2] PyVO: https://github.com/astropy/pyvo
