#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🍓 Strawberry Nutrient System - Project Manager

یک ابزار مدیریت یکپارچه برای اجرا، بکاپ‌گیری و نگهداری پروژه
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
CORE_DIR = BACKEND_DIR / "core"  # ✅ مسیر جدید core


class ProjectManager:
    def __init__(self):
        self.processes = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print("=" * 70)
        print("  🍓 Strawberry Nutrient System - Manager  v2.0")
        print("=" * 70)
        print(f"  📁 Project: {PROJECT_ROOT}")
        print(f"  📅 Date:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  🐍 Python:  {sys.version.split()[0]}")
        print("=" * 70)

    def print_menu(self):
        print("\n📋 Main Menu:")
        print("  ──────────────────────────────────────────────────────")
        print("  1. 🚀 Start Backend + Frontend")
        print("  2. 🛑 Stop all services")
        print("  3. 📦 Backup important files")
        print("  4. 📊 Show status")
        print("  5. 🧹 Clear cache (node_modules, __pycache__, dist)")
        print("  6. 📝 Install dependencies")
        print("  7. 🧪 Run tests")
        print("  0. ❌ Exit")
        print("  ──────────────────────────────────────────────────────")

    # ============================================================
    # 1. RUN SERVICES
    # ============================================================
    def run_services(self):
        self.print_header()
        print("\n🚀 Starting services...")

        try:
            # ===== Backend (Flask) =====
            print("\n  ⚙️  Backend (Flask + Core modules)...")
            print(f"      📁 {BACKEND_DIR}")
            print(f"      📁 {CORE_DIR} (3 modules)")

            p1 = subprocess.Popen(
                "start cmd /k \"python app.py\"",
                cwd=BACKEND_DIR,
                shell=True
            )
            self.processes.append(p1)
            print("  ✅ Backend started on port 5000!")

            # ===== Frontend (Vue.js) =====
            print("\n  ⚙️  Frontend (Vue.js + Tailwind)...")
            print(f"      📁 {FRONTEND_DIR}")

            p2 = subprocess.Popen(
                "start cmd /k \"npm run dev\"",
                cwd=FRONTEND_DIR,
                shell=True
            )
            self.processes.append(p2)
            print("  ✅ Frontend started on port 5173!")

        except Exception as e:
            print(f"\n  ❌ Error: {e}")

        print("\n" + "=" * 70)
        print("✅ Services started successfully!")
        print("  🔗 Backend:  http://127.0.0.1:5000")
        print("  🔗 Frontend: http://localhost:5173")
        print("  📚 API Docs: http://127.0.0.1:5000/health")
        print("\n  ⚠️  To stop services, select option 2.")
        print("=" * 70)

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 2. STOP SERVICES
    # ============================================================
    def stop_services(self):
        self.print_header()
        print("\n🛑 Stopping all services...")

        if not self.processes:
            print("  ℹ️  No services are running.")
        else:
            count = 0
            for p in self.processes:
                try:
                    p.terminate()
                    count += 1
                except:
                    pass
            self.processes = []
            print(f"  ✅ {count} service(s) stopped.")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 3. BACKUP (به‌روز شده با فایل‌های جدید)
    # ============================================================
    def create_backup(self):
        self.print_header()
        print("\n📦 Creating backup...")

        backup_dir = PROJECT_ROOT / "backups"
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"backup_{timestamp}.md"

        # ✅ فایل‌های جدید اضافه شدند
        files = {
            "Backend": [
                "app.py",
                "requirements.txt",
                "test_ec_ph.py"
            ],
            "Backend/Core": [
                "core/__init__.py",
                "core/data_sources.py",
                "core/alerts_engine.py",
                "core/physiology_engine.py"
            ],
            "Frontend": [
                "src/App.vue",
                "src/main.js",
                "src/style.css",
                "src/services/api.js",
                "src/components/CalculatorTab.vue",
                "src/components/AlertsTab.vue",
                "src/components/HelpTab.vue",
                "src/components/ReferencesTab.vue",
                "src/icons/index.js",
                "package.json",
                "vite.config.js",
                "tailwind.config.js",
                "postcss.config.js"
            ],
            "Project Files": [
                "manage.py",
                "README.md"
            ]
        }

        content = [
            "# 📦 Backup",
            "",
            f"**Date:** {timestamp}",
            f"**Path:** {PROJECT_ROOT}",
            f"**Version:** 2.0 (Modular Architecture)",
            "",
            "=" * 70,
            ""
        ]

        total_files = 0

        for category, file_list in files.items():
            content.append(f"## 📁 {category}\n")
            base_dir = BACKEND_DIR if "Backend" in category or "Core" in category else \
                       FRONTEND_DIR if "Frontend" in category else PROJECT_ROOT

            for fname in file_list:
                full_path = base_dir / fname
                if full_path.exists():
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            # تشخیص زبان برای syntax highlighting
                            ext = full_path.suffix.lower()
                            if ext in ['.py']:
                                lang = 'python'
                            elif ext in ['.vue']:
                                lang = 'vue'
                            elif ext in ['.js']:
                                lang = 'javascript'
                            elif ext in ['.css']:
                                lang = 'css'
                            elif ext in ['.json']:
                                lang = 'json'
                            elif ext in ['.md']:
                                lang = 'markdown'
                            else:
                                lang = 'text'

                            content.append(f"\n### `{fname}`\n```{lang}")
                            content.append(f.read().strip())
                            content.append("```\n")
                            print(f"  ✅ {category}/{fname}")
                            total_files += 1
                    except Exception as e:
                        print(f"  ❌ {category}/{fname} (Error: {e})")
                else:
                    print(f"  ⚠️ {category}/{fname} not found")

        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))

        print(f"\n✅ Backup completed!")
        print(f"   📁 File: {backup_file}")
        print(f"   📄 Files backed up: {total_files}")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 4. STATUS
    # ============================================================
    def show_status(self):
        self.print_header()
        print("\n📊 System Status:")

        # ===== Services =====
        print("\n  🟢 Services:")
        if not self.processes:
            print("     ℹ️  No services running.")
        else:
            for i, p in enumerate(self.processes):
                status = "🟢 Running" if p.poll() is None else "🔴 Stopped"
                print(f"     {status} - Service {i+1}")

        # ===== Backend Files =====
        print("\n  📁 Backend Structure:")
        backend_files = [
            ("app.py", BACKEND_DIR / "app.py"),
            ("core/__init__.py", CORE_DIR / "__init__.py"),
            ("core/data_sources.py", CORE_DIR / "data_sources.py"),
            ("core/alerts_engine.py", CORE_DIR / "alerts_engine.py"),
            ("core/physiology_engine.py", CORE_DIR / "physiology_engine.py"),
            ("test_ec_ph.py", BACKEND_DIR / "test_ec_ph.py")
        ]

        for name, path in backend_files:
            icon = "✅" if path.exists() else "❌"
            print(f"     {icon} {name}")

        # ===== Frontend Files =====
        print("\n  📁 Frontend Structure:")
        frontend_files = [
            ("App.vue", FRONTEND_DIR / "src/App.vue"),
            ("AlertsTab.vue", FRONTEND_DIR / "src/components/AlertsTab.vue"),
            ("CalculatorTab.vue", FRONTEND_DIR / "src/components/CalculatorTab.vue")
        ]

        for name, path in frontend_files:
            icon = "✅" if path.exists() else "❌"
            print(f"     {icon} {name}")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 5. CLEAR CACHE
    # ============================================================
    def clear_cache(self):
        self.print_header()
        print("\n🧹 Clearing cache...")

        dirs = [
            (FRONTEND_DIR / "node_modules/.cache", "Frontend cache"),
            (FRONTEND_DIR / "dist", "Frontend dist"),
            (BACKEND_DIR / "__pycache__", "Python cache"),
            (BACKEND_DIR / ".pytest_cache", "Pytest cache"),
            (CORE_DIR / "__pycache__", "Core cache")  # ✅ مسیر جدید
        ]

        removed = 0
        for d, name in dirs:
            if d.exists():
                shutil.rmtree(d)
                print(f"  ✅ {name} removed")
                removed += 1
            else:
                print(f"  ℹ️ {name} not found")

        print(f"\n✅ Done. {removed} items removed.")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 6. INSTALL DEPENDENCIES
    # ============================================================
    def install_dependencies(self):
        self.print_header()
        print("\n📦 Installing dependencies...")

        # ===== Backend =====
        print("\n  ⚙️  Backend (Python)...")
        req_file = BACKEND_DIR / "requirements.txt"
        if req_file.exists():
            result = subprocess.run(
                f'"{sys.executable}" -m pip install -r requirements.txt',
                cwd=BACKEND_DIR,
                shell=True,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("  ✅ Backend dependencies installed!")
            else:
                print(f"  ❌ Error: {result.stderr}")
        else:
            print("  ⚠️ requirements.txt not found!")

        # ===== Frontend =====
        print("\n  ⚙️  Frontend (Node.js)...")
        if (FRONTEND_DIR / "package.json").exists():
            result = subprocess.run(
                "npm install",
                cwd=FRONTEND_DIR,
                shell=True,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("  ✅ Frontend dependencies installed!")
            else:
                print(f"  ❌ Error: {result.stderr}")
        else:
            print("  ⚠️ package.json not found!")

        print("\n✅ Done.")
        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 7. RUN TESTS
    # ============================================================
    def run_tests(self):
        self.print_header()
        print("\n🧪 Running tests...")

        test_file = BACKEND_DIR / "test_ec_ph.py"
        if test_file.exists():
            print("\n  ⚙️ Running EC/pH tests...")
            result = subprocess.run(
                f'"{sys.executable}" test_ec_ph.py',
                cwd=BACKEND_DIR,
                shell=True,
                capture_output=True,
                text=True
            )

            print("\n" + "=" * 70)
            print("📊 Test Results:")
            print("=" * 70)

            if result.returncode == 0:
                print("✅ All tests passed!")
                print("\n" + result.stdout)
            else:
                print("❌ Some tests failed!")
                print("\n" + result.stderr)

        else:
            print("  ⚠️ test_ec_ph.py not found!")

        print("\n" + "=" * 70)
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
            elif choice == '7':
                self.run_tests()
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
