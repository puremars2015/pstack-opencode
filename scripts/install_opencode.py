"""Install all pstack skills without overwriting existing skill names."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--destination", type=Path,
                    default=Path.home() / ".config/opencode/skills")
args = parser.parse_args()
source = Path(__file__).resolve().parents[1] / "skills"
skills = sorted(p for p in source.iterdir() if (p / "SKILL.md").is_file())
if len(skills) != 55:
    parser.error(f"Expected 55 source skills, found {len(skills)}")
destination = args.destination.expanduser().resolve()
conflicts = [p.name for p in skills if (destination / p.name).exists()]
if conflicts:
    parser.error("Refusing to overwrite existing skills: " + ", ".join(conflicts))
destination.mkdir(parents=True, exist_ok=True)
for skill in skills:
    shutil.copytree(skill, destination / skill.name)
print(f"Installed {len(skills)} skills to {destination}")
print("Quit and restart OpenCode to load the new skills.")
