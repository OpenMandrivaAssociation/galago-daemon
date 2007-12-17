%define name galago-daemon
%define version 0.5.1
%define release %mkrel 1

Summary: Galago desktop presence daemon
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.galago-project.org/files/releases/source/galago-daemon/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
Url: http://www.galago-project.org/
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


