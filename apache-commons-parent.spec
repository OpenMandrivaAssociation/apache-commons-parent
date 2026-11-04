%global short_name      commons-parent

Name:             apache-%{short_name}
Version:          107
Release:          1
Summary:          Apache Commons Parent Pom

License:          ASL 2.0
URL:              https://github.com/apache/commons-parent

Source0:          https://github.com/apache/commons-parent/archive/refs/tags/rel/commons-parent-%{version}.tar.gz

BuildArch:        noarch
BuildSystem:	maven
BuildOption:	validate

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n commons-parent-rel-commons-parent-%{version}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
