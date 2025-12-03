def main():
    invalid_id_sum = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        ranges = file.readlines()[0].strip().split(",")

        for r in ranges:
            start = r.split("-")[0]
            end = r.split("-")[1]

            if len(start) % 2 != 0 and len(start) == len(end):
                # an entire range of IDs with the same odd number length contains no invalid IDs
                pass
            else:
                range_r = range(int(start), int(end) + 1)
                for i in range_r:
                    str_i = str(i)
                    if len(str_i) % 2 != 0:
                        # an ID with an odd number length is always valid
                        pass
                    else:
                        if str_i[:int(len(str_i) / 2)] == str_i[int(len(str_i) / 2):]:
                            # if the first half of the ID matches the last half, it's an invalid ID
                            invalid_id_sum += i
                        else:
                            pass

    print("The sum of all the invalid IDs in the ranges is ", invalid_id_sum)
        

if __name__ == '__main__':
    main()