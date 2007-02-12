#
# Conditional build:
%bcond_without	x	# don't build X11 version
#
Summary:	The Unified Extended Dialect of Icon 
Summary(pl.UTF-8):	Rozbudowana wersja języka Icon 
Name:		unicon
Version:	11
%define _snap 20030210
Release:	0.%{_snap}.1
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	http://unicon.sourceforge.net/dist/uni.zip
# Source0-md5:	e089da57b8c796dcf1fa3441f2e35bfe
Patch0:		%{name}-makefile.patch
URL:		http://unicon.sourceforge.net/
BuildRequires:	unzip
Obsoletes:	icon
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicon is a very high level, goal-directed, object-oriented, general purpose 
applications language.

%description -l pl.UTF-8
Unicon jest objektowym językiem programowania ogólnego zastosowania bardzo 
wysokiego poziomu.

%prep
%setup -q -c -T 
cp %{SOURCE0} ./
unzip uni.zip
%patch0 -p1

%build
%ifarch %{ix86}
%{__make} %{?with_x:X-}Configure name=intel_linux
%endif
%ifarch alpha
%{__make} %{?with_x:X-}Configure name=alpha_linux
%endif

%{__make} Unicon CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/unicon/{bin,ipl,uni}}
%{__make} Install dest=$RPM_BUILD_ROOT%{_libdir}/unicon/

for f in icont iconx ivib patchstr ui unicon 
do
	mv $RPM_BUILD_ROOT%{_libdir}/unicon/bin/$f $RPM_BUILD_ROOT%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/unicon
%dir %{_libdir}/unicon/bin
%{_libdir}/unicon/bin/lib*
%{_libdir}/unicon/ipl
%{_libdir}/unicon/uni
