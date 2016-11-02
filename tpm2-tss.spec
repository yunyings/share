Name:           tpm2-tss
Version:        1.0 
Release:        0.1.beta1%{?dist}
Summary:        TPM2.0 Software Stack

%global	pkg_version	1.0-beta_1
%global	pkg_prefix	TPM2.0-TSS

# The entire source code is under BSD except implementation.h and tpmb.h which
# is under TCGL(Trusted Computing Group License).
License:        BSD and TCGL
URL:            https://github.com/01org/TPM2.0-TSS
Source0:        https://github.com/01org/TPM2.0-TSS/archive/%{pkg_version}.tar.gz#/%{pkg_prefix}-%{pkg_version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExcludeArch:	%arm %sparc %alpha %power64 aarch64

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%prep
%autosetup -n %{pkg_prefix}-%{pkg_version} 
./bootstrap


%build
%configure  --disable-static --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name \*.la -delete

%files
%doc README.md ChangeLog
%license LICENSE
%{_libdir}/*.so.*
%{_sbindir}/resourcemgr


%package        devel
Summary:        Headers and libraries for building apps that use tpm2-tss 
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%files devel
%{_includedir}/sapi
%{_includedir}/tcti
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Nov 2 2016 Sun Yunying <yunying.sun@intel.com> - 1.0-0.1.beta1
- Initial version of the package
