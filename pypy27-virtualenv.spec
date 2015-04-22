%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global debug_package %{nil}
%global __strip /bin/true

Name: pypy27-virtualenv
Version: 12.1.1
Release: 1%{?dist}
Summary: virtualenv

License: MIT
URL: https://pypi.python.org/pypi/virtualenv
Source0: https://pypi.python.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz

BuildRequires: pypy27
Requires: pypy27

%description
virtualenv

%prep
%setup -q -n virtualenv-%{version}

%build

%install
rm -rf %{buildroot}
/opt/pypy27/bin/pypy setup.py install --root="%{buildroot}" --record=FILES
mkdir -p $RPM_BUILD_ROOT/opt/pypy27/bin

%clean
rm -rf %{buildroot}


%files -f FILES
