import re
import os
import sys
import json
import shutil
import zipapp
import zipfile
import hashlib
import tempfile
import argparse
from pathlib import Path
from datetime import datetime

# Constants
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

ZIPFILE_SPEC = "spec.json"
ZIPFILE_DATA_DIR = "data"

APPS_DIR = "/var/apps/"
APP_SPEC = "spec.json"

SERVICE_FILE_TMPL = "{name}.{instance}.service"


def is_self_zipapp() -> bool:
    return zipfile.is_zipfile(Path(__file__).parent)


def get_self_zipfile() -> zipfile.ZipFile:
    return zipfile.ZipFile(Path(__file__).parent)


def get_self_zipfile_path() -> zipfile.Path:
    return zipfile.Path(Path(__file__).parent)


def get_self_file():
    if is_self_zipapp():
        zip_file = get_self_zipfile_path()
        return zip_file.joinpath("__main__.py")
    return Path(__file__)


def is_valid_name(name: str) -> bool:
    return bool(re.fullmatch("[a-zA-Z0-9-_]+", name))


def build(args):
    self_file = get_self_file()
    with tempfile.TemporaryDirectory() as temp_dir_name:
        temp_path = Path(temp_dir_name)

        # Copy self
        temp_path.joinpath("__main__.py").write_text(self_file.read_text())

        # Copy script file
        script_path = Path(args.script)
        temp_path.joinpath(script_path.name).write_bytes(script_path.read_bytes())

        # Copy data
        if args.data:
            data_path = Path(args.data)
            if data_path.is_dir():
                shutil.copytree(args.data, temp_path / ZIPFILE_DATA_DIR)
            elif data_path.is_file():
                data_dir_path = temp_path / ZIPFILE_DATA_DIR
                data_dir_path.mkdir(parents=True, exist_ok=True)
                data_dir_path.joinpath(data_path.name).write_bytes(
                    data_path.read_bytes()
                )

        if is_self_zipapp():
            spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
            spec = json.loads(spec_path.read_text())
            population = spec.get("population", 0) + 1 if spec_path.exists() else 1

            population_history = spec.get("population_history", [])
            population_history.append(get_self_zipfile_path().name)
        else:
            population = 1
            population_history = [get_self_file().name]

        # Write spec.json file
        hashobj = hashlib.sha256()
        hashobj.update(script_path.name.encode())
        hashobj.update(b"\n")
        hashobj.update(script_path.read_bytes())

        temp_path.joinpath(ZIPFILE_SPEC).write_text(
            json.dumps(
                {
                    "script": script_path.name,
                    "hash": hashobj.hexdigest(),
                    "args": args.args,
                    "meta": {
                        key: value
                        for key, sep, value in map(
                            lambda s: s.partition("="), args.meta or []
                        )
                    },
                    "created": datetime.now().strftime(DATETIME_FORMAT),
                    "population": population,
                    "population_history": population_history,
                }
            )
        )

        # Create zipapp
        zipapp.create_archive(temp_path, args.output, args.interpreter)


def meta(args):
    if not is_self_zipapp():
        print("meta data is empty")
        return

    spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
    if not spec_path.exists():
        print("meta data is empty")
        return

    meta = json.loads(spec_path.read_text()).get("meta", {})
    if not meta:
        print("meta data is empty")
        return

    if args.keys:
        for key in args.keys:
            if key in meta:
                print(f"{key} = {meta[key]}")
        return

    for key, value in meta.items():
        print(f"{key} = {value}")


def list_instances(args):
    if not is_self_zipapp():
        sys.exit(-1)

    spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
    if not spec_path.exists():
        print("no spec")
        sys.exit(-1)

    spec = json.loads(spec_path.read_text())
    apps_path = Path(APPS_DIR)
    app_dirs = []
    for app_path in [p for p in apps_path.iterdir() if p.is_dir()]:
        app_spec = json.loads(app_path.joinpath(APP_SPEC).read_text())
        if app_spec["hash"] == spec["hash"]:
            app_dirs.append(app_path)

    for app_path in app_dirs:
        print(app_path.name)
        for instance_path in [p for p in app_path.iterdir() if p.is_dir()]:
            print(f"|_ {instance_path.name}")
        print()


def info(args):
    if not is_self_zipapp():
        print("no info")
        return

    spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
    if not spec_path.exists():
        print("no info")
        return

    spec = json.loads(spec_path.read_text())

    if args.keys:
        for key in args.keys:
            if key in spec:
                print(f"{key} = {spec[key]}")
            else:
                print(f"{key} = {None}")
        return

    for key, value in spec.items():
        print(f"{key} = {value}")


