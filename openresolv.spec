Summary:	DNS management framework
Name:		openresolv
Version:	3.6.2
Release:	1
License:	BSD-like
Group:		Base
Source0:	http://roy.marples.name/downloads/openresolv/%{name}-%{version}.tar.bz2
# Source0-md5:	8416f07cc65b535578dc70e86bbed54f
URL:		http://roy.marples.name/projects/openresolv
BuildRequires:	sed
Requires:	systemd
Provides:	resolvconf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/resolvconf

%description
resolvconf itself is just a script that stores, removes and lists
a full resolv.conf generated for the interface. It then calls all
the helper scripts it knows about so it can configure the real
/etc/resolv.conf and optionally any local nameservers other can libc.

%prep
%setup -q

%{__sed} -n '2,25{s:^# \?::;p}' resolvconf.in > LICENSE

%build
%configure \
	--rundir=/run
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/resolvconf.conf
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/dnsmasq
%attr(755,root,root) %{_libexecdir}/libc
%attr(755,root,root) %{_libexecdir}/named
%attr(755,root,root) %{_libexecdir}/pdnsd
%attr(755,root,root) %{_libexecdir}/unbound
%attr(755,root,root) %{_sbindir}/resolvconf
%{_mandir}/man5/resolvconf.conf.5*
%{_mandir}/man8/resolvconf.8*

