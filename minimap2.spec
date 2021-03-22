Name:    minimap2
Version: 2.17
Release: 1
Summary: A versatile pairwise aligner for genomic and spliced nucleotide sequences
License: MIT
URL:	 https://lh3.github.io/minimap2/
Source0: https://github.com/lh3/minimap2/archive/refs/tags/v2.17.tar.bz2

BuildRequires: 	gcc make zlib-devel

%description
Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.


%global ENV %{nil}

%ifarch aarch64
%global ENV arm_neon=true aarch64=true
%endif

%prep
%setup -q -n %{name}-%{version}/

%build
%{ENV} make extra

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 minimap2 %{buildroot}%{_bindir}/minimap2
install -m 755 minimap2-lite %{buildroot}%{_bindir}/minimap2-lite
install -m 755 sdust %{buildroot}%{_bindir}/sdust

%files
%license LICENSE.txt
%doc README.md cookbook.md
%{_bindir}/*


%changelog
* Thu Mar 18 2021 yangzhao <yangzhao1@kylinos.cn> - 2.17-1
- Package init

