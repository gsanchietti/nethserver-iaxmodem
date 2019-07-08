Summary: NethServer module to configure IAX modems
Name: nethserver-iaxmodem
Version: 1.2.5
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>
BuildArch: noarch
Requires: iaxmodem
Requires: nethserver-hylafax
BuildRequires: nethserver-devtools

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
mkdir -p root/var/log/iaxmodem/old

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
install -v -m 644 -D %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/%{name}.json
install -v -m 644 -D ui/public/logo.png %{buildroot}/usr/share/cockpit/%{name}/logo.png
install -v -m 644 -D ui/public/manifest.json %{buildroot}/usr/share/cockpit/%{name}/manifest.json
install -v -m 755 -D api/read %{buildroot}/usr/libexec/nethserver/api/%{name}/read
%{genfilelist} %{buildroot} \
--dir /var/log/iaxmodem/old 'attr(0640,root,root)' > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Thu Aug 09 2018 Davide Principi <davide.principi@nethesis.it> - 1.2.5-1
- Enhancement: (un)mask password fields - NethServer/dev#5554

* Mon Nov 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.4-1
- iaxmodem: logrotate failure - NethServer/dev#5387

* Fri Sep 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.3-1
- IAX modems: faxgetty not started after reboot - Bug NethServer/dev#5344

* Thu Jul 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- IAXModem: bad logrotate configuration - Bug NethServer/dev#5317

* Wed May 10 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Upgrade from NS 6 via backup and restore - NethServer/dev#5234
- Add logrotate configuration

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.0-1
- First NS7 release

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Thu Mar 05 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- IAXmodem server hostname (not only ip) - Enhancement #3002 [NethServer]
- IAXmodem: configure mode for each modem - Enhancement #2761 [NethServer]
- IAXmodem: configure email address for each modem - Feature #2760 [NethServer]

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Missing Italian translation - Bug #2706 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
• Rebuild for automatic package handling. #1870

* Tue Mar 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release #1784

