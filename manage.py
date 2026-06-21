#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Strawberry Nutrient System - Project Manager
"""

import os
import sys
import subprocess
import shutil
import platform
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.absolute()
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"


class ProjectManager:
    def __init__(self):
        self.processes = []
        self.is_windows = platform.system() == 'Windows'

    def clear_screen(self):
        os.system('cls' if self.is_windows else 'clear')

    def print_header(self):
        self.clear_screen()
        print("=" * 60)
        print("  \ud83c\udf53 Strawberry Nutrient System - Manager")
        print("=" * 60)
        print(f"  \ud83d\udcc1 {PROJECT_ROOT}")
        print(f"  \ud83d\udcc5 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  \ud83d\udcbb {platform.system()} ({platform.machine()})")
        print("=" * 60)

    def print_menu(self):
        print("\n\ud83d\udccb Menu:")
        print("  \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500")
        print("  1. \ud83d\ude80 Start Backend + Frontend")
        print("  2. \ud83d\uded1 Stop all services")
        print("  3. \ud83d\udce6 Backup important files")
        print("  4. \ud83d\udcca Show status")
        print("  5. \ud83e\uddf9 Clear cache")
        print("  6. \ud83d\udcdd Install dependencies")
        print("  0. \u274c Exit")
        print("  \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500")

    def _start_process(self, cmd, cwd):
        if self.is_windows:
            return subprocess.Popen(cmd, cwd=cwd, shell=True,
                                    creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            return subprocess.Popen(cmd, cwd=cwd, shell=True,
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL,
                                    start_new_session=True)

    def run_services(self):
        self.print_header()
        print("\n\ud83d\ude80 Starting services...")

        try:
            print("  \u2699\ufe0f  Backend (Flask)...")
            if self.is_windows:
                p1 = self._start_process("start cmd /k python app.py", BACKEND_DIR)
            else:
                p1 = self._start_process(f"{sys.executable} app.py", BACKEND_DIR)
            self.processes.append(p1)
            print("  \u2705 Backend started!")

            print("  \u2699\ufe0f  Frontend (Vue.js)...")
            if self.is_windows:
                p2 = self._start_process("start cmd /k npm run dev", FRONTEND_DIR)
            else:
                p2 = self._start_process("npm run dev", FRONTEND_DIR)
            self.processes.append(p2)
            print("  \u2705 Frontend started!")

        except Exception as e:
            print(f"  \u274c Error: {e}")

        print("\n\u2705 Services started!")
        print("  \ud83d\udd17 Backend:  http://127.0.0.1:5000")
        print("  \ud83d\udd17 Frontend: http://localhost:5173/")
        print("\n\u26a0\ufe0f  To stop services, select option 2.")

        input("\n\ud83d\udd39 Press Enter to return...")

    def stop_services(self):
        self.print_header()
        print("\n\ud83d\uded1 Stopping services...")
        for p in self.processes:
            try:
                p.terminate()
                p.wait(timeout=5)
            except Exception:
                try:
                    p.kill()
                except Exception:
                    pass
        self.processes = []
        print("\u2705 Stopped.")
        input("\n\ud83d\udd39 Press Enter to return...")

    def create_backup(self):
        self.print_header()
        print("\n\ud83d\udce6 Creating backup...")

        backup_dir = PROJECT_ROOT / "backups"
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"backup_{timestamp}.md"

        files = {
            "Backend": ["app.py", "physiology_engine.py", "requirements.txt"],
            "Frontend": [
                "src/App.vue", "src/main.js", "src/style.css",
                "src/services/api.js",
                "src/components/CalculatorTab.vue",
                "src/components/AlertsTab.vue",
                "src/components/HelpTab.vue",
                "src/components/ReferencesTab.vue",
                "src/icons/index.js",
                "package.json", "vite.config.js",
                "tailwind.config.js", "postcss.config.js"
            ]
        }

        content = ["# \ud83d\udce6 Backup", f"\n**Date:** {timestamp}", f"**Path:** {PROJECT_ROOT}", "\n" + "=" * 60]

        for category, file_list in files.items():
            content.append(f"\n## \ud83d\udcc1 {category}\n")
            for fname in file_list:
                full_path = (BACKEND_DIR if category == "Backend" else FRONTEND_DIR) / fname
                if full_path.exists():
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            ext = full_path.suffix
                            lang = 'python' if ext == '.py' else 'javascript' if ext in ('.js', '.vue') else ''
                            content.append(f"\n### `{fname}`\n```{lang}")
                            content.append(f.read())
                            content.append("```\n")
                            print(f"  \u2705 {category}/{fname}")
                    except Exception:
                        print(f"  \u274c {category}/{fname}")
                else:
                    print(f"  \u26a0\ufe0f {category}/{fname} not found")

        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))

        print(f"\n\u2705 Backup: {backup_file}")
        input("\n\ud83d\udd39 Press Enter to return...")

    def show_status(self):
        self.print_header()
        print("\n\ud83d\udcca Status:")

        if not self.processes:
            print("  \u2139\ufe0f  No services running.")
        else:
            for i, p in enumerate(self.processes):
                status = "Running" if p.poll() is None else "Stopped"
                icon = "\ud83d\udfe2" if p.poll() is None else "\ud83d\udd34"
                print(f"  {icon} Service {i+1}: {status}")

        input("\n\ud83d\udd39 Press Enter to return...")

    def clear_cache(self):
        self.print_header()
        print("\n\ud83e\uddf9 Clearing cache...")

        dirs = [
            FRONTEND_DIR / "node_modules/.cache",
            FRONTEND_DIR / "dist",
            BACKEND_DIR / "__pycache__",
            BACKEND_DIR / ".pytest_cache"
        ]

        for d in dirs:
            if d.exists():
                shutil.rmtree(d)
                print(f"  \u2705 {d.name} removed")

        print("\n\u2705 Done.")
        input("\n\ud83d\udd39 Press Enter to return...")

    def install_dependencies(self):
        self.print_header()
        print("\n\ud83d\udce6 Installing dependencies...")

        print("\n  \u2699\ufe0f  Backend...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            cwd=BACKEND_DIR
        )

        print("\n  \u2699\ufe0f  Frontend...")
        subprocess.run(["npm", "install"], cwd=FRONTEND_DIR)

        print("\n\u2705 Done.")
        input("\n\ud83d\udd39 Press Enter to return...")

    def run(self):
        while True:
            self.print_header()
            self.print_menu()

            choice = input("\n\ud83d\udd39 Select option: ").strip()

            if choice == '1':
                self.run_services()
            elif choice == '2':
                self.stop_services()
            elif choice == '3':
                self.create_backup()
            elif choice == '4':
                self.show_status()
            elif choice == '5':
                self.clear_cache()
            elif choice == '6':
                self.install_dependencies()
            elif choice == '0':
                print("\n\ud83d\udc4b Goodbye!")
                self.stop_services()
                sys.exit(0)
            else:
                print("\n\u274c Invalid option.")
                input("\n\ud83d\udd39 Press Enter...")


if __name__ == "__main__":
    try:
        ProjectManager().run()
    except KeyboardInterrupt:
        print("\n\n\ud83d\udc4b Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\u274c Error: {e}")
        sys.exit(1)
