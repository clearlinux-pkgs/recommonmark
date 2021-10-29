#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : recommonmark
Version  : 33b5c2a4ec50d18d3f659aa119d3bd11452327da
Release  : 25
URL      : https://github.com/rtfd/recommonmark/archive/33b5c2a4ec50d18d3f659aa119d3bd11452327da.tar.gz
Source0  : https://github.com/rtfd/recommonmark/archive/33b5c2a4ec50d18d3f659aa119d3bd11452327da.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: recommonmark-bin = %{version}-%{release}
Requires: recommonmark-license = %{version}-%{release}
Requires: recommonmark-python = %{version}-%{release}
Requires: recommonmark-python3 = %{version}-%{release}
Requires: commonmark
Requires: docutils
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : commonmark
BuildRequires : docutils
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# recommonmark
A `docutils`-compatibility bridge to [CommonMark][cm].
This allows you to write CommonMark inside of Docutils & Sphinx projects.

%package bin
Summary: bin components for the recommonmark package.
Group: Binaries
Requires: recommonmark-license = %{version}-%{release}

%description bin
bin components for the recommonmark package.


%package license
Summary: license components for the recommonmark package.
Group: Default

%description license
license components for the recommonmark package.


%package python
Summary: python components for the recommonmark package.
Group: Default
Requires: recommonmark-python3 = %{version}-%{release}

%description python
python components for the recommonmark package.


%package python3
Summary: python3 components for the recommonmark package.
Group: Default
Requires: python3-core

%description python3
python3 components for the recommonmark package.


%prep
%setup -q -n recommonmark-33b5c2a4ec50d18d3f659aa119d3bd11452327da
cd %{_builddir}/recommonmark-33b5c2a4ec50d18d3f659aa119d3bd11452327da

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583218475
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/recommonmark
cp %{_builddir}/recommonmark-33b5c2a4ec50d18d3f659aa119d3bd11452327da/license.md %{buildroot}/usr/share/package-licenses/recommonmark/227326135d61f3b0a7771d7eccc738e48ca056d4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cm2html
/usr/bin/cm2latex
/usr/bin/cm2man
/usr/bin/cm2pseudoxml
/usr/bin/cm2xetex
/usr/bin/cm2xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/recommonmark/227326135d61f3b0a7771d7eccc738e48ca056d4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
