%global debug_package %{nil}
%global __strip /bin/true

Name: pypy27
Version: 2.5.1
Release: 1%{?dist}
Summary: pypy

License: MIT
URL: https://bitbucket.org/pypy/pypy
Source0: https://bitbucket.org/pypy/pypy/downloads/pypy-2.5.1-src.tar.bz2

Conflicts: portable-pypy27

AutoReqProv: no
BuildRequires: gcc, make, libffi-devel, pkgconfig, zlib-devel, bzip2-devel, ncurses-devel, expat-devel, openssl-devel, sqlite-devel, pypy

%description
pypy 2.7 release

%prep
%setup -q -n pypy-%{version}-src

%build
pypy rpython/bin/rpython --make-jobs=4 -Ojit pypy/goal/targetpypystandalone.py


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/pypy27/bin

cp -p pypy-c $RPM_BUILD_ROOT/opt/pypy27/bin/pypy

cp -rp include $RPM_BUILD_ROOT/opt/pypy27/.
cp -rp lib_pypy $RPM_BUILD_ROOT/opt/pypy27/.
cp -rp lib-python $RPM_BUILD_ROOT/opt/pypy27/.
cp -rp site-packages $RPM_BUILD_ROOT/opt/pypy27/.

ln -s pypy $RPM_BUILD_ROOT/opt/pypy27/bin/python
ln -s pypy $RPM_BUILD_ROOT/opt/pypy27/bin/python2.7

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/pypy27
