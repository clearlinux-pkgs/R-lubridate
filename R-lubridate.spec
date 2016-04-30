#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lubridate
Version  : 1.5.6
Release  : 24
URL      : http://cran.r-project.org/src/contrib/lubridate_1.5.6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/lubridate_1.5.6.tar.gz
Summary  : Make Dealing with Dates a Little Easier
Group    : Development/Tools
License  : GPL-2.0
Requires: R-lubridate-lib
Requires: R-stringr
BuildRequires : R-stringr
BuildRequires : clr-R-helpers

%description
[![Build Status](https://travis-ci.org/hadley/lubridate.png?branch=master)](https://travis-ci.org/hadley/lubridate)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/lubridate/master.svg)](https://codecov.io/github/hadley/lubridate?branch=master)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/lubridate)](https://cran.r-project.org/package=lubridate)
[![Development version](https://img.shields.io/badge/devel-1.5.0.9000-orange.svg)](https://github.com/hadley/lubridate)
[![CRAN version](http://www.r-pkg.org/badges/version/lubridate)](http://cran.r-project.org/package=lubridate)

%package lib
Summary: lib components for the R-lubridate package.
Group: Libraries

%description lib
lib components for the R-lubridate package.


%prep
%setup -q -c -n lubridate

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library lubridate
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lubridate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lubridate/CITATION
/usr/lib64/R/library/lubridate/DESCRIPTION
/usr/lib64/R/library/lubridate/INDEX
/usr/lib64/R/library/lubridate/Meta/Rd.rds
/usr/lib64/R/library/lubridate/Meta/data.rds
/usr/lib64/R/library/lubridate/Meta/hsearch.rds
/usr/lib64/R/library/lubridate/Meta/links.rds
/usr/lib64/R/library/lubridate/Meta/nsInfo.rds
/usr/lib64/R/library/lubridate/Meta/package.rds
/usr/lib64/R/library/lubridate/Meta/vignette.rds
/usr/lib64/R/library/lubridate/NAMESPACE
/usr/lib64/R/library/lubridate/NEWS.md
/usr/lib64/R/library/lubridate/R/lubridate
/usr/lib64/R/library/lubridate/R/lubridate.rdb
/usr/lib64/R/library/lubridate/R/lubridate.rdx
/usr/lib64/R/library/lubridate/data/Rdata.rdb
/usr/lib64/R/library/lubridate/data/Rdata.rds
/usr/lib64/R/library/lubridate/data/Rdata.rdx
/usr/lib64/R/library/lubridate/doc/index.html
/usr/lib64/R/library/lubridate/doc/lubridate.R
/usr/lib64/R/library/lubridate/doc/lubridate.Rmd
/usr/lib64/R/library/lubridate/doc/lubridate.html
/usr/lib64/R/library/lubridate/help/AnIndex
/usr/lib64/R/library/lubridate/help/aliases.rds
/usr/lib64/R/library/lubridate/help/lubridate.rdb
/usr/lib64/R/library/lubridate/help/lubridate.rdx
/usr/lib64/R/library/lubridate/help/paths.rds
/usr/lib64/R/library/lubridate/html/00Index.html
/usr/lib64/R/library/lubridate/html/R.css
/usr/lib64/R/library/lubridate/tests/testthat.R
/usr/lib64/R/library/lubridate/tests/testthat/test-Dates.R
/usr/lib64/R/library/lubridate/tests/testthat/test-POSIXt.R
/usr/lib64/R/library/lubridate/tests/testthat/test-accessors.R
/usr/lib64/R/library/lubridate/tests/testthat/test-am-pm.R
/usr/lib64/R/library/lubridate/tests/testthat/test-daylight-savings.R
/usr/lib64/R/library/lubridate/tests/testthat/test-decimal-date.R
/usr/lib64/R/library/lubridate/tests/testthat/test-difftimes.R
/usr/lib64/R/library/lubridate/tests/testthat/test-durations.R
/usr/lib64/R/library/lubridate/tests/testthat/test-guess.R
/usr/lib64/R/library/lubridate/tests/testthat/test-instants.R
/usr/lib64/R/library/lubridate/tests/testthat/test-intervals.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-addition.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-division.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-integer-division.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-modulo.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-multiplication.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-subtraction.R
/usr/lib64/R/library/lubridate/tests/testthat/test-parsers.R
/usr/lib64/R/library/lubridate/tests/testthat/test-periods.R
/usr/lib64/R/library/lubridate/tests/testthat/test-pretty.R
/usr/lib64/R/library/lubridate/tests/testthat/test-settors.R
/usr/lib64/R/library/lubridate/tests/testthat/test-stamp.R
/usr/lib64/R/library/lubridate/tests/testthat/test-timespans.R
/usr/lib64/R/library/lubridate/tests/testthat/test-timezones.R
/usr/lib64/R/library/lubridate/tests/testthat/test-update.R
/usr/lib64/R/library/lubridate/tests/testthat/test-utilities.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lubridate/libs/lubridate.so
