import argparse
import gzip
import os
import shutil
import sys
import threading


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', nargs=1, required=True, help='Target Backup folder')
    parser.add_argument('-s', '--source', nargs='+', required=True, help='Source folders to back up')
    parser.add_argument('-c', '--compress', nargs=1, type=int, help='Gzip threshold in bytes (Default 1024KB)', default=[1024000])
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    return parser.parse_args()


def size_if_newer(source, target):
    try:
        src_stat = os.stat(source)
        try:
            target_ts = os.stat(target).st_mtime
        except FileNotFoundError:
            try:
                target_ts = os.stat(target + '.gz').st_mtime
            except FileNotFoundError:
                target_ts = 0

        return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False

    except FileNotFoundError:
        return False


def transfer_file(source, target, compress_threshold):
    try:
        file_size = os.path.getsize(source)
        if file_size > compress_threshold:
            with gzip.open(target + '.gz', 'wb') as target_fid:
                with open(source, 'rb') as source_fid:
                    shutil.copyfileobj(source_fid, target_fid)
            print(f'Compressed: {source}')
        else:
            shutil.copy2(source, target)
            print(f'Copied: {source}')
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        transfer_file(source, target, compress_threshold)


def threaded_sync_file(source, target, compress_threshold):
    size = size_if_newer(source, target)
    if size:
        thread = threading.Thread(target=transfer_file, args=(source, target, compress_threshold))
        thread.start()
        return thread
    return None


def sync_root(root, arg):
    target_base = arg.target[0]
    compress_threshold = arg.compress[0]
    threads = []

    for path, _, files in os.walk(root):
        for filename in files:
            full_source_path = os.path.join(path, filename)
            rel_path = os.path.relpath(full_source_path, root)
            full_target_path = os.path.join(target_base, rel_path)

            thread = threaded_sync_file(full_source_path, full_target_path, compress_threshold)
            if thread:
                threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    args = parse_input()
    print('------------------------- Start Copy -------------------------')
    print('______________________________________________________________')
    for root_folder in args.source:
        sync_root(root_folder, args)
    print('______________________________________________________________')
    print('------------------------- Done Done! -------------------------')
