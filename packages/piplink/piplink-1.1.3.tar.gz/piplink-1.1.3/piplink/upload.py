import os
import time
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import hashlib
import re
import getpass

def get_package_info():
    with open("setup.py", "r") as f:
        setup_content = f.read()
    
    name_match = re.search(r"name\s*=\s*['\"]([^'\"]+)['\"]", setup_content)
    version_match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", setup_content)
    
    if not name_match or not version_match:
        raise ValueError("Package name or version not found in setup.py")
    
    package_name = name_match.group(1)
    package_version = version_match.group(1)
    
    return package_name, package_version

def upload_to_pypi(token):
    try:
        package_name, package_version = get_package_info()
    except ValueError as e:
        print(e)
        exit(1)

    pypi_api = "https://upload.pypi.org/legacy/"

    time.sleep(5)

    dist_file = f"dist/{package_name}-{package_version}.tar.gz"

    if not os.path.isfile(dist_file):
        print(f"File {dist_file} not found. Make sure the setup.py file ran correctly.")
        exit(1)

    try:
        with open(dist_file, "rb") as f:
            md5 = hashlib.md5(f.read()).hexdigest()
            f.seek(0)

            encoder = MultipartEncoder(
                fields={
                    ":action": "file_upload",
                    "protocol_version": "1",
                    "name": package_name,
                    "version": package_version,
                    "content": (os.path.basename(dist_file), f, "application/gzip"),
                    "md5_digest": md5,
                    "filetype": "sdist",
                    "metadata_version": "2.1"
                }
            )

            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": encoder.content_type
            }

            response = requests.post(pypi_api, headers=headers, data=encoder.to_string())

            if response.status_code == 200:
                print(f"Package {package_name} {package_version} uploaded successfully!")
                print(f"LinkedIn: https://pypi.org/project/{package_name}/{package_version}")
            else:
                error_message = re.search(r"<h1>(.*?)</h1>", response.text)
                if error_message:
                    print(f"Error uploading package: {response.status_code} {error_message.group(1)}")
                else:
                    print(f"Error uploading package: {response.status_code}")
    except FileNotFoundError:
        print(f"File {dist_file} not found after running sdist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    token = getpass.getpass("Enter your PyPI token: ").strip()
    upload_to_pypi(token)
