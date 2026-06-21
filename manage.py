#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🍓 Strawberry Nutrient System - Project Manager v2.0

یک ابزار مدیریت یکپارچه برای اجرا، بکاپ‌گیری و نگهداری پروژه
با پشتیبانی از ساختار ماژولار و سیستم احراز هویت
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
CORE_DIR = BACKEND_DIR / "core"          # ✅ مسیر جدید core
LOGS_DIR = BACKEND_DIR / "logs"          # ✅ مسیر جدید logs
INSTANCE_DIR = BACKEND_DIR / "instance"  # ✅ مسیر جدید instance


class ProjectManager:
    def __init__(self):
        self.processes = []
        self.is_windows = platform.system() == 'Windows'

    def clear_screen(self):
        os.system('cls' if self.is_windows else 'clear')

    def print_header(self):
        self.clear_screen()
        print("=" * 70)
        print("  🍓 Strawberry Nutrient System - Manager v2.0")
        print("=" * 70)
        print(f"  📁 Project: {PROJECT_ROOT}")
        print(f"  📅 Date:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  💻 System:  {platform.system()} ({platform.machine()})")
        print(f"  🐍 Python:  {sys.version.split()[0]}")
        print("=" * 70)

    def print_menu(self):
        print("\n📋 Main Menu:")
        print("  ──────────────────────────────────────────────────────")
        print("  1. 🚀 Start Backend + Frontend")
        print("  2. 🛑 Stop all services")
        print("  3. 📦 Backup important files")
        print("  4. 📊 Show status")
        print("  5. 🧹 Clear cache (node_modules, __pycache__, dist, logs)")
        print("  6. 📝 Install dependencies")
        print("  7. 🧪 Run tests")
        print("  8. 🗄️  Backup database")
        print("  0. ❌ Exit")
        print("  ──────────────────────────────────────────────────────")

    def _start_process(self, cmd, cwd):
        """شروع یک فرایند در ترمینال جداگانه"""
        if self.is_windows:
            return subprocess.Popen(
                cmd,
                cwd=cwd,
                shell=True,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            return subprocess.Popen(
                cmd,
                cwd=cwd,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )

    # ============================================================
    # 1. RUN SERVICES
    # ============================================================
    def run_services(self):
        self.print_header()
        print("\n🚀 Starting services...")

        try:
            # ===== Backend (Flask) =====
            print("\n  ⚙️  Backend (Flask + Core modules + Auth)...")
            print(f"      📁 {BACKEND_DIR}")
            print(f"      📁 {CORE_DIR} (3 modules)")
            print(f"      📁 {LOGS_DIR} (Logs)")
            print(f"      📁 {INSTANCE_DIR} (Database)")

            if self.is_windows:
                p1 = self._start_process("start cmd /k \"python app.py\"", BACKEND_DIR)
            else:
                p1 = self._start_process(f"{sys.executable} app.py", BACKEND_DIR)
            self.processes.append(p1)
            print("  ✅ Backend started on port 5000!")

            # ===== Frontend (Vue.js) =====
            print("\n  ⚙️  Frontend (Vue.js + Tailwind + Auth)...")
            print(f"      📁 {FRONTEND_DIR}")

            if self.is_windows:
                p2 = self._start_process("start cmd /k \"npm run dev\"", FRONTEND_DIR)
            else:
                p2 = self._start_process("npm run dev", FRONTEND_DIR)
            self.processes.append(p2)
            print("  ✅ Frontend started on port 5173!")

        except Exception as e:
            print(f"\n  ❌ Error: {e}")

        print("\n" + "=" * 70)
        print("✅ Services started successfully!")
        print("  🔗 Backend:  http://127.0.0.1:5000")
        print("  🔗 Frontend: http://localhost:5173")
        print("  🔐 Auth API: http://127.0.0.1:5000/auth/register")
        print("  📚 API Docs: http://127.0.0.1:5000/api/docs")
        print("  💚 Health:   http://127.0.0.1:5000/health")
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
                    p.wait(timeout=5)
                    count += 1
                except Exception:
                    try:
                        p.kill()
                        count += 1
                    except Exception:
                        pass
            self.processes = []
            print(f"  ✅ {count} service(s) stopped.")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 3. BACKUP (✅ به‌روز شده با فایل‌های جدید)
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
            "Backend (Main)": [
                "app.py",
                "auth.py",
                "database.py",
                "requirements.txt",
                "test_ec_ph.py"
            ],
            "Backend (Core Modules)": [
                "core/__init__.py",
                "core/data_sources.py",
                "core/alerts_engine.py",
                "core/physiology_engine.py"
            ],
            "Frontend (Main)": [
                "src/App.vue",
                "src/main.js",
                "src/style.css"
            ],
            "Frontend (Services)": [
                "src/services/api.js",
                "src/services/auth.js"
            ],
            "Frontend (Views)": [
                "src/views/AuthView.vue"
            ],
            "Frontend (Components)": [
                "src/components/CalculatorTab.vue",
                "src/components/AlertsTab.vue",
                "src/components/AboutTab.vue",
                "src/components/HelpTab.vue",
                "src/components/ReferencesTab.vue",
                "src/components/calculator/CalculatorForm.vue",
                "src/components/calculator/ResultTable.vue",
                "src/components/calculator/EmptyState.vue"
            ],
            "Frontend (Icons)": [
                "src/icons/index.js"
            ],
            "Frontend (Config)": [
                "package.json",
                "vite.config.js",
                "tailwind.config.js",
                "postcss.config.js"
            ],
            "Project Files": [
                "manage.py",
                "README.md",
                ".gitignore"
            ]
        }

        content = [
            "# 📦 Backup",
            "",
            f"**Date:** {timestamp}",
            f"**Path:** {PROJECT_ROOT}",
            f"**Version:** 2.0 (Modular Architecture + Auth)",
            "",
            "=" * 70,
            ""
        ]

        total_files = 0

        for category, file_list in files.items():
            content.append(f"## 📁 {category}\n")

            # تعیین مسیر پایه
            if "Backend" in category:
                base_dir = BACKEND_DIR
            elif "Frontend" in category:
                base_dir = FRONTEND_DIR
            else:
                base_dir = PROJECT_ROOT

            for fname in file_list:
                full_path = base_dir / fname
                if full_path.exists():
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            # تشخیص زبان برای syntax highlighting
                            ext = full_path.suffix.lower()
                            lang_map = {
                                '.py': 'python',
                                '.vue': 'vue',
                                '.js': 'javascript',
                                '.css': 'css',
                                '.json': 'json',
                                '.md': 'markdown',
                                '.txt': 'text',
                                '.yml': 'yaml',
                                '.yaml': 'yaml',
                                '.sh': 'bash'
                            }
                            lang = lang_map.get(ext, 'text')

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
        print(f"   📦 Size: {backup_file.stat().st_size / 1024:.1f} KB")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 4. STATUS (✅ به‌روز شده)
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
            ("auth.py", BACKEND_DIR / "auth.py"),
            ("database.py", BACKEND_DIR / "database.py"),
            ("core/__init__.py", CORE_DIR / "__init__.py"),
            ("core/data_sources.py", CORE_DIR / "data_sources.py"),
            ("core/alerts_engine.py", CORE_DIR / "alerts_engine.py"),
            ("core/physiology_engine.py", CORE_DIR / "physiology_engine.py"),
            ("test_ec_ph.py", BACKEND_DIR / "test_ec_ph.py"),
            ("logs/", LOGS_DIR),
            ("instance/", INSTANCE_DIR)
        ]

        for name, path in backend_files:
            icon = "✅" if path.exists() else "❌"
            print(f"     {icon} {name}")

        # ===== Frontend Files =====
        print("\n  📁 Frontend Structure:")
        frontend_files = [
            ("App.vue", FRONTEND_DIR / "src/App.vue"),
            ("AuthView.vue", FRONTEND_DIR / "src/views/AuthView.vue"),
            ("AlertsTab.vue", FRONTEND_DIR / "src/components/AlertsTab.vue"),
            ("AboutTab.vue", FRONTEND_DIR / "src/components/AboutTab.vue"),
            ("CalculatorTab.vue", FRONTEND_DIR / "src/components/CalculatorTab.vue"),
            ("api.js", FRONTEND_DIR / "src/services/api.js"),
            ("auth.js", FRONTEND_DIR / "src/services/auth.js")
        ]

        for name, path in frontend_files:
            icon = "✅" if path.exists() else "❌"
            print(f"     {icon} {name}")

        # ===== Auth Status =====
        print("\n  🔐 Authentication:")
        jwt_secret = os.environ.get('JWT_SECRET', 'dev-secret-change-me')
        if jwt_secret == 'dev-secret-change-me':
            print("     ⚠️  Using default JWT_SECRET (not secure for production)")
        else:
            print("     ✅ JWT_SECRET is configured")

        # ===== Database =====
        db_path = INSTANCE_DIR / "database.db"
        if db_path.exists():
            size = db_path.stat().st_size / 1024
            print(f"     ✅ Database: {size:.1f} KB")
        else:
            print("     ⚠️  Database not initialized yet")

        input("\n🔹 Press Enter to return...")

    # ============================================================
    # 5. CLEAR CACHE (✅ به‌روز شده)
    # ============================================================
    def clear_cache(self):
        self.print_header()
        print("\n🧹 Clearing cache...")

        dirs = [
            (FRONTEND_DIR / "node_modules/.cache", "Frontend cache"),
            (FRONTEND_DIR / "dist", "Frontend dist"),
            (BACKEND_DIR / "__pycache__", "Python cache"),
            (BACKEND_DIR / ".pytest_cache", "Pytest cache"),
            (CORE_DIR / "__pycache__", "Core cache"),
            (LOGS_DIR, "Logs directory")  # ✅ پاک کردن لاگ‌ها
        ]

        removed = 0
        for d, name in dirs:
            if d.exists():
                shutil.rmtree(d)
                print(f"  ✅ {name} removed")
                removed += 1
            else:
                print(f"  ℹ️ {name} not found")

        # بازسازی پوشه logs
        LOGS_DIR.mkdir(exist_ok=True)
        print(f"  ✅ Logs directory recreated")

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
                [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                cwd=BACKEND_DIR,
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
                ["npm", "install"],
                cwd=FRONTEND_DIR,
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
                [sys.executable, "test_ec_ph.py"],
                cwd=BACKEND_DIR,
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
    # 8. BACKUP DATABASE (✅ جدید)
    # ============================================================
    def backup_database(self):
        self.print_header()
        print("\n🗄️  Backing up database...")

        db_path = INSTANCE_DIR / "database.db"
        if not db_path.exists():
            print("  ⚠️ Database not found! (Run the app first to create it)")
            input("\n🔹 Press Enter to return...")
            return

        backup_dir = PROJECT_ROOT / "backups" / "database"
        backup_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"database_{timestamp}.db"

        try:
            shutil.copy2(db_path, backup_file)
            size = backup_file.stat().st_size / 1024
            print(f"  ✅ Database backed up: {backup_file}")
            print(f"  📦 Size: {size:.1f} KB")
            print(f"  📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"  ❌ Error: {e}")

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
            elif choice == '8':
                self.backup_database()
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
