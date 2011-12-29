# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-farsi
Version:	20111103
Release:	1
Summary:	(No) Persian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-farsi.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Prevent hyphenation in Persian.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-farsi
%_texmf_language_def_d/hyphen-farsi
%_texmf_language_lua_d/hyphen-farsi

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-farsi <<EOF
%% from hyphen-farsi:
farsi zerohyph.tex
=persian
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-farsi <<EOF
%% from hyphen-farsi:
\addlanguage{farsi}{zerohyph.tex}{}{2}{3}
\addlanguage{persian}{zerohyph.tex}{}{2}{3}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-farsi <<EOF
-- from hyphen-farsi:
	['farsi'] = {
		loader = 'zerohyph.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'persian' },
		patterns = '',
	},
EOF
