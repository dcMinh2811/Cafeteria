count = 0
def Mark(Row, i, left_side, right_side):
    global count
    Row[i] = i+1
    count += 1
    # print("left side:",left_side)
    # print("right side:",right_side)
    print("Dropped:", Row[i])
    print("end\n\n\n")

def Main(Seats, N, K, M):
    global count
    count = 0
    if len(Seats.split()) == M and K >= 0 and N > 0 and M >= 0 and K < N and M <= N:
        Row = ["-"] * N

        for seat in Seats.split():
            seat = int(seat)
            if seat not in Row and seat > 0 and seat <= N:
                Row[seat-1] = seat

        for i in range(N):
            if i+1 not in Row:
                current = Row[i]
                print("\n\n\ncurrent:",current)
                print("i:",i)
                left_side = Row[i-K:i]
                right_side = Row[i+1:i+K+1]
                if len(right_side) >= K and i == 0 and right_side == ["-"] * K:
                    Mark(Row, i, left_side, right_side)

                elif len(left_side) == K and left_side == ["-"] * K and N-i-1 <= K and right_side == ["-"] * (N-i-1):
                    Mark(Row, i, left_side, right_side)

                elif left_side == right_side:
                    Mark(Row, i, left_side, right_side)

                continue

        print("\n\n\n\n\n------------------------------")
        print(Row)
        print("\n")
        print(count)

while True:
    N = int(input("Enter the amount of seats (N): "))
    K = int(input("Enter the distance (K): "))
    M = int(input("Enter the number of people (M): "))
    S = input("Enter the seats (S): ")

    Main(S, N, K, M)