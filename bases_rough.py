# ENCODE ---> TURNING FROM BASE TEN TO BASE TWO 

    remainder = int(number)
    #print(type(remainder))
    if remainder == 0:
        return "0"
    base_two = ""

    # ======================================================
    # ROUGH DRAFT FOR IDEAS
    # while remainder > 0
    #   base_power = 0
    #   while
    #       base_power increments to the greatest it can be while being less than remainder
    #       if base_power is chosen, add 1 to base_two
    #       else base_power is not chosen, add 0 to base_two
    #    base_power decrements
    #
    # ======================================================



    while remainder > 0:
        base_power = 0
        print "check point 1: r=" + str(remainder) + " b=" + str(base) + " bp=" + str(base_power)
        # binary_digit = 0
        # print "base ** base_power is equal to " + str(base ** base_power)
        while remainder - base ** base_power > remainder / 2:
            base_power += 1
            base_two += str(0)
            print "check point 2: r=" + str(remainder) + " bp=" + str(base_power) + " base_two=" + str(base_two)
        print "check point 3: r=" +str(remainder) + " bp=" + str(base_power) + " base_two=" + str(base_two)
        remainder = remainder - base ** base_power
        print "remainder is equal to " + str(remainder)
        base_two += str(1)
    print base_two[::-1]
    return base_two[::-1]
