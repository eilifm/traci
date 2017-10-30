import shutil
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    print("Building TraCI module")
    src_files = os.listdir('sumo/tools/traci/')
    for file_name in src_files:
        full_file_name = os.path.join('sumo/tools/traci/', file_name)
        if (os.path.isfile(full_file_name)):
            print("copying...%s to ./traci" % full_file_name)
            shutil.copy(full_file_name, './traci')


if __name__ == "__main__":
    main()