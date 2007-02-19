Summary:	Jar file creation utility
Summary(pl.UTF-8):	Narzędzie do tworzenia plików jar
Name:		fastjar
Version:	0.93
Release:	7
License:	GPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/fastjar/%{name}-%{version}.tgz
# Source0-md5:	a8159d2042bce9998020f197fee39ef1
Patch0:		%{name}-gcc.patch
URL:		http://fastjar.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
Provides:	jar
Provides:	java-shared
Obsoletes:	java-shared
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FastJar is an attempt at creating a feature-for-feature copy of Sun's
JDK's 'jar' command. Sun's jar (or Blackdown's for that matter) is
written entirely in Java which makes it dog slow. Since FastJar is
written in C, it can create the same .jar file as Sun's tool in a
fraction of the time. On my system, Sun's jar takes 50 seconds to
create a 10MB jar file, while FastJar only takes a little over a
second.

%description -l pl.UTF-8
FastJar to próba stworzenia dokładnej pod względem możliwości kopii
polecenia jar z Sun JDK. jar Suna (lub Blackdowna) jest napisany
całkowicie w Javie, co powoduje, że jest bardzo wolny. Ponieważ
FastJar jest napisany w C, może tworzyć te same pliki .jar co
narzędzie Suna kilka razy szybciej. Na systemie autora jar Suna
potrzebuje 50 sekund na stworzenie 10MB pliku jar, natomiast fastjar
robi to w nieco ponad sekundę.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf fastjar $RPM_BUILD_ROOT%{_bindir}/jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
