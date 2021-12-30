#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-logcondens
Version  : 2.1.6
Release  : 20
URL      : https://cran.r-project.org/src/contrib/logcondens_2.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/logcondens_2.1.6.tar.gz
Summary  : Estimate a Log-Concave Probability Density from Iid Observations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ks
BuildRequires : R-ks
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n logcondens
cd %{_builddir}/logcondens

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634075426

%install
export SOURCE_DATE_EPOCH=1634075426
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logcondens
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logcondens
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library logcondens
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc logcondens || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/logcondens/CITATION
/usr/lib64/R/library/logcondens/DESCRIPTION
/usr/lib64/R/library/logcondens/INDEX
/usr/lib64/R/library/logcondens/Meta/Rd.rds
/usr/lib64/R/library/logcondens/Meta/data.rds
/usr/lib64/R/library/logcondens/Meta/features.rds
/usr/lib64/R/library/logcondens/Meta/hsearch.rds
/usr/lib64/R/library/logcondens/Meta/links.rds
/usr/lib64/R/library/logcondens/Meta/nsInfo.rds
/usr/lib64/R/library/logcondens/Meta/package.rds
/usr/lib64/R/library/logcondens/Meta/vignette.rds
/usr/lib64/R/library/logcondens/NAMESPACE
/usr/lib64/R/library/logcondens/NEWS
/usr/lib64/R/library/logcondens/R/logcondens
/usr/lib64/R/library/logcondens/R/logcondens.rdb
/usr/lib64/R/library/logcondens/R/logcondens.rdx
/usr/lib64/R/library/logcondens/data/brightstar.rda
/usr/lib64/R/library/logcondens/data/pancreas.rda
/usr/lib64/R/library/logcondens/data/reliability.rda
/usr/lib64/R/library/logcondens/doc/index.html
/usr/lib64/R/library/logcondens/doc/logcondens.R
/usr/lib64/R/library/logcondens/doc/logcondens.Rnw
/usr/lib64/R/library/logcondens/doc/logcondens.pdf
/usr/lib64/R/library/logcondens/help/AnIndex
/usr/lib64/R/library/logcondens/help/aliases.rds
/usr/lib64/R/library/logcondens/help/logcondens.rdb
/usr/lib64/R/library/logcondens/help/logcondens.rdx
/usr/lib64/R/library/logcondens/help/paths.rds
/usr/lib64/R/library/logcondens/html/00Index.html
/usr/lib64/R/library/logcondens/html/R.css
