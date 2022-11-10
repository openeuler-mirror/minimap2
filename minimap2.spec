Name:    minimap2
Version: 2.17
Release: 3
Summary: A versatile pairwise aligner for genomic and spliced nucleotide sequences
License: MIT
URL:     https://lh3.github.io/minimap2/
Source0: https://github.com/lh3/minimap2/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:  0001-fix-man-command.patch

BuildRequires:  gcc make zlib-devel

%description
Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.


%global ENV %{nil}

%ifarch aarch64
%global ENV arm_neon=true aarch64=true
%endif

%prep
%setup  -q -n %{name}-%{version}/
%patch0 -p 1

%build
%{ENV} make extra

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 minimap2 %{buildroot}%{_bindir}/minimap2
install -m 755 minimap2-lite %{buildroot}%{_bindir}/minimap2-lite
install -m 755 sdust %{buildroot}%{_bindir}/sdust
mkdir -p %{buildroot}%{_mandir}/man1/
cp ./minimap2.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE.txt
%doc README.md cookbook.md
%{_bindir}/*
%{_mandir}/*

%changelog
* Thu Nov 10 2022 xu_ping <xuping33@h-partners.com> - 2.17-3
- fix source url

* Sat Aug 28 2021 yangzhao <yangzhao1@kylinos.cn> - 2.17-2
- fix man command

* Thu Mar 18 2021 yangzhao <yangzhao1@kylinos.cn> - 2.17-1
- Package init
