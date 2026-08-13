%global tl_name hyphen-farsi
%global tl_revision 74115

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	(No) Persian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-farsi
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-farsi.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Prevent hyphenation in Persian.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-farsi:
farsi hyph-fa.tex
=persian
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-farsi:
\addlanguage{farsi}{hyph-fa.tex}{}{0}{0}
\addlanguage{persian}{hyph-fa.tex}{}{0}{0}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-farsi:
['farsi'] = {
	loader = 'hyph-fa.tex',
	lefthyphenmin = 0,
	righthyphenmin = 0,
	synonyms = { 'persian' },
},
TL_HYPHEN_EOF
