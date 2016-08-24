Name:           tpm2-tss
Version:        1.0 
Release:        0.1.beta1%{?dist}
Summary:        TPM2.0 Software Stack

License:        BSD
URL:            https://github.com/01org/TPM2.0-TSS
Source0:        https://github.com/01org/TPM2.0-TSS/archive/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  libcmocka-devel


%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system APIs.
It sits between TPM driver and applications, providing TPM2.0 specified APIs for 
applications to access TPM module through kernel TPM drivers.


%prep
%setup -q


%build
./bootstrap
CONFIG_SITE=$(pwd)/lib/default_config.site ./configure
#%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_includedir}/sapi/*.h
%{_includedir}/tcti/*.h
%{_libdir}/libsapi*
%{_libdir}/libtcti*
%{_libdir}/pkgconfig/sapi*
%{_libdir}/pkgconfig/tcti*
%{_sbindir}/resourcemgr

%doc


%changelog
* Tue Aug 16 2016 Sun Yunying <yunying.sun@intel.com> - 1.0beta1-1
- Initial version of the package
