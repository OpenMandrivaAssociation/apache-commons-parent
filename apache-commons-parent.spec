%{?_javapackages_macros:%_javapackages_macros}
%global short_name      commons-parent

Name:             apache-%{short_name}
Version:          32
Release:          2.1%{?dist}
Summary:          Apache Commons Parent Pom

License:          ASL 2.0
URL:              https://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-32
# tar caf commons-parent-32.tar.xz commons-parent-32
Source0:          %{short_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    java-devel
BuildRequires:    mvn(org.apache:apache)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.rat:apache-rat-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Requires:         mvn(org.codehaus.mojo:buildnumber-maven-plugin)

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}

# Plugin is not in fedora
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%changelog
* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-2
- Remove use of maven-scm-publish-plugin plugin

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-1
- Updated to latest upstream, rhbz #904731

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 26-7
- Use pom macros instead of patching
- Update spec for latest guidelines rhbz #991975

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-5
- Add buildnumber-maven-plugin to R/BR

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-4
- Fix Requires and BuildRequires

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 26-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Oct 19 2012 Chris Spike <spike@fedoraproject.org> 22-4
- Updated to 26

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Alexander Kurtakov <akurtako@redhat.com> 22-2
- Add missing BR/R on buildbumber-maven-plugin.

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 22-1
- Update to latest upstream.

* Fri Apr 15 2011 Chris Spike <spike@fedoraproject.org> 20-1
- Updated to 20
- Fixed Rs for maven 3

* Sat Nov 6 2010 Chris Spike <spike@fedoraproject.org> 15-2
- Added patch to remove commons-build-plugin from pom file

* Wed Oct 20 2010 Chris Spike <spike@fedoraproject.org> 15-1
- Initial version of the package
