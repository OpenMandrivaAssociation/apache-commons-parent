%global short_name      commons-parent

Name:             apache-%{short_name}
Version:          107
Release:          2
Summary:          Apache Commons Parent Pom
Group:            Development/Java

License:          ASL 2.0
URL:              https://github.com/apache/commons-parent

Source0:          https://github.com/apache/commons-parent/archive/refs/tags/rel/commons-parent-%{version}.tar.gz

BuildArch:        noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	python
BuildSystem:	maven
BuildOption:	validate

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n commons-parent-rel-commons-parent-%{version}
# JDK 9+ activates add-module-info. moditect is not packaged, and every
# child fails while resolving the plugin. The jars stay automatic modules.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text, n = re.subn(
	r"\s*<plugin>\s*<groupId>org\.moditect</groupId>\s*<artifactId>moditect-maven-plugin</artifactId>.*?</plugin>",
	"",
	text,
	count=1,
	flags=re.S,
)
if n != 1:
	raise SystemExit(f"expected to remove moditect-maven-plugin, removed {n}")
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
