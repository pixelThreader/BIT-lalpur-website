import subprocess
import sys
import pkg_resources

def install(package):
    try:
        pkg_resources.get_distribution(package)
        print(f"{package} is already installed")
    except pkg_resources.DistributionNotFound:
        print(f"Installing {package}...")
        process = subprocess.Popen(
            [sys.executable, "-m", "pip", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
        if rc == 0:
            print(f"Successfully installed {package}")
        else:
            error_output = process.stderr.read()
            print(f"Failed to install {package}. Error: {error_output}")

# Example usage
install("python-dotenv")
