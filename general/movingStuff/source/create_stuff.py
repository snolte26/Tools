from time import perf_counter


def main():
    timerStart = perf_counter()
    for i in range(50):
        fileNum = str(i)
        name = "newFile_" + fileNum + ".txt"
        try:
            newFile = open(name, "w+")
            newFile.close()
            print("Successfully created " + name)
        except:
            print("Failed to create " + name)
    print("Done!")
    timerEnd = perf_counter()
    print()
    print(f'Time Elapsed: {timerEnd - timerStart} seconds')
    input()


if __name__ == '__main__':
    main()
