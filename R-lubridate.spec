#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lubridate
Version  : 1.7.9
Release  : 85
URL      : https://cran.r-project.org/src/contrib/lubridate_1.7.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lubridate_1.7.9.tar.gz
Summary  : Make Dealing with Dates a Little Easier
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-lubridate-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-generics
BuildRequires : R-Rcpp
BuildRequires : R-generics
BuildRequires : buildreq-R

%description
fast and user friendly parsing of date-time data, extraction and
    updating of components of a date-time (years, months, days, hours,
    minutes, and seconds), algebraic manipulation on date-time and
    time-span objects. The 'lubridate' package has a consistent and
    memorable syntax that makes working with dates easy and fun.  Parts of
    the 'CCTZ' source code, released under the Apache 2.0 License, are

%package lib
Summary: lib components for the R-lubridate package.
Group: Libraries

%description lib
lib components for the R-lubridate package.


%prep
%setup -q -c -n lubridate
cd %{_builddir}/lubridate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591717344

%install
export SOURCE_DATE_EPOCH=1591717344
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lubridate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lubridate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lubridate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lubridate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lubridate/CITATION
/usr/lib64/R/library/lubridate/DESCRIPTION
/usr/lib64/R/library/lubridate/INDEX
/usr/lib64/R/library/lubridate/Meta/Rd.rds
/usr/lib64/R/library/lubridate/Meta/data.rds
/usr/lib64/R/library/lubridate/Meta/features.rds
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
/usr/lib64/R/library/lubridate/cctz.sh
/usr/lib64/R/library/lubridate/data/Rdata.rdb
/usr/lib64/R/library/lubridate/data/Rdata.rds
/usr/lib64/R/library/lubridate/data/Rdata.rdx
/usr/lib64/R/library/lubridate/doc/index.html
/usr/lib64/R/library/lubridate/doc/lubridate.R
/usr/lib64/R/library/lubridate/doc/lubridate.Rmd
/usr/lib64/R/library/lubridate/doc/lubridate.html
/usr/lib64/R/library/lubridate/help/AnIndex
/usr/lib64/R/library/lubridate/help/aliases.rds
/usr/lib64/R/library/lubridate/help/figures/logo.png
/usr/lib64/R/library/lubridate/help/lubridate.rdb
/usr/lib64/R/library/lubridate/help/lubridate.rdx
/usr/lib64/R/library/lubridate/help/paths.rds
/usr/lib64/R/library/lubridate/html/00Index.html
/usr/lib64/R/library/lubridate/html/R.css
/usr/lib64/R/library/lubridate/pkgdown/assets/tidyverse.css
/usr/lib64/R/library/lubridate/pkgdown/assets/tidyverse.css.map
/usr/lib64/R/library/lubridate/tests/testthat.R
/usr/lib64/R/library/lubridate/tests/testthat/helper-output.R
/usr/lib64/R/library/lubridate/tests/testthat/helper-skip.R
/usr/lib64/R/library/lubridate/tests/testthat/output/test-vctrs.txt
/usr/lib64/R/library/lubridate/tests/testthat/setup-options.R
/usr/lib64/R/library/lubridate/tests/testthat/test-Dates.R
/usr/lib64/R/library/lubridate/tests/testthat/test-POSIXt.R
/usr/lib64/R/library/lubridate/tests/testthat/test-accessors.R
/usr/lib64/R/library/lubridate/tests/testthat/test-am-pm.R
/usr/lib64/R/library/lubridate/tests/testthat/test-daylight-savings.R
/usr/lib64/R/library/lubridate/tests/testthat/test-decimal-date.R
/usr/lib64/R/library/lubridate/tests/testthat/test-difftimes.R
/usr/lib64/R/library/lubridate/tests/testthat/test-durations.R
/usr/lib64/R/library/lubridate/tests/testthat/test-format_ISO8601.R
/usr/lib64/R/library/lubridate/tests/testthat/test-guess.R
/usr/lib64/R/library/lubridate/tests/testthat/test-instants.R
/usr/lib64/R/library/lubridate/tests/testthat/test-intervals.R
/usr/lib64/R/library/lubridate/tests/testthat/test-namespace.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-addition.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-compare.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-division.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-integer-division.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-integer-division.txt
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-modulo.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-multiplication.R
/usr/lib64/R/library/lubridate/tests/testthat/test-ops-subtraction.R
/usr/lib64/R/library/lubridate/tests/testthat/test-parsers.R
/usr/lib64/R/library/lubridate/tests/testthat/test-periods.R
/usr/lib64/R/library/lubridate/tests/testthat/test-pretty.R
/usr/lib64/R/library/lubridate/tests/testthat/test-rollback.R
/usr/lib64/R/library/lubridate/tests/testthat/test-round.R
/usr/lib64/R/library/lubridate/tests/testthat/test-settors.R
/usr/lib64/R/library/lubridate/tests/testthat/test-stamp.R
/usr/lib64/R/library/lubridate/tests/testthat/test-time-zones.R
/usr/lib64/R/library/lubridate/tests/testthat/test-timespans.R
/usr/lib64/R/library/lubridate/tests/testthat/test-update.R
/usr/lib64/R/library/lubridate/tests/testthat/test-utilities.R
/usr/lib64/R/library/lubridate/tests/testthat/test-vctrs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lubridate/libs/lubridate.so
/usr/lib64/R/library/lubridate/libs/lubridate.so.avx2
