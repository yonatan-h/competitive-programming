if __name__ == '__main__':
    num_commands = int(input())

    result = []

    for i in range(num_commands):
        instruction = input().split()
        command = instruction[0]

        if command == "print":
            print(result)
        else:
            pythonish_arguments = ",".join(instruction[1:])
            pythonish = f"result.{command}({pythonish_arguments})"
            exec(pythonish)

#30min
#2sub

