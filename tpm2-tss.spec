Name:           tpm2-tss
Version:        1.0 
Release:        0.1.beta1%{?dist}
Summary:        TPM2.0 Software Stack

License:        BSD
URL:            https://github.com/01org/TPM2.0-TSS
Source0:        https://github.com/01org/TPM2.0-TSS/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.


%prep
%setup -q
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
* Mon Sep 5 2016 Sun Yunying <yunying.sun@intel.com> - 1.0beta1-1
- Initial version of the package