def unpack(args):
    if not is_self_zipapp():
        print("not script and data")
        sys.exit(-1)

    if not args.script and not args.data:
        print("no script or data argument specified")
        sys.exit(-1)

    spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
    if not spec_path.exists():
        print("no spec")
        sys.exit(-1)

    spec = json.loads(spec_path.read_text())

    if args.script:
        print(f"Unpack script to {args.script}")
        script_path = get_self_zipfile_path() / spec["script"]
        output_script_dir = Path(args.script)
        output_script_dir.joinpath(spec["script"]).write_bytes(script_path.read_bytes())

    if args.data:
        data_path = get_self_zipfile_path() / ZIPFILE_DATA_DIR
        if not data_path.exists():
            print("no data")
            sys.exit(-1)

        print(f"Unpack data to {args.data}")

        target_dir_path = Path(args.data)
        target_dir_path.mkdir(parents=True, exist_ok=True)
        zf = get_self_zipfile()
        data_dir = (
            ZIPFILE_DATA_DIR
            if ZIPFILE_DATA_DIR.endswith("/")
            else f"{ZIPFILE_DATA_DIR}/"
        )
        for zi in [
            zi
            for zi in zf.filelist
            if zi.filename.startswith(data_dir) and not zi.filename.endswith("/")
        ]:
            target_path = target_dir_path / zi.filename[len(data_dir) :]
            print(f"Extract {zi.filename} => {target_path}")
            if zi.is_dir():
                target_path.mkdir(parents=True, exist_ok=True)
            else:
                with zf.open(zi) as io:
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    target_path.write_bytes(io.read())


def setup(args):
    if not is_self_zipapp():
        print("not script and data")
        sys.exit(-1)

    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not is_valid_name(args.instance):
        print(f"Invalid instance name {args.instance!r}")
        sys.exit(-1)

    # Create Directories
    apps_path = Path(APPS_DIR)
    try:
        apps_path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(exc)
        sys.exit(exc.errno)

    # Read spec
    spec_path = get_self_zipfile_path() / ZIPFILE_SPEC
    if not spec_path.exists():
        print("no spec")
        sys.exit(-1)

    spec = json.loads(spec_path.read_text())

    app_path = apps_path / args.name
    instance_path = app_path / args.instance
    if instance_path.exists():
        print("instance name not available")
        sys.exit(-1)

    if app_path.exists():
        app_spec_path = app_path / APP_SPEC
        if app_spec_path.exists():
            app_spec = json.loads(app_spec_path.read_text())

            if spec["hash"] != app_spec["hash"]:
                print("name not available")
                sys.exit(-1)

    try:
        app_path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(exc)
        sys.exit(exc.errno)

    # Unpack
    script_path = app_path / spec["script"]
    app_spec_path = app_path / APP_SPEC
    if not script_path.exists() or not app_spec_path.exists():
        try:
            print(f"Unpack script to {app_path}")
            script_path.write_bytes(
                get_self_zipfile_path().joinpath(spec["script"]).read_bytes()
            )

            print(f"Write {app_spec_path.name}")
            app_spec_path.write_text(
                json.dumps({"script": script_path.name, "hash": spec["hash"]})
            )

        except OSError as exc:
            print(exc)
            sys.exit(exc.errno)

    try:
        instance_path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(exc)
        sys.exit(exc.errno)

    print(f"Unpack data to {instance_path}")

    zf = get_self_zipfile()
    data_dir = (
        ZIPFILE_DATA_DIR if ZIPFILE_DATA_DIR.endswith("/") else f"{ZIPFILE_DATA_DIR}/"
    )
    for zi in [
        zi
        for zi in zf.filelist
        if zi.filename.startswith(data_dir) and not zi.filename.endswith("/")
    ]:
        target_path = instance_path / zi.filename[len(data_dir) :]

        print(f"Extract {zi.filename} => {target_path}")

        if zi.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
        else:
            with zf.open(zi) as io:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.write_bytes(io.read())

    arguments = spec["args"] or ""
    service_file_path = Path("/lib/systemd/system").joinpath(
        SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
    )
    print(f"Write {service_file_path}")
    service_file_path.write_text(
        "[Unit]\n"
        "Description=Telegram bot, Raffle bot.\n"
        "After=syslog.target\n"
        "After=network.target\n"
        "\n"
        "[Service]\n"
        f"WorkingDirectory={instance_path}\n"
        f"ExecStart=/usr/bin/python3 {script_path} {arguments}\n"
        f"ExecReload=/usr/bin/python3 {script_path} {arguments}\n"
        "KillSignal=SIGINT\n"
        "Restart=always\n"
        "RestartSec=10\n"
        "\n"
        "[Install]\n"
        "WantedBy=multi-user.target\n"
        "\n"
    )


def status(args):
    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not is_valid_name(args.instance):
        print(f"Invalid instance name {args.instance!r}")
        sys.exit(-1)

    service_name = SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
    os.system(f"systemctl status {service_name}")


def start(args):
    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not is_valid_name(args.instance):
        print(f"Invalid instance name {args.instance!r}")
        sys.exit(-1)

    service_name = SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
    if os.system(f"systemctl is-enabled -q {service_name}") != 0:
        os.system(f"systemctl enable {service_name}")

    os.system(f"systemctl start {service_name}")


def stop(args):
    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not is_valid_name(args.instance):
        print(f"Invalid instance name {args.instance!r}")
        sys.exit(-1)

    service_name = SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
    if os.system(f"systemctl is-enabled -q {service_name}") == 0:
        os.system(f"systemctl disable {service_name}")

    os.system(f"systemctl stop {service_name}")


