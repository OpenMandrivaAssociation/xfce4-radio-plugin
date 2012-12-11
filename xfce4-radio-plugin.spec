%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Radio plugin for the Xfce panel
Name:		xfce4-radio-plugin
Version:	0.5.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-radio-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-radio-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-radio-plugin-0.5.1-gold.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfcegui4-devel
Obsoletes:	xfce-radio-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is an Xfce panel plugin which allows you to control your V4l radio device.
You can turn your radio on/off, tune it to some frequency and manage station
presets.

%prep
%setup -q
%patch1 -p0
autoconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/xfce4/panel-plugins/*.desktop 
%{_libdir}/xfce4/panel-plugins/*


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.5.1-3mdv2012.0
+ Revision: 791560
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.5.1-2
+ Revision: 790093
- Rebuild for xfce 4.10

* Tue Jun 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1
+ Revision: 687928
- update to new version 0.5.1

* Tue Jun 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-2
+ Revision: 687921
- rebuild

* Sun May 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-1
+ Revision: 677456
- update to new version 0.5.0

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.5-1
+ Revision: 644046
- update to new version 0.4.5

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-1mdv2011.0
+ Revision: 594850
- add missing buildrequires on libxfcegui4-devel
- update to new version 0.4.4
- add support for new urlsfor Source0
- dropl old conditionals in spec file for mdv releases older than 200900

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-3mdv2010.1
+ Revision: 543435
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 446108
- rebuild

* Thu Mar 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2009.1
+ Revision: 358205
- update to new version 0.4.2

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2009.1
+ Revision: 349476
- rebuild for xfce-4.6.0

* Mon Jan 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-1mdv2009.1
+ Revision: 331468
- update to new version 0.4.1

* Wed Dec 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 309815
- update to new version 0.4.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-2mdv2009.1
+ Revision: 295006
- rebuild for new Xfce4.6 beta1
- update to new version 0.3.1
- execute scriplets only for mdv older than 2009

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 219214
- New version 0.3.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-2mdv2008.1
+ Revision: 110130
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING, NEWS and INSTALL files
- add ChangeLog ot the docs
- use upstream name

* Sat Jun 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 40285
- new version

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-4mdv2008.0
+ Revision: 33239
- drop __libtoolize
- spec file clean
- add macros to %%post and %%postun

