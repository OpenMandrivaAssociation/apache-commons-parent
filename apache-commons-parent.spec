%global base_name       parent
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          20
Release:          5
Summary:          Apache Commons Parent Pom
Group:            Development/Java
License:          ASL 2.0
URL:              http://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-20
# tar caf commons-parent-20.tar.xz commons-parent-20
Source0:          %{short_name}-%{version}.tar.xz

#common-build-plugin not in fedora yet
Patch1:           %{name}-remove-build-plugin.patch
BuildArch:        noarch

BuildRequires:    java-devel >= 0:1.6.0
BuildRequires:    jpackage-utils

Requires:         java >= 0:1.6.0
Requires:         jpackage-utils
Requires:         maven2
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils


%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}
%patch1 -p0

%build
#nothing to do for the pom

%install
rm -rf %{buildroot}

%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*



%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 20-3
+ Revision: 733818
- rebuild
- imported package apache-commons-parent

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix deps

* Tue Oct 18 2011 Oden Eriksson <oeriksson@mandriva.com> 20-2
+ Revision: 705220
- rebuild
- import apache-commons-parent