def restart(args):
    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not is_valid_name(args.instance):
        print(f"Invalid instance name {args.instance!r}")
        sys.exit(-1)

    service_name = SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
    os.system(f"systemctl restart {service_name}")


def remove(args):
    if not is_valid_name(args.name):
        print(f"Invalid name {args.name!r}")
        sys.exit(-1)

    if not args.all:
        if not args.instance:
            print("instance name required")
            sys.exit(-1)

        if not is_valid_name(args.instance):
            print(f"Invalid instance name {args.instance!r}")
            sys.exit(-1)

        stop(args)
        service_name = SERVICE_FILE_TMPL.format(name=args.name, instance=args.instance)
        service_path = Path("/lib/systemd/system") / service_name
        print(f"Remove {service_path}")
        if service_path.exists():
            service_path.unlink()
        else:
            print(f"No file {service_path}")

        instance_path = Path(APPS_DIR) / args.name / args.instance
        if instance_path.exists():
            print(f"Remove {instance_path}")
            shutil.rmtree(instance_path)
        else:
            print(f"No directory {instance_path}")

    else:
        app_path = Path(APPS_DIR) / args.name
        if app_path.exists():
            for dir_name in (e.name for e in app_path.iterdir() if e.is_dir()):
                stop(argparse.Namespace(name=args.name, instance=dir_name))
                service_name = SERVICE_FILE_TMPL.format(
                    name=args.name, instance=dir_name
                )
                service_path = Path("/lib/systemd/system") / service_name
                if service_path.exists():
                    print(f"Remove {service_path}")
                    service_path.unlink()
                else:
                    print(f"No file {service_path}")

            print(f"Remove {app_path}")
            shutil.rmtree(app_path)

        else:
            print(f"No directory {app_path}")


def main():
    arg_parser = argparse.ArgumentParser()
    subparsers = arg_parser.add_subparsers(dest="command")

    # Build
    parser_build = subparsers.add_parser("build")
    parser_build.add_argument(
        "-s", "--script", help="path to python script", required=True
    )
    parser_build.add_argument(
        "-d", "--data", help="directory or file with data, settings or configs"
    )
    parser_build.add_argument(
        "-i", "--interpreter", help="interpreter for file shebang"
    )
    parser_build.add_argument(
        "-o", "--output", default="o.pyz", help="output file name"
    )
    parser_build.add_argument("-a", "--args", default="", help="script arguments")
    parser_build.add_argument(
        "-m", "--meta", metavar="KEY=VALUE", nargs="+", help="meta data"
    )

    # Meta
    parser_meta = subparsers.add_parser("meta")
    parser_meta.add_argument("keys", nargs="*", help="key of value")

    # Info
    parser_info = subparsers.add_parser("info")
    parser_info.add_argument("keys", nargs="*", help="key of value")

    # List
    parser_list = subparsers.add_parser("list")

    # Unpack
    parser_unpack = subparsers.add_parser("unpack")
    parser_unpack.add_argument(
        "-s", "--script", help="directory where to unpack the script"
    )
    parser_unpack.add_argument(
        "-d", "--data", help="directory where to unpack the data"
    )

    # Setup
    parser_setup = subparsers.add_parser("setup")
    parser_setup.add_argument("-n", "--name", help="app name", required=True)
    parser_setup.add_argument("-i", "--instance", help="instance name", required=True)

    # Status
    parser_status = subparsers.add_parser("status")
    parser_status.add_argument("-n", "--name", help="app name", required=True)
    parser_status.add_argument("-i", "--instance", help="instance name", required=True)

    # Start
    parser_start = subparsers.add_parser("start")
    parser_start.add_argument("-n", "--name", help="app name", required=True)
    parser_start.add_argument("-i", "--instance", help="instance name", required=True)

    # Stop
    parser_stop = subparsers.add_parser("stop")
    parser_stop.add_argument("-n", "--name", help="app name", required=True)
    parser_stop.add_argument("-i", "--instance", help="instance name", required=True)

    # Restart
    parser_restart = subparsers.add_parser("restart")
    parser_restart.add_argument("-n", "--name", help="app name", required=True)
    parser_restart.add_argument("-i", "--instance", help="instance name", required=True)

    # Remove
    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("-n", "--name", help="app name", required=True)
    parser_remove.add_argument("-i", "--instance", help="instance name")
    parser_remove.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="remove the entire app and all instances",
    )

    # Execute
    args = arg_parser.parse_args()
    if args.command == "build":
        build(args)
    elif args.command == "meta":
        meta(args)
    elif args.command == "info":
        info(args)
    elif args.command == "list":
        list_instances(args)
    elif args.command == "unpack":
        unpack(args)
    elif args.command == "setup":
        setup(args)
    elif args.command == "status":
        status(args)
    elif args.command == "start":
        start(args)
    elif args.command == "stop":
        stop(args)
    elif args.command == "restart":
        restart(args)
    elif args.command == "remove":
        remove(args)
    else:
        arg_parser.print_usage()


if __name__ == "__main__":
    main()
