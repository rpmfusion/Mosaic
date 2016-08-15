Name:           Mosaic
Version:        2.7
Release:        0.5.b5%{?dist}
Summary:        Web Browser

Group:          Applications/Internet
# This is different from "NCSA" license
License:        Mosaic
URL:            http://www.ncsa.uiuc.edu/Projects/mosaic.html
Source0:        ftp://ftp.ncsa.uiuc.edu/Mosaic/Unix/source/Mosaic-src-2.7b5.tar.gz
Source1:        Mosaic.desktop
Patch0:         Mosaic-2.7b5-compile.patch
Patch1:         Mosaic-2.7b5-modern.patch
Patch2:         Mosaic-2.7b5-crash.patch
Patch3:         Mosaic-2.7b5-script.patch
Patch4:         Mosaic-2.7b5-hash_url.patch
Patch5:         Mosaic-2.7b5-redirect.patch
Patch6:         Mosaic-2.7b5-gcc-compile.patch

BuildRequires:  openmotif-devel
BuildRequires:  libjpeg-devel libpng-devel
BuildRequires:  autoconf ImageMagick desktop-file-utils
BuildRequires:  libXmu-devel
Requires:  xv

%description
Mosaic is a web browser and client for protocols such as FTP, Usenet, and
Gopher. Its has a clean, easily understood user interface and is capable of
displaying images inline with text.


%prep
%setup -q -n %{name}-src
%patch0 -p1 -b .compile
%patch1 -p1 -b .modern
%patch2 -p1 -b .crash
%patch3 -p1 -b .script
%patch4 -p1 -b .hash_url
%patch5 -p1 -b .redirect
%patch6 -p1 -b .gcc

%build
autoconf
%configure --with-png --with-jpeg
make %{?_smp_mflags}

# Convert the icon into Icon Theme Specification compilant one
convert src/pixmaps/s_icon.1.xpm Mosaic.png

# Fix permissions for debuginfo package
chmod 0644 src/bitmaps/busy_9.xbm libnut/url-utils.c


%install
rm -rf $RPM_BUILD_ROOT

# Directory structure
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_bindir}

# Executable
install src/Mosaic $RPM_BUILD_ROOT%{_bindir}

# Icon
install -pm 0644 Mosaic.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Menu entry
desktop-file-install %{SOURCE1} \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications


%files
%doc README.resources.html
%doc CHANGES FEATURES INSTALL README
%license COPYRIGHT
%{_bindir}/Mosaic
%{_datadir}/pixmaps/Mosaic.png
%{_datadir}/applications/Mosaic.desktop


%changelog
* Mon Aug 15 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.7-0.5.b5
- Patch for libpng changes
- Patch for gcc changes
- Add Requires xv

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.7-0.4.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 23 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.7-0.3.b5
- Grammar fixes
- Fix buildrequires
- Correct license tag
- Strip executable bits off source files
- Don't use vendor tag for desktop menu entry

* Sun Mar 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.7-0.2.b5
- Fix build for Fedora 11

* Tue Nov 25 2008 Lubomir Rintel <lkundrak@v3.sk> - 2.7-0.1.b5
- Initial packaging
