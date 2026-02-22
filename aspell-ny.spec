Summary:	Chichewa dictionary for aspell
Summary(pl.UTF-8):	Słownik niandża dla aspella
Name:		aspell-ny
Version:	0.01
%define	subv	0
Release:	3
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ny/aspell5-ny-%{version}-%{subv}.tar.bz2
# Source0-md5:	856906a424fcbc50cc925d692d294215
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chichewa dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik niandża (lista słów) dla aspella.

%prep
%setup -q -n aspell5-ny-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/Crawler.txt
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
