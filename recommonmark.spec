#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : recommonmark
Version  : 0.4.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/3d/95/aa1085573adf3dc7b164ae8569d57b1af5e98922e40345bb7efffed5ad2e/recommonmark-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/95/aa1085573adf3dc7b164ae8569d57b1af5e98922e40345bb7efffed5ad2e/recommonmark-0.4.0.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : MIT
Requires: recommonmark-bin
Requires: recommonmark-python3
Requires: recommonmark-python
Requires: commonmark
Requires: docutils
BuildRequires : buildreq-distutils3
BuildRequires : commonmark
BuildRequires : docutils

%description
No detailed description available

%package bin
Summary: bin components for the recommonmark package.
Group: Binaries

%description bin
bin components for the recommonmark package.


%package python
Summary: python components for the recommonmark package.
Group: Default
Requires: recommonmark-python3

%description python
python components for the recommonmark package.


%package python3
Summary: python3 components for the recommonmark package.
Group: Default
Requires: python3-core

%description python3
python3 components for the recommonmark package.


%prep
%setup -q -n recommonmark-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536660534
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
