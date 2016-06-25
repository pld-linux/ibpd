Summary:	InfiniBand Proxy Daemon
Summary(pl.UTF-8):	InfiniBand Proxy Daemon - demon proxy IB
Name:		ibpd
Version:	1.0.1
Release:	1
License:	GPL v2 or BSD
Group:		Daemons
Source0:	https://www.openfabrics.org/downloads/ibpd/%{name}-%{version}.tar.gz
# Source0-md5:	688c17adf3b4f591ca3999043f9f29a2
URL:		http://www.intel.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IB Proxy Daemon (ibpd) is a user-mode process for InfiniBand proxy
devices.

%description -l pl.UTF-8
IB Proxy Daemon (ibpd) to proces przestrzeni użytkownika dla urządzeń
proxy InfiniBand.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_sbindir}/ibpd
