Name:           tpm2-tss
Version:        1.0 
Release:        2%{?dist}
Summary:        TPM2.0 Software Stack

%global  pkg_prefix  TPM2.0-TSS

# The entire source code is under BSD except implementation.h and tpmb.h which
# is under TCGL(Trusted Computing Group License).
License:        BSD and TCGL
URL:            https://github.com/01org/TPM2.0-TSS
Source0:        https://github.com/01org/TPM2.0-TSS/archive/%{version}.tar.gz#/%{pkg_prefix}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf-archive
BuildRequires:  libtool
BuildRequires:  pkgconfig(cmocka)

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExclusiveArch: %{ix86} x86_64

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%prep
%autosetup -n %{pkg_prefix}-%{version} 
./bootstrap


%build
%configure  --disable-static --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name \*.la -delete

%files
%doc README.md CHANGELOG.md 
%license LICENSE
%{_libdir}/libsapi.so.*
%{_libdir}/libtcti-device.so.*
%{_libdir}/libtcti-socket.so.*
%{_sbindir}/resourcemgr


%package        devel
Summary:        Headers and libraries for building apps that use tpm2-tss 
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%files devel
%{_includedir}/sapi/
%{_includedir}/tcti/
%{_libdir}/libsapi.so
%{_libdir}/libtcti-device.so
%{_libdir}/libtcti-socket.so
%{_libdir}/pkgconfig/sapi.pc
%{_libdir}/pkgconfig/tcti-device.pc
%{_libdir}/pkgconfig/tcti-socket.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Mon Dec 12 2016 Sun Yunying <yunying.sun@intel.com> - 1.0-2
- Remove global macro pkg_version to avoid duplicate of version
- Use ExclusiveArch instead of ExcludeArch
- Use less wildcard in %files section to be more specific
- Add trailing slash at end of added directory in %file section
- Remove autoconf/automake/pkgconfig from BuildRequires
- Increase release version to 2

* Fri Dec 2 2016 Sun Yunying <yunying.sun@intel.com> - 1.0-1
- Initial version of the package
