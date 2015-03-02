Summary: NethServer module to configure IAX modems
Name: nethserver-iaxmodem
Version: 1.0.3
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>
BuildArch: noarch
Requires: iaxmodem
Requires: nethserver-hylafax
BuildRequires: nethserver-devtools
AutoReq: no

%description
NethServer module to configure IAX modems


%prep
%setup

%pre

%post

%preun

%postun

%build
%{makedocs}
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
   $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(0644,root,root)

%changelog
* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Missing Italian translation - Bug #2706 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
• Rebuild for automatic package handling. #1870

* Tue Mar 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release #1784

