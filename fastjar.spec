Summary:	Jar file creation utility
Summary(pl):	Narz�dzie do tworzenia plik�w jar
Name:		fastjar
Version:	0.90
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/fastjar/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR_and_install.patch
URL:		http://fastjar.sourceforge.net
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FastJar is an attempt at creating a feature-for-feature copy of Sun's
JDK's 'jar' command. Sun's jar (or Blackdown's for that matter) is
written entirely in Java which makes it dog slow. Since FastJar is
written in C, it can create the same .jar file as Sun's tool in a
fraction of the time. On my system, Sun's jar takes 50 seconds to
create a 10MB jar file, while FastJar only takes a little over a
second.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf fastjar $RPM_BUILD_ROOT%{_bindir}/jar

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
