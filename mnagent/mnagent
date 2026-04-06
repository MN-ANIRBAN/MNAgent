import ast
import subprocess
import sys
import importlib.util
import importlib.metadata
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def mnagent_header():
    print(f"\n{Colors.CYAN}{' '*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}          MN-AGENT v2.4 | Advanced Dependency Guard{Colors.ENDC}")
    print(f"{Colors.CYAN}{' '*60}{Colors.ENDC}")

def run_pip_command(command_list):
    try:
        subprocess.check_call([sys.executable, "-m", "pip"] + command_list + ["--no-warn-script-location"])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies():
    mnagent_header()

    print(f"{Colors.YELLOW}{Colors.BOLD}[STEP 1]{Colors.ENDC} Checking for Pip updates...")
    run_pip_command(["install", "--upgrade", "pip"])
    print(f"{Colors.GREEN}✓ Pip management complete.{Colors.ENDC}\n")

    main_script_path = sys.argv[0]
    if not main_script_path.endswith('.py'):
        print(f"{Colors.RED}Execution context not recognized as a Python script.{Colors.ENDC}")
        return

    print(f"{Colors.YELLOW}{Colors.BOLD}[STEP 2]{Colors.ENDC} Analyzing imports in: {Colors.CYAN}{os.path.basename(main_script_path)}{Colors.ENDC}")
    try:
        with open(main_script_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except Exception as e:
        print(f"{Colors.RED}✗ Error reading script: {e}{Colors.ENDC}")
        return

    required_libs = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = node.names if isinstance(node, ast.Import) else [ast.alias(name=node.module)]
            for n in names:
                if n.name:
                    required_libs.add(n.name.split('.')[0])

    mapping = {
        "cv2": "opencv-python",
        "sklearn": "scikit-learn",
        "PIL": "pillow",
        "yaml": "pyyaml",
        "firebase_admin": "firebase-admin"
    }

    print(f"{Colors.BLUE}Detected Modules: {Colors.ENDC}{', '.join(required_libs)}")
    print(f"{Colors.YELLOW}{Colors.BOLD}[STEP 3]{Colors.ENDC} Synchronizing Packages...\n")

    for lib in required_libs:
        if lib in ['mnagent4', 'os', 'sys', 'ast', 'subprocess', 'importlib', 'json', 'datetime', 'time', 're', 'math', 'os.path']:
            continue
            
        install_name = mapping.get(lib, lib)
        spec = importlib.util.find_spec(lib)

        if spec is not None:
            print(f"{Colors.CYAN}Checking for updates: {Colors.BOLD}{install_name}{Colors.ENDC}")
            run_pip_command(["install", "--upgrade", install_name])
        else:
            print(f"{Colors.RED}{Colors.BOLD}MISSING MODULE:{Colors.ENDC} {install_name}")
            print(f"{Colors.YELLOW}Downloading and Installing...{Colors.ENDC}")
            if run_pip_command(["install", install_name]):
                print(f"{Colors.GREEN}✓ {install_name} successfully integrated.{Colors.ENDC}")
            else:
                print(f"{Colors.RED}✗ Critical Error: Could not install {install_name}{Colors.ENDC}")

    print(f"\n{Colors.GREEN}{'-'*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.GREEN}      ENVIRONMENT READY | ALL DEPENDENCIES VERIFIED{Colors.ENDC}")
    print(f"{Colors.GREEN}{'-'*60}{Colors.ENDC}\n")

if __name__ != "__main__":
    try:
        check_and_install_dependencies()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Agent execution interrupted by user.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}Agent System Error: {e}{Colors.ENDC}")
