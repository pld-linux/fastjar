
Summary:	Jar file creation utility
Summary(pl):	Narzêdzie do tworzenia plików jar
Name:		fastjar
Version:	0.90
Release:	1
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	%{name}-%{version}.tgz
Patch0:	fastjar-DESTDIR_and_install.patch
URL:		http://fastjar.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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

gzip -9nf README LICENSE INSTALL CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,LICENSE,INSTALL,CHANGES}.gz
%attr(755, root, root) %{_bindir}/jar
%attr(755, root, root) %{_bindir}/fastjar
