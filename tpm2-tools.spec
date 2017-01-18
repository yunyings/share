Name: tpm2-tools
Version: 1.1.0 
Release: 2%{?dist}
Summary: A TPM2.0 testing tool build upon TPM2.0-TSS

%global pkg_prefix tpm2.0-tools

License: BSD
URL:     https://github.com/01org/tpm2.0-tools
Source0: https://github.com/01org/tpm2.0-tools/archive/v%{version}.tar.gz#/%{pkg_prefix}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl)
# tpm2-tss-devel-1.0-2 provides sapi/tcti-device/tcti-socket
BuildRequires: pkgconfig(sapi)
BuildRequires: pkgconfig(tcti-device)
BuildRequires: pkgconfig(tcti-socket)

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExclusiveArch: %{ix86} x86_64

# tpm2-tools is heavily depending on TPM2.0-TSS project, matched tss is required
Requires: tpm2-tss = 1.0-2

%description
tpm2-tools is a batch of testing tools for tpm2.0. It is based on tpm2-tss.

%prep
%autosetup -n %{pkg_prefix}-%{version}
./bootstrap

%build
%configure --prefix=/usr --disable-static --disable-silent-rules
%make_build

%install
%make_install

%files
%doc README.md CHANGELOG 
%license LICENSE
%{_sbindir}/tpm2_*

%changelog
* Wed Dec 21 2016 Sun Yunying <yunying.sun@intel.com> - 1.1.0-2
- Remove pkg_version to avoid dupliate use of version
- Remove redundant BuildRequires for autoconf/automake/pkgconfig
- Add comments for BuildRequires of sapi/tcti-device/tcti-socket
- Use ExclusiveArch instead of ExcludeArch
- Requires tpm2-tss version updated to 1.0-2
- Updated release version and changelog

* Fri Dec 2 2016 Sun Yunying <yunying.sun@intel.com> - 1.1.0-1
- Initial version of the package
