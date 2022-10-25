#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pywinrm
Version  : 0.4.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/7c/ba/78329e124138f8edf40a41b4252baf20cafdbea92ea45d50ec712124e99b/pywinrm-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/ba/78329e124138f8edf40a41b4252baf20cafdbea92ea45d50ec712124e99b/pywinrm-0.4.3.tar.gz
Summary  : Python library for Windows Remote Management
Group    : Development/Tools
License  : MIT
Requires: pypi-pywinrm-python = %{version}-%{release}
Requires: pypi-pywinrm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_ntlm)
BuildRequires : pypi(six)
BuildRequires : pypi(xmltodict)

%description
# pywinrm
pywinrm is a Python client for the Windows Remote Management (WinRM) service.
It allows you to invoke commands on target Windows machines from any machine
that can run Python.

%package python
Summary: python components for the pypi-pywinrm package.
Group: Default
Requires: pypi-pywinrm-python3 = %{version}-%{release}

%description python
python components for the pypi-pywinrm package.


%package python3
Summary: python3 components for the pypi-pywinrm package.
Group: Default
Requires: python3-core
Provides: pypi(pywinrm)
Requires: pypi(requests)
Requires: pypi(requests_ntlm)
Requires: pypi(six)
Requires: pypi(xmltodict)

%description python3
python3 components for the pypi-pywinrm package.


%prep
%setup -q -n pywinrm-0.4.3
cd %{_builddir}/pywinrm-0.4.3
pushd ..
cp -a pywinrm-0.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657662004
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
