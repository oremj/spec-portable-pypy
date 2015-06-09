
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global debug_package %{nil}
%global __strip /bin/true

Name: portable-pypy27
Version: 2.6
Release: 1%{?dist}
Summary: https://github.com/squeaky-pl/portable-pypy

License: MIT
URL: https://github.com/squeaky-pl/portable-pypy
Source0: https://bitbucket.org/squeaky/portable-pypy/downloads/pypy-%{version}-linux_x86_64-portable.tar.bz2

AutoReqProv: no

%description
portable pypy 2.7 release


%prep
%setup -q -n pypy-%{version}-linux_x86_64-portable

%build
ln -s pypy bin/python
ln -s pypy bin/python2.7

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/pypy27

cp -r . $RPM_BUILD_ROOT/opt/pypy27

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/pypy27
