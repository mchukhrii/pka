Name: libpka
Version: 2.0
Release: 1%{?dist}
Summary: Nvidia BlueField Public Key Acceleration (PKA) Package

License: BSD
Url: https://nvidia.com
Source: %{name}-%{version}.tgz

BuildRequires: binutils
BuildRequires: openssl-devel
BuildRequires: gcc

%description
The PKA software package consists of (1) an API specification, which
is the application writer's view (this is also intended to provide
complete interfaces to use with OpenSSL), (2) an API implementation
for BlueField, (3) validation test suite, an independant set of
test routines that run against the API implementation and verifies
that it correctly implements all of the defined APIs at a functional
level, and (4) a dynamic OpenSSL engine component to support RSA,
DSA, DH, ECDH and ECDSA operations and interfaces with the BlueField
PKA hardware.

%prep
%setup

%build
%configure
%make_build

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/engines-1.1
cp $RPM_BUILD_ROOT%{_libdir}/libbfengine.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/engines-1.1/

%preun
rm -f %{_libdir}/engines-1.1/pka.so

%post
ln -s %{_libdir}/engines-1.1/libbfengine.so.*.*.* %{_libdir}/engines-1.1/pka.so

%files
%defattr(-, root, root)
%{_prefix}/share/*
%{_libdir}/libPKA*
%{_libdir}/libbfengine*
%{_bindir}/*
%{_libdir}/engines-1.1/libbfengine*
%{_libdir}/engines-1.1/pka.so

%doc COPYING
