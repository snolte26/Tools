from time import perf_counter
import os
import shutil


def main():

    source = input("Source: ")
    print()
    destin = input("Destination: ")
    print()

    print("Working...")
    timerStart = perf_counter()
    print()

    dirlist = os.listdir(source)
    for f in dirlist:
        if f.endswith(".mp3"):
            try:
                srcs = source + "\\" + f
                des = destin + "\\" + f

                dest = shutil.copytree(srcs, des)

                print("Successfully copied " + str(f))
            except:
                print("Failed to move " + str(f))
    print("Done")
    timerEnd = perf_counter()
    print()
    print(f'Time Elapsed: {timerEnd - timerStart} seconds')
    input()


if __name__ == '__main__':
    main()
