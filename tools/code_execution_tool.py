import subprocess
import tempfile
import os


def execute_python_code(code):

    temp_file = None

    try:

        # Create temporary python file
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as f:

            f.write(code)

            temp_file = f.name

        # Execute code
        result = subprocess.run(
            ["python", temp_file],
            capture_output=True,
            text=True,
            timeout=20
        )

        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        if temp_file and os.path.exists(temp_file):

            os.remove(temp_file)