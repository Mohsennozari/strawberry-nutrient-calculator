#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Strawberry Nutrient System - Project Manager
"""

import os
import sys
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.absolute()
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"


class ProjectManager:
    def __init__(self):
        self.processes = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print("=" * 60)
        print("  🍓 Strawberry Nutrient System - Manager")
        print("=" * 60)
        print(f"  📁 {PROJECT_ROOT}")
        print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

    def print_menu(self):
        print("\n📋 Menu:")
        print("  ─────────────────────────────────────")
        print("  1. 🚀 Start Backend + Frontend")
        print("  2. 🛑 Stop all services")
        print("  3. 📦 Backup important files")
        print("  4. 📊 Show status")
        print("  5. 🧹 Clear cache")
        print("  6. 📝 Install dependencies")
        print("  0. ❌ Exit")
        print("  ─────────────────────────────────────")

    # ============================================================
    # 1. RUN SERVICES
    # ============================================================
    def run_services(self):
        self.print_header()
        print("\n🚀 Starting services...")

        try:
            # Backend
            print("  ⚙️  Backend (Flask)...")
            p1 = subprocess.Popen(
                "start cmd /k python app.py",
                cwd=BACKEND_DIR,
                shell=True
            )
            self.processes.append(p1)
            print("  ✅ Backend started!")

            # Frontend
            print("  ⚙️  Frontend (Vue.js)...")
            p2 = subprocess.Popen(
                "start cmd /k npm run dev",
                cwd=FRONTEND_DIR,
                shell=True
            )
            self.processes.append(p2)
            print("  ✅ Frontend started!")

        except Exception as e:
            print(f"  ❌ Error: {e}")

        print("\n✅ Services started!")
        print("  🔗 Backend:  http://127.0.0.1:5000")
        print("  🔗 Frontend: http://localhost:5173/")
        print("\n⚠️  To stop services, select option 2.")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 2. STOP SERVICES
    # ============================================================
    def stop_services(self):
        self.print_header()
        print("\n🛑 Stopping services...")
        for p in self.processes:
            try:
                p.terminate()
            except:
                pass
        self.processes = []
        print("✅ Stopped.")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 3. BACKUP
    # ============================================================
    def create_backup(self):
        self.print_header()
        print("\n📦 Creating backup...")

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

        content = ["# 📦 Backup", f"\n**Date:** {timestamp}", f"**Path:** {PROJECT_ROOT}", "\n" + "=" * 60]

        for category, file_list in files.items():
            content.append(f"\n## 📁 {category}\n")
            for fname in file_list:
                full_path = (BACKEND_DIR if category == "Backend" else FRONTEND_DIR) / fname
                if full_path.exists():
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content.append(f"\n### `{fname}`\n```python" if fname.endswith('.py') else f"\n### `{fname}`\n```")
                            content.append(f.read())
                            content.append("```\n")
                            print(f"  ✅ {category}/{fname}")
                    except:
                        print(f"  ❌ {category}/{fname}")
                else:
                    print(f"  ⚠️ {category}/{fname} not found")

        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))

        print(f"\n✅ Backup: {backup_file}")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 4. STATUS
    # ============================================================
    def show_status(self):
        self.print_header()
        print("\n📊 Status:")

        if not self.processes:
            print("  ℹ️  No services running.")
        else:
            for i, p in enumerate(self.processes):
                status = "Running" if p.poll() is None else "Stopped"
                icon = "🟢" if p.poll() is None else "🔴"
                print(f"  {icon} Service {i+1}: {status}")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 5. CLEAR CACHE
    # ============================================================
    def clear_cache(self):
        self.print_header()
        print("\n🧹 Clearing cache...")

        dirs = [
            FRONTEND_DIR / "node_modules/.cache",
            FRONTEND_DIR / "dist",
            BACKEND_DIR / "__pycache__",
            BACKEND_DIR / ".pytest_cache"
        ]

        for d in dirs:
            if d.exists():
                shutil.rmtree(d)
                print(f"  ✅ {d.name} removed")

        print("\n✅ Done.")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 6. INSTALL DEPENDENCIES
    # ============================================================
    def install_dependencies(self):
        self.print_header()
        print("\n📦 Installing dependencies...")

        print("\n  ⚙️  Backend...")
        subprocess.run(
            f'"{sys.executable}" -m pip install -r requirements.txt',
            cwd=BACKEND_DIR,
            shell=True
        )

        print("\n  ⚙️  Frontend...")
        subprocess.run("npm install", cwd=FRONTEND_DIR, shell=True)

        print("\n✅ Done.")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # MAIN
    # ============================================================
    def run(self):
        while True:
            self.print_header()
            self.print_menu()

            choice = input("\n🔹 Select option: ").strip()

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
                print("\n👋 Goodbye!")
                self.stop_services()
                sys.exit(0)
            else:
                print("\n❌ Invalid option.")
                input("\n🔹 Press Enter...")


if __name__ == "__main__":
    try:
        ProjectManager().run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
