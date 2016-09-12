Name:           tpm2-tools
Version:        1.1 
Release:        0.1.beta1%{?dist}
Summary:        a TPM2.0 testing tool build upon TPM2.0-TSS

%global pkg_version	1.1-beta_1
%global pkg_prefix	tpm2.0-tools

License:        BSD
URL:            https://github.com/01org/tpm2.0-tools
Source0:        https://github.com/01org/tpm2.0-tools/archive/v%{pkg_version}.tar.gz
# If downloaded tarball name is different with the name specified in Source0
# url, run script below to rename it, otherwise rpm fails to find the package.
Source1:	rename-tarball.sh

BuildRequires:	gcc 
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(sapi)
BuildRequires:	pkgconfig(tcti-device)
BuildRequires:	pkgconfig(tcti-socket)

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExcludeArch:	%arm %sparc %alpha %power64

Requires:	tpm2-tss = 1.0-0.1.beta1

%description
tpm2-tools is a batch of testing tools for tpm2.0. It is based on tpm2-tss.

%prep
%autosetup -n %{pkg_prefix}-%{pkg_version}
./bootstrap

%build
%configure --prefix=/usr --disable-static --disable-silent-rules
%make_build


%install
%make_install


%files
%doc README.md ChangeLog
%license LICENSE
%{_sbindir}/tpm2_*


%changelog
* Mon Sep 12 2016 Sun Yunying <yunying.sun@intel.com> - 1.1beta1-1
- Initial version of the package
