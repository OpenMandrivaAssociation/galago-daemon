%define name galago-daemon
%define version 0.5.1
%define release %mkrel 4

Summary: Galago desktop presence daemon
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.galago-project.org/files/releases/source/galago-daemon/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
Url: http://www.galago-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgalago-devel >= 0.5.2

%description
This are the daemon of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%config(noreplace) %_sysconfdir/dbus-1/system.d/galago-daemon.conf
%_libexecdir/galago-daemon
%_datadir/dbus-1/services/org.freedesktop.Galago.service




%changelog
* Wed Jul 27 2011 Götz Waschk <waschk@mandriva.org> 0.5.1-4mdv2012.0
+ Revision: 691829
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-3mdv2011.0
+ Revision: 245618
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5.1-1mdv2008.1
+ Revision: 140733
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2007.0
+ Revision: 104441
- new version
- bump deps
- Import galago-daemon

* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-4mdv2007.1
- Rebuild

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.0-3mdv2007.0
- Rebuild with latest dbus

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdk
- Rebuild

* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- bump deps
- New release 0.5.0
- use mkrel

* Fri Jan 27 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3.4-3mdk
- rebuild for new dbus

* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdk
- rebuild for new dbus

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdk
- update file list
- bump deps
- new URL
- new version

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdk
- initial package

